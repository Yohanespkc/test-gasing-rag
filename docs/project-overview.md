# Gambaran Umum Proyek: gasing-rag

**Versi:** 1.0.0
**Tanggal Dokumen:** 2026-05-17
**Status:** Stabil — Production Ready (v1.0.0, topik penjumlahan)

---

## Ringkasan Eksekutif

**gasing-rag** adalah AI Tutor matematika Sekolah Dasar berbasis Retrieval-Augmented Generation (RAG) yang dirancang khusus untuk Metode GASING (Gampang, Asyik, dan Menyenangkan). Sistem ini berperan sebagai tutor digital yang menjelaskan soal penjumlahan menggunakan pedagogik GASING secara akurat dan konsisten.

Sistem ini merupakan **evolusi arsitektur** dari pendekatan *prompt-only* (modelfile v44, 1671 baris / ~70 KB) menjadi arsitektur RAG yang lebih efisien — hanya mengirim 5–15 KB konteks relevan per query, bukan seluruh knowledge base di setiap request.

**Pencapaian v1.0.0:**
- ✅ 22 chunks Markdown knowledge base (penjumlahan)
- ✅ 100% math accuracy pada 40 test cases otomatis
- ✅ Hybrid retrieval: rule-based + semantic vector search
- ✅ Ekspansi otomatis konteks shared (komutativitas, format mencongak, dll.)
- ✅ Pipeline ingest → query → chat → validasi yang lengkap

---

## Stack Teknologi

| Kategori | Teknologi | Versi | Peran |
|---|---|---|---|
| **Bahasa** | Python | 3.10+ | Semua pipeline |
| **LLM Runtime** | Ollama | ≥0.4.0 (client) | Menjalankan model lokal |
| **LLM Model** | Gemma 3:4b / Gemma 4 | — | Generasi respons tutor |
| **Embedding Model** | nomic-embed-text | 274 MB | Vector embedding 768 dimensi |
| **Vector Database** | ChromaDB | ≥0.5.0 | Penyimpanan dan pencarian vektor |
| **Knowledge Base** | Markdown (22 chunks) | — | Dokumen pedagogik GASING |
| **Version Control** | Git + GitHub | — | `Yohanespkc/test-gasing-rag` |

---

## Arsitektur Sistem

```
User Query
    │
    ▼
[Classifier Rule-Based]        ← classify_soal() di utils.py
    │ Jenis soal (Nol/A1/.../F)
    ▼
[Hybrid Retrieval]             ← retrieve_chunks() di utils.py
    ├── Rule-based: force-load chunk per jenis
    └── Semantic: embedding query → ChromaDB cosine search
    │
    ▼
[Shared Expansion]             ← konsep_terkait di frontmatter chunk
    │ Tambah S01-S05 yang dibutuhkan
    ▼
[Context Formatting]           ← format_context()
    │ Susun: shared chunks dulu → per_jenis chunks
    ▼
[Ollama LLM Call]              ← gemma3:4b / gasing-rag modelfile
    │ SYSTEM prompt + history + augmented user message
    ▼
Response Tutor GASING
```

---

## Klasifikasi Jenis Soal (Rule-Based)

| Kode | Deskripsi | Contoh |
|---|---|---|
| Nol | Salah satu operand = 0 | 7 + 0 |
| A1 | 1d+1d, hasil 1–5 | 2 + 3 |
| A2 | 1d+1d, hasil 6–10 | 6 + 4 |
| B1 | 10 + X | 10 + 7 |
| B2 | X + 10 | 5 + 10 |
| B3 | 1d+1d, hasil 11–19 | 9 + 5 |
| C | 2 digit + 1 digit | 25 + 7 |
| D | Maks 2 digit (2d+2d atau 1d+2d) | 37 + 29 |
| E | 3 digit | 106 + 287 |
| F | 4+ digit | 4859 + 3148 |

---

## Struktur Direktori

```
gasing-rag/
├── chunks/                         Knowledge base (22 chunks Markdown)
│   ├── shared/                     5 chunks konsep lintas jenis
│   │   ├── S01_konfigurasi_jari.md
│   │   ├── S02_komutativitas.md
│   │   ├── S03_format_mencongak_universal.md
│   │   ├── S04_format_dua_cara.md
│   │   └── S05_aturan_1_kecil.md
│   └── per_jenis/                  17 chunks aturan per jenis soal
│       ├── J00_nol.md … J96_f_mencongak.md
├── scripts/                        Pipeline Python
│   ├── utils.py                    Helper: load, embed, retrieve, format
│   ├── 01_ingest.py                Ingest chunks → ChromaDB
│   ├── 02_query.py                 Test retrieval standalone
│   ├── 03_chat.py                  Chat interaktif (entry point utama)
│   ├── 05_validate.py              Validasi otomatis 40 test cases
│   └── generate_*.py               Regenerasi konten chunks
├── chroma_db/                      Persistent vector store (5 MB)
├── Model-gasing-rag.modelfile      Custom Ollama modelfile (SYSTEM ramping)
├── system_prompt.txt               SYSTEM prompt runtime (dipakai 03_chat.py)
├── system_prompt_v44_ramping.md    SYSTEM prompt versi panjang (referensi)
├── chunks_index.json               Metadata index semua chunks
├── requirements.txt                Python dependencies
├── SETUP.md                        Panduan setup lengkap
├── README.md                       Dokumentasi arsitektur RAG
└── docs/                           BMAD documentation output
```

---

## Mode Interaksi

Sistem mendukung dua mode pembelajaran GASING:

- **Mode B (Belajar):** Tutor menjelaskan langkah demi langkah dengan konsep GASING lengkap (konfigurasi jari, lirik kanan, aturan 1-kecil, komutativitas)
- **Mode C (Mencongak):** Format singkat — hanya jawaban + alasan singkat, tanpa penjelasan panjang

Trigger:
- `B: berapa 25 + 7` → Mode Belajar
- `C: berapa 25 + 7` → Mode Mencongak

---

## Target Pengguna Dokumen Ini

| Audiens | Kebutuhan Utama |
|---|---|
| **Tim IT-DEL** | Setup lokal, arsitektur teknis, cara extend ke topik baru |
| **GASING Academy** | Pemahaman pedagogik dalam sistem, cara validasi output |
| **Developer** | API utils.py, cara tambah chunks baru, cara retraining |
