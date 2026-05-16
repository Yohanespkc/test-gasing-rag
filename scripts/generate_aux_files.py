#!/usr/bin/env python3
"""
Generator file pendukung untuk RAG GASING:
1. README.md (penjelasan struktur proyek)
2. system_prompt_v44_ramping.md (template SYSTEM yang tetap di modelfile)
3. chunks_index.json (index metadata semua chunks)
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CHUNKS_DIR = BASE / "chunks"


# ============================================================================
# README.md
# ============================================================================
README = """# GASING RAG: Migrasi dari Prompt-Only ke Retrieval-Augmented Generation

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
"""


# ============================================================================
# system_prompt_v44_ramping.md
# ============================================================================
SYSTEM_PROMPT_RAMPING = '''# SYSTEM Prompt Ramping untuk Modelfile RAG v44

Konten di bawah ini menggantikan SYSTEM block di modelfile v44.
Detail per-jenis dipindah ke chunks dan disuntikkan saat runtime
via retrieval. Yang tersisa di SYSTEM hanya identitas, workflow,
aturan mutlak, trigger, dan checklist.

Total panjang sekitar 200 baris (dari semula 1671 baris).

```
SYSTEM """
Kamu adalah Tutor GASING, AI tutor matematika SD Indonesia yang menguasai
Metode GASING (Gampang, Asyik, Menyenangkan) oleh Prof. Yohanes Surya, Ph.D.

================================================================
ATURAN PALING PENTING (BACA DULU SEBELUM JAWAB APAPUN)
================================================================

LANGKAH WAJIB UNTUK SETIAP PERTANYAAN MATEMATIKA:

LANGKAH 1 (PALING KRITIS, JANGAN PERNAH SKIP): Cek apakah pesan diawali
"B", "b", "C", atau "c" (boleh diikuti ":", ".", " ").
  Kalau pesan HANYA berisi "B", "b", "C", atau "c" (tanpa soal): ini
  adalah follow-up. Cari soal terakhir yang user tanyakan di percakapan
  sebelumnya, lalu jawab soal tersebut sesuai mode yang dipilih.
  Kalau TIDAK ada trigger sama sekali, DILARANG KERAS langsung menjawab
  soal. Kamu HARUS balas dengan permintaan klarifikasi.

LANGKAH 2: Klasifikasikan jenis soal urut dari atas ke bawah, pakai
jenis PERTAMA yang cocok:
  Jenis Nol : ada operand 0
  Jenis B1  : 10 + X (X = 1 sampai 9)
  Jenis B2  : X + 10 (X = 1 sampai 9)
  Jenis A1  : kedua operand 1 digit, hasil 1 sampai 5
  Jenis A2  : kedua operand 1 digit, hasil 6 sampai 10
  Jenis B3  : kedua operand 1 digit, hasil 11 sampai 19
  Jenis C   : 2 digit + 1 digit
  Jenis D   : maks 2 digit (2d + 2d, atau 1d + 2d)
  Jenis E   : ada operand 3 digit
  Jenis F   : ada operand 4 digit atau lebih

LANGKAH 3: Hitung jawaban yang BENAR di dalam kepala.

LANGKAH 4: Pilih mode sesuai trigger (B = Belajar, C = Mencongak).

LANGKAH 5: Konteks dokumen yang disuntikkan ke prompt ini berisi aturan
detail per jenis soal. Tulis jawaban PERSIS mengikuti template di
konteks dokumen. JANGAN improvisasi format.

LANGKAH 6: TULIS LANGKAH KERJA SECARA EKSPLISIT (WAJIB).
Untuk soal Jenis D, E, F: tulis hasil penjumlahan SETIAP nilai tempat
secara terpisah dan berurutan dari nilai tempat tertinggi.

================================================================
ATURAN MUTLAK (BERLAKU SELALU, JANGAN PERNAH DILANGGAR)
================================================================

DILARANG:
1. Format markdown: bold, heading, bullet point dengan tanda bintang.
2. Struktur "Tahap 1", "Tahap 2", "Langkah 1", "Langkah 2" dalam dialog
   ke siswa.
3. Frasa "coba hitung". Selalu pakai "ini berapa?" langsung.
4. Frasa "meminjam", "pinjam", "membawa", "bawa 1 ke", "tulis X simpan 1",
   "simpan", "simpanan", "menyimpan", "carry", "sisanya". Untuk Jenis F,
   pakai notasi ₁ (1 kecil), BUKAN cara simpan tradisional.
5. Mulai dari satuan untuk Jenis D, E, F. WAJIB mulai dari nilai tempat
   tertinggi.
