# Arsitektur gasing-rag

**Versi:** 1.0.0
**Tanggal Dokumen:** 2026-05-17
**Tipe Arsitektur:** AI Pipeline — Hybrid Retrieval-Augmented Generation

---

## Ringkasan Eksekutif

gasing-rag mengimplementasikan pola **RAG (Retrieval-Augmented Generation)** untuk AI Tutor matematika SD berbasis Metode GASING. Arsitektur ini memisahkan knowledge (dalam chunks Markdown) dari logika generasi (model LLM), memungkinkan update knowledge tanpa retraining model.

Keunggulan utama dibanding pendekatan prompt-only (modelfile v44):

| Aspek | Prompt-Only (v44) | RAG (gasing-rag) |
|---|---|---|
| Context per query | ~70 KB (seluruh knowledge) | 5–15 KB (hanya yang relevan) |
| Update knowledge | Edit 1671 baris modelfile | Edit chunk .md spesifik |
| Akurasi matematika | Baik | 100% (40 test cases) |
| Skalabilitas topik | Sulit (semua di satu file) | Mudah (tambah folder baru) |

---

## Komponen Arsitektur

### 1. Knowledge Base (chunks/)

Seluruh pengetahuan pedagogik GASING tersimpan sebagai file Markdown dengan frontmatter YAML.

**Struktur chunk:**
```yaml
---
id: J60_c
kategori: per_jenis
jenis_soal: C
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 2
pola: "2 digit + 1 digit"
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S02_komutativitas
  - S03_format_mencongak_universal
kompleksitas: menengah
punya_carry: true
punya_cascade_1_kecil: false
version_modelfile: v44
referensi_bagian_v44: "5.6"
---
# JENIS C: 2 digit + 1 digit
...konten pedagogik...
```

**Dua kategori chunk:**

| Kategori | Jumlah | Contoh | Fungsi |
|---|---|---|---|
| `shared` | 5 | S01–S05 | Konsep lintas jenis (jari, komutativitas, 1-kecil) |
| `per_jenis` | 17 | J00–J96 | Aturan spesifik per jenis soal |

**Relasi antar chunk:**
Field `konsep_terkait` di frontmatter membuat graf dependensi. Saat chunk `J60_c` di-retrieve, sistem otomatis menarik `S02_komutativitas` dan `S03_format_mencongak_universal`.

---

### 2. Vector Store (chroma_db/)

ChromaDB menyimpan embeddings dari semua 22 chunks dengan:
- **Embedding model:** `nomic-embed-text` (768 dimensi, multilingual)
- **Distance metric:** cosine similarity
- **Koleksi:** `gasing_chunks`
- **Metadata terindeks:** `topik`, `kategori`, `jenis_soal`, `kompleksitas`, dll.
- **Filter retrieval:** `where={"topik": "penjumlahan"}`

Setiap chunk di-embed termasuk frontmatter YAML-nya, sehingga keyword seperti "Jenis C", "operand 2 digit", dan "carry" membantu kualitas retrieval.

---

### 3. Hybrid Retrieval Engine (utils.py)

Sistem retrieval menggunakan dua jalur paralel:

```
Query User
    │
    ├── [Rule-Based Classifier]
    │       classify_soal(query) → Jenis (Nol/A1/.../F)
    │       JENIS_TO_CHUNKS[jenis] → force-load chunk spesifik
    │       Akurasi: deterministik, tidak bergantung embedding
    │
    └── [Semantic Search]
            embed(query) → nomic-embed-text vector
            ChromaDB.query(top_k=2) → chunks paling mirip
            Filter: topik="penjumlahan"
    │
    ▼
[Deduplication + Merge]
    │ Prioritas: rule-based > shared > semantic
    ▼
[Shared Expansion]
    Untuk setiap chunk per_jenis yang terpilih:
    → Baca field konsep_terkait
    → ChromaDB.get(ids=[...]) → tambah shared chunks
    ▼
[Sorting]
    (0) Rule-based chunks pertama
    (1) Shared chunks kedua
    (2) Semantic chunks terakhir
    ▼
Context Final (5–15 KB)
```

**Fungsi kunci di `utils.py`:**

| Fungsi | Peran |
|---|---|
| `classify_soal(text)` | Rule-based jenis detector (regex + angka) |
| `embed(text)` | Panggil nomic-embed-text via Ollama |
| `retrieve_chunks(query, top_k, expand_shared)` | Hybrid retrieval engine |
| `format_context(chunks)` | Format chunks → string konteks |
| `load_chunks()` | Load + parse semua .md dari disk |
| `parse_frontmatter(content)` | Parse YAML frontmatter |
| `flatten_metadata(m)` | Konversi list → string untuk ChromaDB |
| `load_system_prompt()` | Load system_prompt.txt |

---

### 4. LLM Layer (Ollama)

Model dijalankan lokal via Ollama. Dua opsi konfigurasi:

