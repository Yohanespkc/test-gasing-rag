# SETUP.md: Setup GASING RAG di Mac Pak

Panduan ini asumsikan Pak sudah punya:
- Ollama terinstall dan berjalan (`ollama serve`)
- Python 3.10 atau lebih baru
- MacBook M5 Max (atau Mac mana saja dengan RAM cukup)

## Langkah 1: Extract Proyek

Setelah download `gasing-rag.tar.gz`:

```bash
cd ~/Documents   # atau folder kerja Pak yang lain
tar -xzf ~/Downloads/gasing-rag.tar.gz
cd gasing-rag
```

Struktur direktori setelah extract:

```
gasing-rag/
├── chunks/                              22 chunks .md
├── scripts/
│   ├── utils.py
│   ├── 01_ingest.py
│   ├── 02_query.py
│   ├── 03_chat.py
│   ├── generate_*.py                    (untuk regenerate chunks)
├── chroma_db/                           (akan dibuat oleh ingest)
├── Model-gasing-rag.modelfile           Modelfile dengan SYSTEM ramping
├── README.md
├── SETUP.md                             file ini
├── chunks_index.json
├── requirements.txt
├── system_prompt.txt
└── system_prompt_v44_ramping.md
```

## Langkah 2: Setup Python Virtual Environment

```bash
cd ~/Documents/gasing-rag

# Buat virtualenv (sekali saja)
python3 -m venv .venv

# Aktifkan
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Cek versi:

```bash
python -c "import ollama, chromadb; print('OK')"
```

## Langkah 3: Pull Model Embedding

ChromaDB butuh embedding model. Kita pakai `nomic-embed-text` (768
dimensi, multilingual termasuk Bahasa Indonesia, gratis dari Ollama).

```bash
ollama pull nomic-embed-text
```

Ukuran model sekitar 274 MB. Sekali pull, dipakai selamanya.

Verifikasi Pak punya Gemma 3:4b juga (yang dipakai oleh AI Tutor):

```bash
ollama list | grep gemma
```

Kalau belum ada, pull:

```bash
ollama pull gemma3:4b
```

## Langkah 4: Build Index ChromaDB

```bash
cd scripts
python 01_ingest.py
```

Output yang diharapkan:

```
============================================================
GASING RAG: Ingest Chunks ke ChromaDB
============================================================

[1/4] Cek Ollama dan model nomic-embed-text...
      OK

[2/4] Load chunks dari disk...
      Loaded 22 chunks:
        shared: 5
        per_jenis: 17

[3/4] Buat koleksi ChromaDB (delete koleksi lama kalau ada)...
      Koleksi siap

[4/4] Embed setiap chunk dan add ke ChromaDB...
      [ 1/22] J00_nol                                  ( 3178 chars)
      ...
      [22/22] S05_aturan_1_kecil                       ( 3915 chars)

============================================================
Selesai dalam 8.3 detik
Total chunks ter-index: 22
ChromaDB persistence: ./chroma_db/
============================================================
```

ChromaDB akan menyimpan vector store di `../chroma_db/`. Folder ini
sekitar 5 MB.

## Langkah 5: Test Retrieval Standalone

Sebelum chat, test apakah retrieval benar:

```bash
python 02_query.py "berapa 25 + 7"
```

Output yang diharapkan:

```
Query: 'berapa 25 + 7'

Retrieving (top_k=3 + ekspansi shared via konsep_terkait)...

Dapat 5 chunks total

======================================================================

[1] S02_komutativitas
    kategori: shared
    via konsep_terkait
    preview: # KOMUTATIVITAS GASING ## Prinsip Penjumlahan...

[2] S03_format_mencongak_universal
    kategori: shared
    via konsep_terkait
    preview: # FORMAT MENCONGAK UNIVERSAL ## Struktur Output...

[3] J60_c
    kategori: per_jenis
    distance=0.4123
    preview: # JENIS C: 2 digit + 1 digit ## Klasifikasi Jenis C...

[4] J70_d
    kategori: per_jenis
    distance=0.5234
    preview: # JENIS D: maks 2 digit (2d+2d atau 1d+2d)...

[5] J20_a2
    kategori: per_jenis
    distance=0.5612
    preview: # JENIS A2: kedua operand 1 digit...
```

Yang penting J60_c muncul di top hasil (karena 25 + 7 memang Jenis C),
dan shared chunks yang relevan (S02 untuk komutativitas, S03 untuk
format mencongak) ikut ter-include via ekspansi konsep_terkait.

Coba beberapa query lain:

```bash
python 02_query.py "B: 4859 + 3148"
python 02_query.py "operand 0"
python 02_query.py "soal 3 digit"
```

## Langkah 6: Buat Model Ollama dari Modelfile

```bash
cd ..   # kembali ke gasing-rag/
ollama create gasing-rag -f Model-gasing-rag.modelfile
```

Output yang diharapkan:

```
transferring model data
using existing layer sha256:...
creating new layer sha256:...
writing manifest
success
```

Verifikasi:

```bash
ollama list | grep gasing-rag
```

## Langkah 7: Chat Interaktif

```bash
cd scripts
python 03_chat.py --model gasing-rag
```

Atau pakai gemma3:4b langsung (tanpa custom modelfile, SYSTEM prompt
disuntik via runtime):

```bash
python 03_chat.py --model gemma3:4b
```

Contoh sesi:

```
======================================================================
GASING Tutor RAG (model: gasing-rag, retrieval: True)
Ketik /quit untuk keluar, /debug untuk toggle debug mode
======================================================================

User: B: 25 + 7

