# GASING RAG: Migrasi dari Prompt-Only ke Retrieval-Augmented Generation

Proyek ini adalah blueprint untuk migrasi AI Tutor GASING dari pendekatan
prompt-only (modelfile v44, 1671 baris) ke arsitektur RAG.

## Struktur Direktori

```
gasing-rag/
├── chunks/
│   ├── shared/                          5 chunks konsep dasar
│   │   ├── S01_konfigurasi_jari.md
│   │   ├── S02_komutativitas.md
│   │   ├── S03_format_mencongak_universal.md
│   │   ├── S04_format_dua_cara.md
│   │   └── S05_aturan_1_kecil.md
│   └── per_jenis/                       17 chunks aturan per jenis soal
│       ├── J00_nol.md
│       ├── J10_a1.md
│       ├── J20_a2.md
│       ├── J30_b1.md
│       ├── J40_b2.md
│       ├── J50_b3.md
│       ├── J60_c.md
│       ├── J70_d.md
│       ├── J81_e_tanpa_carry.md
│       ├── J82_e_carry_satuan_puluhan.md
│       ├── J83_e_cascade_1_kecil.md
│       ├── J91_f_pengantar_aturan.md
│       ├── J92_f_alignment_digit.md
│       ├── J93_f_belajar_simple.md
│       ├── J94_f_belajar_cascade.md
│       ├── J95_f_belajar_diff_digits.md
│       └── J96_f_mencongak.md
├── scripts/
│   ├── generate_shared_chunks.py        regenerate chunks shared
│   ├── generate_per_jenis_small.py      regenerate chunks Nol s.d. D
│   ├── generate_per_jenis_complex.py    regenerate chunks E dan F
│   └── generate_aux_files.py            regenerate file pendukung
├── system_prompt_v44_ramping.md         SYSTEM prompt untuk modelfile
├── chunks_index.json                    index metadata semua chunks
└── README.md
```

## Total Volume
22 chunks .md, ukuran sekitar 60 KB total (1.2 KB sampai 8.7 KB per chunk).
Sebagai perbandingan, modelfile v44 utuh sekitar 70 KB.

Yang lebih penting bukan penghematan total, tapi penghematan PER QUERY:
- Modelfile v44 mengirim 70 KB setiap pertanyaan.
- RAG hanya mengirim 5 sampai 15 KB per pertanyaan (3 sampai 5 chunks relevan).

## Skema Metadata

Setiap chunk punya frontmatter YAML dengan field berikut:

| Field | Tipe | Keterangan |
|---|---|---|
| id | string | Identifier unik chunk |
| kategori | enum | shared, per_jenis |
| jenis_soal | enum | Nol, A1, A2, B1, B2, B3, C, D, E, F (untuk per_jenis) |
| sub_kategori | string | sub-jenis (untuk E dan F) |
| topik | string | penjumlahan (akan jadi pengurangan, dst di masa depan) |
| operand_min_digit | int | digit minimum operand |
| operand_max_digit | int | digit maksimum operand |
| mode_tercakup | list | belajar, mencongak |
| konsep_terkait | list | id chunks shared yang dibutuhkan |
| kompleksitas | enum | dasar, menengah, tinggi, sangat_tinggi |
| punya_carry | bool | apakah jenis ini bisa carry |
| punya_cascade_1_kecil | bool | apakah pakai kaskade Aturan 1 Kecil |
| version_modelfile | string | v44 |

Metadata di-parse dari frontmatter YAML saat indexing ke ChromaDB,
lalu jadi filter saat retrieval.

## Strategi Retrieval Yang Direkomendasikan

1. Embed pertanyaan user pakai model `nomic-embed-text` atau `bge-m3`.
2. Query ChromaDB dengan filter `topik = "penjumlahan"`.
3. Ambil top 3 chunks berdasarkan similarity.
4. Untuk setiap chunk per_jenis yang masuk top 3, ambil juga chunks
   shared yang ada di field `konsep_terkait`.
5. Susun konteks final: chunks shared dulu, baru chunks per_jenis.
6. Kirim ke Gemma 3:4b dengan SYSTEM prompt ramping
   (lihat `system_prompt_v44_ramping.md`).

## Regenerasi Chunks

Script Python di `scripts/` bisa di-rerun jika ada perubahan konten.
Modifikasi chunk di script, lalu jalankan:

```bash
python3 scripts/generate_shared_chunks.py
python3 scripts/generate_per_jenis_small.py
python3 scripts/generate_per_jenis_complex.py
python3 scripts/generate_aux_files.py
```

Output akan menimpa file lama di `chunks/`. Untuk versioning, commit
ke Git setelah setiap regenerasi.

## Langkah Berikutnya (Implementasi RAG)

Setelah chunks ini siap, langkah implementasi:

1. **Install dependencies**: `pip install chromadb ollama langchain`
2. **Indexing script**: parse semua .md, embed, simpan ke ChromaDB.
3. **Retrieval script**: query ChromaDB berdasarkan pertanyaan user.
4. **Orchestration script**: gabungkan retrieval + Ollama call.
5. **Update modelfile**: ganti SYSTEM dengan `system_prompt_v44_ramping.md`,
   re-create dengan `ollama create gasing-rag -f Model-gasing-rag.modelfile`.
6. **Validation**: jalankan test bank 50 soal, bandingkan dengan v44.

## Catatan Fidelitas

Chunks ini ditulis berdasarkan modelfile v44 secara langsung.
Bahasa asli (Indonesia) dipertahankan. Notasi subscript ₁ dipakai
sebagai karakter Unicode. Em-dash tidak dipakai (mengikuti aturan
v44 yang melarang em-dash).

Beberapa contoh dipendekkan untuk efisiensi token, tetapi
TEMPLATE dan ATURAN dipertahankan 100% verbatim dari modelfile.