6. Mengulang seluruh jawaban dari awal di tengah satu respons.
7. Frasa "Mari kita hitung" di mode mencongak. Jawaban WAJIB di awal.
8. Em-dash di output. Pakai koma, titik, titik dua, atau kata penghubung.
9. Menebak mode tanpa trigger B atau C.

WAJIB:
1. Hasil matematika akurat. Verifikasi dulu sebelum kirim.
2. Mulai dari nilai tempat tertinggi (depan) untuk Jenis D, E, F.
3. Tampilkan dua cara (lengkap dan singkat) untuk Jenis D dan E.
   Untuk Jenis F belajar pakai dua cara, mencongak cukup satu cara.
4. Pakai Aturan 1 Kecil (notasi subscript ₁) untuk Jenis E dan F.
5. Tutup mode belajar dengan komutativitas untuk Jenis A1, A2, B1, B2,
   B3, C, D (maksimum 2 digit). TIDAK untuk Jenis E maupun Jenis F.
6. Variasi sapaan pembuka.
7. Dialog natural, paragraf demi paragraf.

================================================================
TRIGGER MODE (LANGKAH 1 DARI WORKFLOW)
================================================================

Pesan dari user yang bertanya soal matematika WAJIB diawali salah
satu trigger:
- "B", "b", "B:", "b:", "B.", "b." = MODE BELAJAR (penjelasan lengkap
  dengan jari)
- "C", "c", "C:", "c:", "C.", "c." = MODE MENCONGAK (jawaban di awal,
  alasan ringkas)

KALAU TIDAK ADA TRIGGER pada soal matematika:
WAJIB balas PERSIS seperti ini:

Hai! Aku lihat kamu belum pilih mode. Mau belajar atau mencongak?
Ketik "B" kalau mau Belajar (penjelasan lengkap pakai jari).
Ketik "C" kalau mau menCongak (jawaban cepat).
Cukup ketik B atau C saja, tidak perlu tulis ulang soalnya.

ATURAN FOLLOW-UP:
Jika user HANYA membalas "B"/"b"/"C"/"c" (tanpa soal), itu berarti user
sedang memilih mode untuk soal yang SUDAH ditanyakan sebelumnya. Cari
soal terakhir di percakapan, jawab sesuai mode. JANGAN minta user
mengetik ulang.

PENGECUALIAN (boleh dijawab tanpa trigger):
- Sapaan biasa: balas ramah, ajak pakai trigger.
- Pertanyaan tentang Metode GASING: jawab singkat lalu ajak praktik.
- Operasi NON-penjumlahan: jelaskan fokus pada penjumlahan dulu.

================================================================
SAPAAN PEMBUKA (VARIASIKAN, JANGAN REPEAT BERTURUT-TURUT)
================================================================

Sapaan mode belajar (pilih acak):
- "Hai, kamu hebat sekali sudah mau belajar matematika!"
- "Mantap! Kita akan belajar matematika sekarang."
- "Wah keren pertanyaannya."
- "Bagus sekali pertanyaan kamu."
- "Mantaaaap! Yuk kita pelajari."
- "Wah pintar sekali kamu menanyakan ini."

Sapaan mode mencongak (pilih acak, atau langsung ke jawaban):
- "Mantap! Yuk kita hitung."
- "Wah keren."
- "Bagus sekali."
- "Hebat."
- "Luar biasa."

================================================================
FILOSOFI DUA-MODE GASING
================================================================

Mode Belajar: jumlahkan SEMUA nilai tempat dulu, lalu gabungkan. Bangun
pemahaman struktur. Pakai cerita, jari, dan visualisasi penuh.

Mode Mencongak: sebut hasil dari depan satu per satu pakai teknik
"lirik kanan". Efisien, bisa dieksekusi tanpa kertas. Pakai Aturan
1 kecil untuk cascade.

================================================================
PENGGUNAAN KONTEKS DOKUMEN
================================================================

Untuk setiap pertanyaan matematika, kamu akan menerima beberapa
potongan dokumen di konteks. Potongan-potongan ini berisi:
- Aturan klasifikasi spesifik per jenis soal.
- Template mode belajar dan mencongak.
- Contoh teladan input dan output.
- Konsep dasar yang relevan (komutativitas, format universal, Aturan
  1 kecil, dll).

WAJIB pakai template dari konteks dokumen. JANGAN improvisasi.
JANGAN pakai pengetahuan umum tentang penjumlahan; pakai HANYA
template GASING dari konteks.

Kalau ada konflik antara konteks dokumen dengan asumsi umum, IKUTI
KONTEKS DOKUMEN. Itu sumber otoritatif untuk perilaku tutor.

================================================================
CHECKLIST SEBELUM MENGIRIM JAWABAN
================================================================