Tutor: Mantap! Kita akan belajar matematika sekarang.
Pakai cara cepat GASING.
Puluhan: 2
Lirik kanan satuan 5 + 7 = 12, lebih dari atau sama dengan 10.
Tambah 1 ke puluhan.
Puluhan jadi 2 + 1 = 3.
Satuan: 12, ambil 2 (karena 1-nya ke puluhan).
Jadi 25 + 7 = 32.

Dan lihat ya, 25 + 7 hasilnya 32, dan kalau dibalik, 7 + 25 juga
hasilnya 32.

User: /debug
[debug mode: True]

User: C: 113 + 287

[DEBUG] Retrieved 4 chunks:
  [shared   ] S03_format_mencongak_universal             (expanded)
  [shared   ] S04_format_dua_cara                        (expanded)
  [shared   ] S05_aturan_1_kecil                         (expanded)
  [per_jenis] J83_e_cascade_1_kecil                      (0.387)

Tutor: Berapa 113 + 287?
Jawab: 113 + 287 = 400
Alasan: Dikerjakan dari depan (mulai dari ratusan)
ratusan 1 + 2 = 3
lirik kanan, jumlah puluhan 9, lirik kanan lagi satuannya 10.
Ratusannya bertambah 1, puluhannya juga bertambah 1.
Jadi ratusannya 3 + 1 = 4
Puluhannya 9 + 1 = 10 (ambil 0)
Satuan 3 + 7 = 10, ambil 0
Jadi 113 + 287 = 400

Cara singkat: 113 + 287 = 39₁0 = 400
```

## Perintah Khusus di Chat

Di dalam sesi chat, Pak bisa pakai:

- `/quit` - keluar
- `/debug` - toggle tampilan chunks yang ter-retrieve
- `/clear` - reset history percakapan (mulai sesi baru)

## Mode Testing Tanpa RAG

Untuk bandingkan dengan baseline tanpa retrieval:

```bash
python 03_chat.py --model gasing-rag --no-retrieval
```

Mode ini hanya pakai SYSTEM prompt ramping, tanpa inject konteks
chunks. Ini akan menunjukkan bahwa SYSTEM ramping saja tidak cukup,
dan chunks memang membawa nilai.

## Troubleshooting

### "Tidak bisa konek ke Ollama"
Pastikan Ollama jalan. Buka terminal lain dan jalankan `ollama serve`.

### "Model nomic-embed-text belum di-pull"
```bash
ollama pull nomic-embed-text
```

### Retrieval mengambil chunks yang salah
Cek dengan `python 02_query.py "query Pak"` untuk lihat skor distance.
Kalau chunks yang relevan distance-nya tinggi (>0.6), pertimbangkan:
1. Tambah kata kunci di pertanyaan (misal "B: berapa 25 + 7" lebih
   informatif daripada "25+7")
2. Edit chunks supaya keyword lebih jelas (tambah contoh di section
   Klasifikasi)
3. Coba embedding model lain (bge-m3 sering lebih akurat untuk multilingual)

### Gemma jawab salah meskipun chunks benar
Cek dengan `--debug` mode apakah chunks yang relevan ada di konteks.
Kalau iya tapi Gemma tetap jawab salah, mungkin:
1. SYSTEM prompt ramping kurang tegas → edit system_prompt.txt
2. Gemma 3:4b terlalu kecil → coba qwen2.5:7b atau llama3.1:8b
3. Temperature terlalu tinggi → turunkan ke 0.1 di Modelfile

## Validasi Sistematis

Setelah pipeline jalan, lakukan validasi:

1. Ambil 50 soal test bank Pak (yang sedang dikembangkan untuk A1).
2. Jalankan tiap soal via 03_chat.py (otomatis lewat script atau manual).
3. Bandingkan output dengan ekspektasi: jawaban benar, format sesuai,
   komutativitas ada untuk maks 2 digit, dst.
4. Hitung accuracy, format compliance, dan komutativitas presence.
5. Bandingkan dengan baseline v44 prompt-only.

Pak bisa buat script `04_validate.py` (saya bisa bantu kalau Pak mau).

## Ekspansi ke Topik Lain

Setelah penjumlahan stabil, ekspansi ke pengurangan:

1. Buat chunks `chunks/per_jenis_pengurangan/` dengan pola sama.
2. Update field `topik: "pengurangan"` di frontmatter.
3. Re-run ingest. Index akan punya chunks untuk dua topik.
4. Retrieval otomatis filter by topik berdasarkan klasifikasi soal.

Untuk klasifikasi soal pengurangan vs penjumlahan, tambah pre-processor
sederhana di 03_chat.py yang cek tanda operasi (+ atau −) di input,
lalu set `filter_topik` sesuai.

## Catatan Maintenance

- ChromaDB persistence di `chroma_db/`. Backup folder ini jika perlu.
- Setelah edit chunks .md, JANGAN lupa rerun `01_ingest.py` supaya
  ChromaDB sinkron dengan disk.
- Setelah edit `system_prompt.txt`, jangan lupa update juga isi SYSTEM
  di `Model-gasing-rag.modelfile` (atau buat script regen).
- Kalau lupa langkah ini, output Gemma akan tetap pakai versi lama
  karena cache.

## Selanjutnya

Setelah pipeline ini stabil, langkah natural berikutnya:
1. **A1 Test Bank Validation**: jalankan 50 soal, ukur accuracy
2. **A2 Senior Trainer Review**: review hasil dengan pelatih senior
3. **A3 Multimodal**: tambah dukungan gambar konfigurasi jari
4. **Ekspansi topik**: pengurangan, perkalian, pembagian
