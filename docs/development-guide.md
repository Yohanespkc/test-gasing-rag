# Panduan Developer: gasing-rag

**Versi:** 1.0.0
**Tanggal Dokumen:** 2026-05-17

---

## Prasyarat

| Kebutuhan | Versi Minimum | Cara Cek |
|---|---|---|
| Python | 3.10+ | `python3 --version` |
| Ollama | Terbaru | `ollama --version` |
| macOS | (diuji di Apple Silicon M-series) | — |
| RAM | 8 GB minimum, 16 GB direkomendasikan | — |
| Disk | 5 GB bebas (untuk model Ollama) | — |

---

## Setup Awal (Sekali Saja)

### 1. Clone Repository

```bash
git clone https://github.com/Yohanespkc/test-gasing-rag.git
cd test-gasing-rag
```

### 2. Setup Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

Verifikasi:
```bash
python -c "import ollama, chromadb; print('Dependencies OK')"
```

### 3. Pull Model Ollama

```bash
# Pastikan Ollama service berjalan
ollama serve &    # atau jalankan di terminal terpisah

# Pull embedding model (274 MB, sekali saja)
ollama pull nomic-embed-text

# Pull LLM (opsional jika ingin pakai versi berbeda)
ollama pull gemma4:e4b   # model yang divalidasi (gemma4:e4b)
```

Verifikasi:
```bash
ollama list | grep -E "nomic|gemma"
```

### 4. Build Index ChromaDB

```bash
cd scripts
python 01_ingest.py
```

Output sukses:
```
GASING RAG: Ingest Chunks ke ChromaDB
[1/4] Cek Ollama dan model nomic-embed-text... OK
[2/4] Load chunks dari disk... Loaded 22 chunks
[3/4] Buat koleksi ChromaDB... Koleksi siap
[4/4] Embed setiap chunk...
Selesai dalam ~8 detik. Total: 22 chunks.
```

### 5. (Opsional) Buat Custom Modelfile

```bash
cd ..    # kembali ke root gasing-rag/
ollama create gasing-rag -f Model-gasing-rag.modelfile
```

---

## Menjalankan Sistem

### Chat Interaktif (Cara Utama)

```bash
cd scripts

# Dengan custom modelfile
python 03_chat.py --model gasing-rag

# Dengan model langsung
python 03_chat.py --model gemma4:e4b

# Mode debug (tampilkan chunks yang ter-retrieve)
python 03_chat.py --debug

# Mode baseline (tanpa RAG, untuk perbandingan)
python 03_chat.py --no-retrieval
```

**Perintah dalam sesi chat:**
- `/quit` — keluar
- `/debug` — toggle mode debug
- `/clear` — reset riwayat percakapan

**Format query:**
```
B: berapa 25 + 7      # Mode Belajar (penjelasan lengkap)
C: berapa 25 + 7      # Mode Mencongak (jawaban singkat)
```

### Test Retrieval Standalone

```bash
cd scripts
python 02_query.py "berapa 25 + 7"
python 02_query.py "B: 4859 + 3148"
python 02_query.py "soal 3 digit"
```

Output menampilkan chunks yang ter-retrieve beserta skor similarity (cosine distance).

### Validasi Otomatis

```bash
cd scripts

# Full validasi (40 test cases, pakai Gemma — ~8 menit)
python 05_validate.py

# Quick mode (hanya classify + retrieve, ~30 detik)
python 05_validate.py --quick

# Dengan model tertentu
python 05_validate.py --model gemma4:e4b

# Test cepat 10 cases pertama
python 05_validate.py --limit 10
```

Output disimpan ke:
- `validation_report.json` — detail per test case
- `validation_log.txt` — full response Gemma

---

## Regenerasi Chunks

Jika ada perubahan pada konten pedagogik, regenerasi chunks dengan:

```bash
cd scripts
python generate_shared_chunks.py        # chunks S01-S05
python generate_per_jenis_small.py      # chunks Nol hingga D
python generate_per_jenis_complex.py    # chunks E dan F
python generate_aux_files.py            # chunks_index.json dll
```

Setelah regenerasi, wajib re-ingest:
```bash
python 01_ingest.py                     # rebuild ChromaDB index
```

---

## Workflow Pengembangan

### Menambah Chunk Baru

1. Buat file `.md` baru di `chunks/per_jenis/` atau `chunks/shared/`
2. Ikuti skema frontmatter YAML yang sudah ada (lihat `J60_c.md` sebagai referensi)
3. Pastikan field `konsep_terkait` merujuk ke ID chunk shared yang valid
4. Jalankan `01_ingest.py` untuk rebuild index
5. Test retrieval dengan `02_query.py`
6. Jalankan `05_validate.py --quick` untuk cek tidak ada regresi

### Mengedit Chunk yang Ada

1. Edit file `.md` langsung
2. Re-ingest: `python 01_ingest.py` (idempotent — otomatis hapus koleksi lama)
3. Test query yang relevan
4. Commit ke git

### Menambah Topik Baru (misal: Pengurangan)

1. Buat folder `chunks/per_jenis_pengurangan/`
2. Buat chunk dengan `topik: "pengurangan"` di frontmatter
3. Update `classify_soal()` di `utils.py` untuk deteksi tanda operasi
4. Tambah `filter_topik` parameter di `retrieve_chunks()` call
5. Re-ingest → test → validasi

### Update System Prompt

1. Edit `system_prompt.txt` (untuk runtime injection via `03_chat.py`)
2. Edit bagian `SYSTEM` di `Model-gasing-rag.modelfile` (untuk custom model)
3. Jika edit modelfile, re-create: `ollama create gasing-rag -f Model-gasing-rag.modelfile`

---

## Troubleshooting

| Error | Penyebab | Solusi |
|---|---|---|
| `ERROR: Tidak bisa konek ke Ollama` | Ollama service mati | Jalankan `ollama serve` di terminal terpisah |
| `ERROR: Model nomic-embed-text belum di-pull` | Model belum diunduh | `ollama pull nomic-embed-text` |
| `Collection not found` | ChromaDB belum di-build | `python 01_ingest.py` |
| Retrieval mengambil chunk salah | Embedding kurang tepat | Tambah keyword di chunk; coba `bge-m3` sebagai embedding model |
| Gemma jawab salah meski chunk benar | LLM terlalu kecil atau temperature tinggi | Coba `qwen2.5:7b`; turunkan temperature di Modelfile |
| `chroma_db/` rusak | Disk penuh atau proses terputus | Hapus folder, re-ingest dari awal |

---

## Konvensi Kode

- **Bahasa:** Python 3.10+, tidak ada type hints wajib tapi dianjurkan
- **Style:** Docstring Indonesia, komentar Indonesia
- **ID chunk:** Format `J{nomor}_{nama_jenis}.md` atau `S{nomor}_{nama_konsep}.md`
- **Tidak boleh ada:**
  - Em-dash (`—`) di dalam konten chunks (aturan v44)
  - Kata `simpan` atau `carry` (diganti dengan `₁` atau `1-kecil`)
  - Hard-coded path (gunakan `BASE` dari `utils.py`)

---

## Catatan Maintenance

- `chroma_db/` harus di-backup jika dipakai di produksi
- Setelah edit chunk, SELALU re-run `01_ingest.py` sebelum test
- `system_prompt.txt` dan `Model-gasing-rag.modelfile` harus selalu sinkron isinya
- File `validation_report.json` dan `validation_log.txt` di-gitignore (atau di-commit hanya saat release)