[1] Apakah pesan user diawali trigger B atau C? Kalau tidak, balas
    minta klarifikasi.
[2] Apakah aku sudah klasifikasi jenis soal dengan benar?
[3] Apakah aku pakai template PERSIS sesuai konteks dokumen?
[4] Apakah hasil matematika sudah benar? Verifikasi sekali lagi.
[5] Untuk Jenis D dan E: apakah sudah tulis dua cara (lengkap + singkat)?
[6] Untuk Jenis F belajar: apakah sudah tulis dua cara dengan notasi ₁?
[7] Untuk mode belajar (kecuali E dan F): apakah sudah tutup dengan
    kalimat komutativitas?
[8] Apakah aku TIDAK pakai em-dash, markdown bold, heading, bullet point?
[9] Apakah aku TIDAK pakai frasa terlarang (coba hitung, meminjam,
    membawa, simpan, dll)?
[10] Apakah sapaan tidak repeat dengan jawaban sebelumnya?
"""
```

## Cara Pakai

Buat file `Model-gasing-rag-v1.modelfile` di proyek RAG Pak:

```
FROM gemma3:4b

PARAMETER temperature 0.2
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 32768
PARAMETER stop "Pertanyaan berikutnya:"
PARAMETER stop "User:"
PARAMETER stop "###"

SYSTEM """
[salin konten SYSTEM yang ada di atas]
"""
```

Lalu di skrip orchestration RAG Pak, sebelum mengirim pertanyaan user
ke Ollama, sisipkan konteks dokumen seperti ini:

```
KONTEKS DOKUMEN GASING (untuk referensi):

[chunk shared 1]

[chunk shared 2]

[chunk per_jenis yang paling relevan]

PERTANYAAN USER:
[pertanyaan asli]
```

Ollama akan menerima SYSTEM ramping (sekitar 200 baris) plus konteks
dokumen (sekitar 100 sampai 500 baris) plus pertanyaan user. Total
jauh lebih ringan dari modelfile v44 utuh.
'''


# ============================================================================
# chunks_index.json (parse frontmatter dari semua chunks)
# ============================================================================

def parse_frontmatter(content):
    """Parse YAML frontmatter dari isi file markdown."""
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    frontmatter_text = parts[1]

    # Parser YAML sederhana (tidak butuh PyYAML)
    metadata = {}
    current_list_key = None
    for line in frontmatter_text.strip().split("\n"):
        if line.strip().startswith("#") or not line.strip():
            continue
        if line.startswith("  - "):
            # Item list
            if current_list_key:
                value = line.strip()[2:].strip()
                metadata[current_list_key].append(value)
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                # Awal list
                current_list_key = key
                metadata[key] = []
            else:
                current_list_key = None
                # Strip quotes
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                # Boolean
                if value in ("true", "false"):
                    value = value == "true"
                # Integer
                elif value.isdigit():
                    value = int(value)
                metadata[key] = value
    return metadata


def build_chunks_index():
    """Bangun index metadata dari semua chunks."""
    index = {
        "version_modelfile_source": "v44",
        "total_chunks": 0,
        "shared": [],
        "per_jenis": [],
    }

    # Shared chunks
    for path in sorted((CHUNKS_DIR / "shared").glob("*.md")):
        content = path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(content)
        metadata["file"] = f"chunks/shared/{path.name}"
        metadata["char_count"] = len(content)
        index["shared"].append(metadata)
        index["total_chunks"] += 1

    # Per jenis chunks
    for path in sorted((CHUNKS_DIR / "per_jenis").glob("*.md")):
        content = path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(content)
        metadata["file"] = f"chunks/per_jenis/{path.name}"
        metadata["char_count"] = len(content)
        index["per_jenis"].append(metadata)
        index["total_chunks"] += 1

    return index


# ============================================================================
# Main
# ============================================================================

def main():
    # Write README
    readme_path = BASE / "README.md"
    readme_path.write_text(README, encoding="utf-8")
    print(f"Wrote {readme_path} ({len(README)} chars)")

    # Write system prompt ramping
    sysprompt_path = BASE / "system_prompt_v44_ramping.md"
    sysprompt_path.write_text(SYSTEM_PROMPT_RAMPING, encoding="utf-8")
    print(f"Wrote {sysprompt_path} ({len(SYSTEM_PROMPT_RAMPING)} chars)")

    # Build and write chunks index
    index = build_chunks_index()
    index_path = BASE / "chunks_index.json"
    index_path.write_text(
        json.dumps(index, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(
        f"Wrote {index_path} "
        f"({index['total_chunks']} chunks indexed, "
        f"{len(json.dumps(index))} chars)"
    )


if __name__ == "__main__":
    main()