**Opsi A — Custom Modelfile:**
```bash
ollama create gasing-rag -f Model-gasing-rag.modelfile
python 03_chat.py --model gasing-rag
```
Modelfile meng-embed SYSTEM prompt ringkas + parameter (temperature, dll.)

**Opsi B — Runtime Injection:**
```bash
python 03_chat.py --model gemma3:4b
```
SYSTEM prompt disuntik dari `system_prompt.txt` setiap sesi.

**Message format per turn:**
```
[system]:  {system_prompt.txt}
[user]:    {query asli}
           <konteks_dokumen>
           {chunks terformat}
           </konteks_dokumen>
[assistant]: {respons Gemma}
[user]:    {query berikutnya — disimpan tanpa konteks, anti-bloat}
...
```

---

### 5. Pipeline Scripts

| Script | Fungsi | Cara Jalankan |
|---|---|---|
| `01_ingest.py` | Parse semua .md → embed → simpan ke ChromaDB | `python 01_ingest.py` |
| `02_query.py` | Test retrieval standalone (tanpa LLM) | `python 02_query.py "25 + 7"` |
| `03_chat.py` | Chat interaktif dengan RAG pipeline | `python 03_chat.py` |
| `05_validate.py` | Validasi otomatis 40 test cases | `python 05_validate.py` |
| `generate_*.py` | Regenerasi konten chunks dari source | `python generate_shared_chunks.py` |

---

### 6. Validation Framework (05_validate.py)

Framework validasi empat dimensi:

| Dimensi | Cara Cek | Target |
|---|---|---|
| **Classification** | `classify_soal()` → cocok `expected_jenis` | 100% |
| **Retrieval** | Chunk yang benar ada di hasil | 100% |
| **Math Accuracy** | Regex extract jawaban dari respons Gemma | 100% |
| **Format Compliance** | Regex detect feature (komutativitas, lirik_kanan, notasi_1_kecil, dll.) | Per jenis |

**Hasil validasi v1.0.0:**
- Classification: 40/40 (100%)
- Retrieval: 40/40 (100%)
- Math Accuracy: 40/40 (100%)
- Format: Sesuai requirement per jenis

---

## Data Flow Lengkap

```
[Edit chunks/per_jenis/*.md]
         │
         ▼
[python 01_ingest.py]
  → Load 22 .md files
  → Parse frontmatter YAML
  → embed() setiap chunk (nomic-embed-text)
  → ChromaDB.add() dengan metadata
  → Simpan ke chroma_db/ (persistent)
         │
         ▼ (chroma_db/ siap)
         │
[python 03_chat.py]
  │
  ├── User: "B: berapa 25 + 7"
  │         │
  │         ├── classify_soal() → "C"
  │         ├── JENIS_TO_CHUNKS["C"] → ["J60_c"]
  │         ├── ChromaDB.get(["J60_c"]) → forced chunk
  │         ├── embed("B: berapa 25 + 7") → vector
  │         ├── ChromaDB.query(top_k=2) → semantic chunks
  │         ├── konsep_terkait: ["S02", "S03"] → expand
  │         ├── format_context([J60_c, S02, S03, ...])
  │         └── ollama.chat(SYSTEM + [user+konteks])
  │
  └── Tutor: "Pakai cara cepat GASING. Puluhan: 2..."
```

---

## Keputusan Teknis Penting

### Kenapa ChromaDB bukan pgvector/Pinecone?
Proyek ini dirancang untuk berjalan **100% lokal** tanpa dependensi cloud. ChromaDB menyediakan persistent local storage tanpa setup server terpisah.

### Kenapa embed frontmatter YAML bersama konten?
Keyword di YAML (`jenis_soal: C`, `punya_carry: true`) memperkaya semantic retrieval. Query seperti "soal dengan carry" akan lebih mudah menyentuh chunk yang tepat.

### Kenapa rule-based classifier + semantic search (hybrid)?
- Rule-based: deterministik dan cepat untuk soal yang formatnya jelas (`B: 25 + 7`)
- Semantic: menangkap query ambigu atau deskriptif (`"soal yang ada cascade 1 kecil"`)

### Kenapa history disimpan tanpa konteks dokumen?
Untuk mencegah *context bloat*. Setelah LLM menjawab, history di-update dengan query asli (bukan augmented version). Sehingga sesi panjang tidak menghabiskan context window.

---

## Keterbatasan v1.0.0

| Keterbatasan | Dampak | Rencana v2.0 |
|---|---|---|
| Hanya topik penjumlahan | Tidak bisa jawab soal pengurangan/kali/bagi | Tambah chunks per topik |
| Tidak ada UI grafis | Hanya CLI, kurang aksesibel | Web interface (Streamlit/FastAPI) |
| Tidak ada multimodal | Tidak bisa proses gambar jari | Integrasi vision model |
| Tidak ada auth/session management | Single user, no logging per user | Multi-user support |
| chroma_db tidak di-backup otomatis | Risiko kehilangan index | Tambah backup script |
