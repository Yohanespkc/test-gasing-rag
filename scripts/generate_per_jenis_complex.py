#!/usr/bin/env python3
"""
Generator chunks per-jenis E dan F (bagian kompleks) untuk
AI Tutor GASING v44.

Jenis E dibagi 3 sub-chunk berdasarkan tingkat carry.
Jenis F dibagi 6 sub-chunk karena volume contoh paling besar.

Output: chunks/per_jenis/J81_*.md sampai J96_*.md
"""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "chunks" / "per_jenis"
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# J81: Jenis E tanpa carry (E-1, E-2)
# ============================================================================
J81 = """---
id: J81_e_tanpa_carry
kategori: per_jenis
jenis_soal: E
sub_kategori: tanpa_carry
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 3
ada_operand_3_digit: true
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S03_format_mencongak_universal
  - S04_format_dua_cara
kompleksitas: tinggi
punya_carry: false
punya_cascade_1_kecil: false
version_modelfile: v44
referensi_bagian_v44: "5.8 (sub: tanpa carry)"
---

# JENIS E TANPA CARRY: 3 digit tanpa carry

## Klasifikasi
Sub-jenis E ini berlaku jika ada operand 3 digit DAN tidak ada carry
(semua jumlah nilai tempat kurang dari 10).
Contoh: 106+283, 105+182, 234+352.

## Strategi
Dekomposisi nilai tempat 3-level. Hitung dari RATUSAN ke bawah.
Tanpa carry artinya cara singkat tidak butuh notasi 1 kecil.

## Aturan Penting
- JANGAN pakai pola Jenis D. Pakai 3-level (Ratusan, Puluhan, Satuan).
- Mode belajar: WAJIB pakai label "Ratusan:", "Puluhan:", "Satuan:"
  (format vertikal eksplisit).
- TIDAK ADA komutativitas di akhir Jenis E (komutativitas hanya untuk
  operand maks 2 digit).
- Cara singkat di sub-jenis tanpa carry: TULIS LANGSUNG hasilnya
  (tidak perlu notasi 1 kecil).
- Operand 2 digit di soal Jenis E: 0 ratusan (misal 46 = 0 ratusan,
  4 puluhan, 6 satuan).

## Contoh Belajar 106 + 283
Berapa 106 + 283?
106 terdiri dari 1 ratusan, 0 puluhan, dan 6 satuan
283 terdiri dari 2 ratusan, 8 puluhan, dan 3 satuan
Jumlahkan sesuai dengan nilai tempatnya
Ratusan: 1 ratusan + 2 ratusan = 3 ratusan
Puluhan: 0 puluhan + 8 puluhan = 8 puluhan
Satuan: 6 satuan + 3 satuan = 9 satuan
106 + 283 = 389

Cara singkat:
106 + 283 = 389

## Contoh Mencongak 106 + 283
Berapa 106 + 283?
Jawab: 106 + 283 = 389
Alasan: Dikerjakan dari depan (mulai dari ratusan)
ratusan 1 + 2 = 3
lirik kanan, jumlah puluhan kurang dari 10, ratusan tetap sama.
Jadi ratusannya 3
Puluhan 0 + 8 = 8
lirik kanan, jumlah satuan kurang dari 10, puluhan tetap sama
jadi puluhannya 8
Satuan 6 + 3 = 9
Jadi 106 + 283 = 389

Cara singkat: 106 + 283 = 389
"""


# ============================================================================
# J82: Jenis E carry satuan atau puluhan (E-3 sampai E-6)
# ============================================================================
J82 = """---
id: J82_e_carry_satuan_puluhan
kategori: per_jenis
jenis_soal: E
sub_kategori: carry_satuan_atau_puluhan
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 3
ada_operand_3_digit: true
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S03_format_mencongak_universal
  - S04_format_dua_cara
  - S05_aturan_1_kecil
kompleksitas: tinggi
punya_carry: true
punya_cascade_1_kecil: false
version_modelfile: v44
referensi_bagian_v44: "5.8 (sub: carry satuan/puluhan)"
---

# JENIS E DENGAN CARRY: carry di satuan atau puluhan (tanpa kaskade penuh)

## Klasifikasi
Sub-jenis E ini berlaku jika ada operand 3 digit DAN ada carry
(satuan dan/atau puluhan menghasilkan lebih dari atau sama dengan 10),
TAPI tanpa kaskade penuh (puluhan tidak bernilai 9 saat satuan carry).
Contoh: 106+287, 156+287.

## Strategi
3-level dekomposisi. Cara singkat WAJIB pakai NOTASI 1 KECIL 1 baris
(BUKAN bracket).

## Aturan Cara Singkat
Pakai notasi 1 kecil ₁ untuk menandai nilai tempat yang carry.
Contoh: 106 + 287 = 38₁3 = 393
Contoh: 156 + 287 = 3₁3₁3 = 443

## Contoh Belajar 106 + 287 (carry satuan)
Berapa 106 + 287?
106 terdiri dari 1 ratusan, 0 puluhan, dan 6 satuan
287 terdiri dari 2 ratusan, 8 puluhan, dan 7 satuan
Jumlahkan sesuai dengan nilai tempatnya
Ratusan: 1 ratusan + 2 ratusan = 3 ratusan
Puluhan: 0 puluhan + 8 puluhan = 8 puluhan
Satuan: 6 satuan + 7 satuan = 13 satuan = 1 puluhan 3 satuan
Puluhan: 8 puluhan + 1 puluhan = 9 puluhan
Satuan: 3 satuan
106 + 287 = 393

Cara singkat:
106 + 287 = 38₁3 = 393

## Contoh Mencongak 106 + 287 (carry satuan)
Berapa 106 + 287?
Jawab: 106 + 287 = 393
Alasan: Dikerjakan dari depan (mulai dari ratusan)
ratusan 1 + 2 = 3
lirik kanan, jumlah puluhan kurang dari 10, ratusan tidak berubah
Jadi ratusannya 3
Puluhan 0 + 8 = 8
lirik kanan, jumlah satuan lebih dari atau sama dengan 10, puluhan
tambah 1, jadi puluhannya 8 + 1 = 9
Satuan 6 + 7 = 13, ambil 3 (1 nya sudah gabung dengan puluhan)
Jadi 106 + 287 = 393

Cara singkat: 106 + 287 = 38₁3 = 393

## Contoh Belajar 156 + 287 (carry ganda: puluhan dan satuan)
Berapa 156 + 287?
156 terdiri dari 1 ratusan, 5 puluhan, dan 6 satuan
287 terdiri dari 2 ratusan, 8 puluhan, dan 7 satuan
Jumlahkan sesuai dengan nilai tempatnya
Ratusan: 1 ratusan + 2 ratusan = 3 ratusan
Puluhan: 5 puluhan + 8 puluhan = 13 puluhan = 1 ratusan 3 puluhan
Satuan: 6 satuan + 7 satuan = 13 satuan = 1 puluhan 3 satuan
Ratusan: 3 ratusan + 1 ratusan = 4 ratusan
Puluhan: 3 puluhan + 1 puluhan = 4 puluhan
Satuan: 3 satuan
156 + 287 = 443

Cara singkat:
156 + 287 = 3₁3₁3 = 443

## Contoh Mencongak 156 + 287 (carry ganda)
Berapa 156 + 287?
Jawab: 156 + 287 = 443
Alasan: Dikerjakan dari depan (mulai dari ratusan)
ratusan 1 + 2 = 3
lirik kanan, jumlah puluhan lebih dari atau sama dengan 10, ratusan
tambah 1
Jadi ratusannya 3 + 1 = 4
Puluhan 5 + 8 = 13, ambil 3 (angka 1 didepan sudah bergabung dengan
ratusan)
lirik kanan, jumlah satuan lebih dari atau sama dengan 10, puluhan
tambah 1, jadi puluhannya 3 + 1 = 4
Satuan 6 + 7 = 13, ambil 3 (angka 1 didepan sudah bergabung dengan
puluhan)
Jadi 156 + 287 = 443

Cara singkat: 156 + 287 = 3₁3₁3 = 443
"""


# ============================================================================
# J83: Jenis E cascade 1 kecil (E-7 sampai E-12)
# ============================================================================
J83 = """---
id: J83_e_cascade_1_kecil
kategori: per_jenis
jenis_soal: E
sub_kategori: cascade_1_kecil
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 3
ada_operand_3_digit: true
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S03_format_mencongak_universal
  - S04_format_dua_cara
  - S05_aturan_1_kecil
kompleksitas: tinggi
punya_carry: true
punya_cascade_1_kecil: true
beda_panjang_digit: true
version_modelfile: v44
referensi_bagian_v44: "5.8 (sub: cascade dan diff digits)"
---

# JENIS E DENGAN KASKADE 1 KECIL: puluhan 9 cascade, atau operand beda digit

## Klasifikasi
Sub-jenis E ini berlaku untuk dua kasus:
1. Ada operand 3 digit DAN puluhan = 9 saat satuan carry (membutuhkan
   kaskade Aturan 1 Kecil).
2. Operand berbeda panjang digit (1d+3d, 2d+3d) dengan atau tanpa carry.
Contoh: 113+287, 6+283, 46+287, 6+297.

## Strategi
Pakai Aturan 1 Kecil dengan kaskade penuh untuk kasus puluhan = 9.
Untuk operand beda panjang, samakan dengan menambah 0 ratusan di depan
operand pendek.

## Aturan Operand Pendek
- Operand 1 digit: 0 ratusan, 0 puluhan, X satuan.
  Contoh: 6 = 0 ratusan, 0 puluhan, 6 satuan.
- Operand 2 digit: 0 ratusan, X puluhan, Y satuan.
  Contoh: 46 = 0 ratusan, 4 puluhan, 6 satuan.

## Contoh Mencongak 113 + 287 (kaskade puluhan)
Berapa 113 + 287?
Jawab: 113 + 287 = 400
Alasan: Dikerjakan dari depan (mulai dari ratusan)
ratusan 1 + 2 = 3
lirik kanan, jumlah puluhan 9, lirik kanan lagi satuannya 10. Ratusannya
bertambah 1, puluhannya juga bertambah 1.
Jadi ratusannya 3 + 1 = 4
Puluhannya 9 + 1 = 10 (ambil 0 karena 1 nya sudah ditambahkan ke ratusan)
Satuan 3 + 7 = 10, ambil 0 (karena 1 nya sudah ditambahkan ke puluhan)
Jadi 113 + 287 = 400

Cara singkat: 113 + 287 = 39₁0 = 400
(Aturan 1 kecil: ₁0 satuan, puluhan 9+1=10 ditulis 0, ratusan 3+1=4)

## Contoh Belajar 113 + 287 (kaskade puluhan)
Berapa 113 + 287?
113 terdiri dari 1 ratusan, 1 puluhan, dan 3 satuan
287 terdiri dari 2 ratusan, 8 puluhan, dan 7 satuan
Jumlahkan sesuai dengan nilai tempatnya
Ratusan: 1 ratusan + 2 ratusan = 3 ratusan
Puluhan: 1 puluhan + 8 puluhan = 9 puluhan
Satuan: 3 satuan + 7 satuan = 10 satuan = 1 puluhan 0 satuan
Puluhan: 9 puluhan + 1 puluhan = 10 puluhan = 1 ratusan 0 puluhan
Ratusan: 3 ratusan + 1 ratusan = 4 ratusan
Puluhan: 0 puluhan
Satuan: 0 satuan
113 + 287 = 400

Cara singkat: 113 + 287 = 39₁0 = 400

## Contoh Belajar 6 + 283 (1d+3d tanpa carry)
Berapa 6 + 283?
6 terdiri dari 6 satuan
283 terdiri dari 2 ratusan, 8 puluhan, dan 3 satuan
Jumlahkan sesuai dengan nilai tempatnya
Ratusan: 2 ratusan
Puluhan: 8 puluhan
Satuan: 6 satuan + 3 satuan = 9 satuan
6 + 283 = 289

Cara singkat:
6 + 283 = 289

## Contoh Mencongak 6 + 283 (1d+3d tanpa carry)
Berapa 6 + 283?
Jawab: 6 + 283 = 289
Alasan: Dikerjakan dari depan (mulai dari ratusan)
Ratusan 2, lirik kanan puluhan kurang dari 10, ratusan tetap 2
Puluhan 8, lirik kanan satuan kurang dari 10, puluhan tetap 8
Satuan 6 + 3 = 9
Jadi 6 + 283 = 289

Cara singkat: 6 + 283 = 289

## Contoh Belajar 46 + 287 (2d+3d carry ganda)
Berapa 46 + 287?
46 terdiri dari 4 puluhan dan 6 satuan
287 terdiri dari 2 ratusan, 8 puluhan, dan 7 satuan
Jumlahkan sesuai dengan nilai tempatnya
Ratusan: 2 ratusan
Puluhan: 4 puluhan + 8 puluhan = 12 puluhan = 1 ratusan 2 puluhan
Satuan: 6 satuan + 7 satuan = 13 satuan = 1 puluhan 3 satuan
Ratusan: 2 ratusan + 1 ratusan = 3 ratusan
Puluhan: 2 puluhan + 1 puluhan = 3 puluhan
Satuan: 3 satuan
46 + 287 = 333

Cara singkat:
46 + 287 = 2₁2₁3 = 333

## Contoh Mencongak 6 + 297 (1d+3d cascade Aturan 1 Kecil)
Berapa 6 + 297?
Jawab: 6 + 297 = 303
Alasan: Dikerjakan dari depan (mulai dari ratusan)
ratusan 2 lirik kanan, jumlah puluhannya 9, lirik kanan lagi satuannya
lebih dari atau sama dengan 10. Ratusannya tambah 1, puluhannya tambah 1.
Jadi ratusannya 2 + 1 = 3
Puluhan 9 + 1 = 10 (ambil 0, karena 1 nya sudah ditambahkan ke ratusan)
Satuan 6 + 7 = 13, ambil 3 (angka 1 didepan sudah bergabung dengan
puluhan)
Jadi 6 + 297 = 303

Cara singkat: 6 + 297 = 29₁3 = 303
(Aturan 1 kecil: ₁3 satuan, puluhan 9+1=10 ditulis 0, ratusan 2+1=3)
"""


# ============================================================================
# J91: Jenis F Pengantar dan Aturan
# ============================================================================
J91 = """---
id: J91_f_pengantar_aturan
kategori: per_jenis
jenis_soal: F
sub_kategori: pengantar
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 99
ada_operand_4_digit_atau_lebih: true
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S03_format_mencongak_universal
  - S04_format_dua_cara
  - S05_aturan_1_kecil
kompleksitas: sangat_tinggi
version_modelfile: v44
referensi_bagian_v44: "5.9 (pengantar dan aturan wajib)"
---

# JENIS F: PENGANTAR DAN ATURAN WAJIB

## Klasifikasi
Jenis F berlaku jika salah satu atau kedua operand berukuran 4 digit
atau lebih. Tidak ada batas atas digit. Bisa 4d+4d, 4d+5d, 6d+8d, dst.
Contoh: 4859+3148, 4259+3148, 234859+565148, 3264859+3763148,
898+3289, 8373+239889.

## Strategi
Hitung dari nilai tempat TERTINGGI ke bawah. Gunakan Aturan 1 Kecil
untuk menandai carry. TIDAK perlu komutativitas di akhir.
- Mode belajar: dua cara (lengkap + singkat).
- Mode mencongak: cukup satu cara dengan teknik lirik kanan.

## Aturan Wajib Jenis F Belajar (DILARANG DILANGGAR)
1. DILARANG KERAS pakai kata "simpan", "menyimpan", "simpanan",
   "carry". Pakai notasi ₁ (1 kecil).
2. DILARANG mulai dari satuan atau dari kanan. WAJIB mulai dari nilai
   tempat TERTINGGI (paling kiri).
3. WAJIB pakai notasi ₁ (subscript 1 kecil) untuk setiap hasil yang
   melebihi 9. Penulisan: ₁ SELALU diikuti TEPAT SATU DIGIT (digit
   satuan dari hasil). Misal 17 ditulis ₁7, 10 ditulis ₁0. Lihat
   chunk S05_aturan_1_kecil untuk detail lengkap.
4. Cara Lengkap: jumlahkan SETIAP nilai tempat dari KIRI ke KANAN,
   tulis hasilnya. Jika hasil >= 10, ambil HANYA digit satuan dan
   taruh ₁ di depannya. JANGAN tambahkan carry di langkah ini. Tulis
   jumlah mentah per digit dulu, lalu resolve ₁ setelahnya.
5. Resolve ₁ WAJIB dari DEPAN (kiri ke kanan): scan setiap digit dari
   kiri, jika digit berikutnya punya ₁, tambahkan 1 ke digit saat ini.
   JANGAN resolve dari belakang.
6. Cara Singkat: tulis langsung dengan notasi ₁, lalu resolve.

## Format Output Mode Belajar Jenis F
Jumlahkan angka dengan nilai tempat yang sama:
[Daftar nilai tempat dari tertinggi ke satuan, masing-masing per baris]
[Contoh:]
Ribuan: 4 + 3 = 7
Ratusan: 8 + 1 = 9
Puluhan: 5 + 4 = 9
Satuan: 9 + 8 = 17

[soal] = [hasil mentah dengan notasi 1 kecil]

[Resolve 1 kecil jika ada, dengan penjelasan]

Maka [soal] = [jawaban akhir].

Cara singkat: [soal] = [notasi 1 kecil] = [jawaban]

## Format Output Mode Mencongak Jenis F
Berapa [soal]?
Jawab: [soal] = [jawaban]
Alasan: jumlahkan dari depan sebagai berikut,
[Baris demi baris pakai teknik lirik kanan, lihat J96_f_mencongak]
Jadi: [soal] = [jawaban]

## Pengantar Naratif (Singkat)
Setelah menjumlahkan setiap nilai tempat dari depan, akan muncul angka
1 kecil pada nilai tempat yang hasilnya melebihi 9. Angka 1 kecil itu
kemudian dijumlahkan dengan angka di depannya. Jika angka di depannya
9, berlaku efek domino: 9 berubah menjadi 0, lalu 1 kecil pindah lagi
ke kiri sampai bertemu angka selain 9.
"""


# ============================================================================
# J92: Jenis F Alignment Digit
# ============================================================================
J92 = """---
id: J92_f_alignment_digit
kategori: per_jenis
jenis_soal: F
sub_kategori: alignment
topik: penjumlahan
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S05_aturan_1_kecil
kompleksitas: sangat_tinggi
beda_panjang_digit: true
version_modelfile: v44
referensi_bagian_v44: "5.9 (aturan alignment digit)"
---

# JENIS F: ATURAN ALIGNMENT DIGIT

## Kapan Berlaku
Aturan alignment ini WAJIB diterapkan jika kedua operand BERBEDA
panjang digit, di mana setidaknya satu operand berukuran 4 digit atau
lebih. Misalnya: 898+3289, 8373+239889, 837382+82839767.

## Langkah Alignment (WAJIB sebelum menjumlahkan)
1. Tambahkan angka 0 di depan operand yang lebih pendek sampai kedua
   operand SAMA PANJANG.
2. Pasangkan digit berdasarkan NILAI TEMPAT (satuan dengan satuan,
   puluhan dengan puluhan, dst).
3. JANGAN pasangkan digit dari kiri begitu saja. Pasangkan dari KANAN
   (berdasarkan posisi nilai tempat).

## Contoh Alignment
### Soal: 898 + 3289
898 (3 digit) menjadi 0898 (4 digit) supaya selevel dengan 3289.
Pasangkan: 0+3 di ribuan, 8+2 di ratusan, 9+8 di puluhan, 8+9 di
satuan.

### Soal: 8373 + 239889
8373 (4 digit) menjadi 008373 (6 digit) supaya selevel dengan 239889.
Pasangkan dari nilai tempat tertinggi:
Ratus ribuan: 0+2, Puluh ribuan: 0+3, Ribuan: 8+9, Ratusan: 3+8,
Puluhan: 7+8, Satuan: 3+9.

### Soal: 837382 + 82839767
837382 (6 digit) menjadi 00837382 (8 digit) supaya selevel.
Pasangkan dari nilai tempat tertinggi:
Puluh jutaan: 0+8, Jutaan: 0+2, Ratus ribuan: 8+8, Puluh ribuan: 3+3,
Ribuan: 7+9, Ratusan: 3+7, Puluhan: 8+6, Satuan: 2+7.

## Catatan Penting
Setelah alignment, proses penjumlahan menggunakan teknik standar
Jenis F. Cara singkat di mode belajar bisa menampilkan kedua bentuk:
operand asli dan operand setelah alignment.

Contoh format cara singkat dengan alignment:
898 + 3289 = 0898 + 3289 = 3₁0₁7₁7 = 4187
8373 + 239889 = 008373 + 239889 = 23₁7₁1₁5₁2 = 248262

## Kesalahan Yang Harus Dihindari
- JANGAN langsung jumlahkan tanpa alignment. Hasil akan salah karena
  digit terpasang ke nilai tempat yang salah.
- JANGAN pasangkan dari kiri. Misal 898 + 3289 BUKAN jadi 8+3, 9+2,
  8+8, dst. Itu salah karena 8 dari 898 ada di ratusan, sedangkan 3
  dari 3289 ada di ribuan.
"""


# ============================================================================
# J93: Jenis F Belajar Simple (F-1, F-2, F-3)
# ============================================================================
J93 = """---
id: J93_f_belajar_simple
kategori: per_jenis
jenis_soal: F
sub_kategori: belajar_simple
topik: penjumlahan
mode_tercakup:
  - belajar
konsep_terkait:
  - S04_format_dua_cara
  - S05_aturan_1_kecil
kompleksitas: tinggi
punya_carry: true
punya_cascade_1_kecil: true
version_modelfile: v44
referensi_bagian_v44: "5.9 contoh F-1 s.d. F-3"
---

# JENIS F BELAJAR (SIMPLE): 4-6 digit dengan kaskade satu grup

## Cakupan
Contoh Jenis F mode belajar dengan kaskade SATU grup (satu ₁ inline
yang resolve ke kiri). Tidak ada beberapa kelompok 1 kecil terpisah.

## Contoh F-1: 4859 + 3148
Jumlahkan angka dengan nilai tempat yang sama:
Ribuan: 4 + 3 = 7
Ratusan: 8 + 1 = 9
Puluhan: 5 + 4 = 9
Satuan: 9 + 8 = 17
4859 + 3148 = 799₁7
Karena 799₁ = 799 + 1 = 800
Maka 4859 + 3148 = 8007.

Cara singkat: 4859 + 3148 = 799₁7 = 8007

## Contoh F-2: 4259 + 3148
Jumlahkan angka dengan nilai tempat yang sama:
Ribuan: 4 + 3 = 7
Ratusan: 2 + 1 = 3
Puluhan: 5 + 4 = 9
Satuan: 9 + 8 = 17
4259 + 3148 = 739₁7
Karena 39₁ = 39 + 1 = 40
Maka 4259 + 3148 = 7407.

Cara singkat: 4259 + 3148 = 739₁7 = 7407

## Contoh F-3: 234859 + 563148
Jumlahkan angka dengan nilai tempat yang sama:
Ratus ribuan: 2 + 5 = 7
Puluh ribuan: 3 + 6 = 9
Ribuan: 4 + 3 = 7
Ratusan: 8 + 1 = 9
Puluhan: 5 + 4 = 9
Satuan: 9 + 8 = 17
234859 + 563148 = 79799₁7
Karena 799₁ = 799 + 1 = 800
Maka 234859 + 563148 = 798007.

Cara singkat: 234859 + 563148 = 79799₁7 = 798007

## Pola Yang Bisa Dilihat
Ketiga contoh ini menunjukkan satu ₁ inline yang resolve melalui
deretan 9 di kiri (kalau ada). Pola:
- F-1: 9 di ratusan dan puluhan, ₁ resolve melalui keduanya jadi 800.
- F-2: hanya 9 di puluhan, ₁ resolve melalui satu 9 saja jadi 40.
- F-3: 9 di ratusan dan puluhan (tidak menjalar ke puluh ribuan
  karena 7 di ribuan menahan kaskade).

## Catatan
TIDAK ada komutativitas di akhir untuk Jenis F. Setelah hasil akhir,
respons berakhir di "Maka [soal] = [jawaban]." plus "Cara singkat:
[notasi 1 kecil] = [jawaban]".
"""


# ============================================================================
# J94: Jenis F Belajar Cascade kompleks (F-4 s.d. F-8)
# ============================================================================
J94 = """---
id: J94_f_belajar_cascade
kategori: per_jenis
jenis_soal: F
sub_kategori: belajar_cascade_kompleks
topik: penjumlahan
mode_tercakup:
  - belajar
konsep_terkait:
  - S05_aturan_1_kecil
kompleksitas: sangat_tinggi
punya_carry: true
punya_cascade_1_kecil: true
beberapa_kelompok_1_kecil: true
version_modelfile: v44
referensi_bagian_v44: "5.9 contoh F-4 s.d. F-8"
---

# JENIS F BELAJAR (CASCADE KOMPLEKS): kaskade panjang dan beberapa kelompok 1 kecil

## Cakupan
Contoh Jenis F mode belajar dengan:
1. Kaskade panjang yang menjalar melalui banyak 9 (sampai memunculkan
   digit baru di paling kiri).
2. Beberapa kelompok ₁ terpisah dalam satu hasil.
3. Kaskade dengan dua ₁ yang berinteraksi (domino).

## Contoh F-4: 234859 + 565148 (kaskade penuh ke 6 digit jadi 7 digit)
Jumlahkan angka dengan nilai tempat yang sama:
Ratus ribuan: 2 + 5 = 7
Puluh ribuan: 3 + 6 = 9
Ribuan: 4 + 5 = 9
Ratusan: 8 + 1 = 9
Puluhan: 5 + 4 = 9
Satuan: 9 + 8 = 17
234859 + 565148 = 79999₁7
Karena 79999₁ = 79999 + 1 = 80000 (efek domino menjalar ke seluruh
deretan 9)
Maka 234859 + 565148 = 800007.

Cara singkat: 234859 + 565148 = 79999₁7 = 800007

## Contoh F-5: 3264859 + 3763148 (dua kelompok ₁)
Jumlahkan angka dengan nilai tempat yang sama:
Jutaan: 3 + 3 = 6
Ratus ribuan: 2 + 7 = 9
Puluh ribuan: 6 + 6 = 12
Ribuan: 4 + 3 = 7
Ratusan: 8 + 1 = 9
Puluhan: 5 + 4 = 9
Satuan: 9 + 8 = 17
3264859 + 3763148 = 69₁2799₁7
Soal ini muncul dua angka 1 kecil pada tempat yang berbeda, jadi kita
kerjakan masing-masing:
Karena 69₁ = 69 + 1 = 70
Karena 799₁ = 799 + 1 = 800
Maka 3264859 + 3763148 = 7028007.

Cara singkat: 3264859 + 3763148 = 69₁2799₁7 = 7028007

## Contoh F-6: 83938 + 16067 (kaskade penuh dari 5 digit ke 6 digit)
Jumlahkan angka dengan nilai tempat yang sama:
Puluh ribuan: 8 + 1 = 9
Ribuan: 3 + 6 = 9
Ratusan: 9 + 0 = 9
Puluhan: 3 + 6 = 9
Satuan: 8 + 7 = 15
83938 + 16067 = 9999₁5
Karena 9999₁ = 9999 + 1 = 10000 (efek domino menjalar ke seluruh
deretan 9, sehingga jumlahnya menjadi enam digit)
Maka 83938 + 16067 = 100005.

Cara singkat: 83938 + 16067 = 9999₁5 = 100005

## Contoh F-7: 3473 + 3529 (kaskade pendek)
Jumlahkan angka dengan nilai tempat yang sama:
Ribuan: 3 + 3 = 6
Ratusan: 4 + 5 = 9
Puluhan: 7 + 2 = 9
Satuan: 3 + 9 = 12
3473 + 3529 = 699₁2
Karena 699₁ = 699 + 1 = 700
Maka 3473 + 3529 = 7002.

Cara singkat: 3473 + 3529 = 699₁2 = 7002

## Contoh F-8: 4778 + 5287 (dua ₁ berinteraksi domino)
Jumlahkan angka dengan nilai tempat yang sama:
Ribuan: 4 + 5 = 9
Ratusan: 7 + 2 = 9
Puluhan: 7 + 8 = 15
Satuan: 8 + 7 = 15
4778 + 5287 = 99₁5₁5
Ada dua angka 1 kecil yang berinteraksi. Efek domino merambat ke depan:
Satuan menghasilkan ₁5, tambahkan 1 ke puluhan: 5 + 1 = 6, menjadi
99₁65.
Karena 99₁ = 99 + 1 = 100 (efek domino, sehingga jumlahnya menjadi
lima digit)
Maka 4778 + 5287 = 10065.

Cara singkat: 4778 + 5287 = 99₁5₁5 = 10065

## Pola Yang Bisa Dilihat
- F-4 dan F-6: kaskade menjalar penuh, menambah digit baru di paling
  kiri (semua 9 jadi 0, atau ada deretan 9 yang habis).
- F-5: dua kelompok ₁ terpisah, masing-masing diselesaikan independen.
- F-8: dua ₁ yang berdekatan, satu ₁ memicu ₁ lain (domino dalam
  domino).

## Catatan Penting
Saat ada beberapa kelompok ₁, JANGAN coba selesaikan semuanya bersamaan.
Selesaikan kelompok pertama, lalu kelompok kedua, lalu gabungkan
hasilnya sesuai urutan posisi.
"""


# ============================================================================
# J95: Jenis F Belajar Beda Panjang Digit (F-9, F-10, F-11, F-12)
# ============================================================================
J95 = """---
id: J95_f_belajar_diff_digits
kategori: per_jenis
jenis_soal: F
sub_kategori: belajar_diff_digits
topik: penjumlahan
mode_tercakup:
  - belajar
konsep_terkait:
  - J92_f_alignment_digit
  - S05_aturan_1_kecil
kompleksitas: sangat_tinggi
punya_carry: true
punya_cascade_1_kecil: true
beda_panjang_digit: true
banyak_1_kecil: true
version_modelfile: v44
referensi_bagian_v44: "5.9 contoh F-9 s.d. F-12"
---

# JENIS F BELAJAR (BEDA PANJANG DIGIT): operand beda panjang + banyak 1 kecil

## Cakupan
Contoh Jenis F mode belajar di mana operand BERBEDA panjang digit DAN
sering muncul banyak angka 1 kecil yang harus di-resolve dari depan.

## Strategi Khusus
1. Samakan jumlah digit dulu (tambah 0 di depan operand pendek). Lihat
   chunk J92_f_alignment_digit untuk detail.
2. Jumlahkan setiap nilai tempat, tulis hasil mentah dengan notasi ₁.
3. Resolve ₁ dari DEPAN (kiri ke kanan), bukan dari belakang.

## Contoh F-9: 898 + 3289 (banyak ₁)
Langkah pertama: samakan jumlah digit. 898 menjadi 0898.

Jumlahkan angka dengan nilai tempat yang sama:
Ribuan: 0 + 3 = 3
Ratusan: 8 + 2 = 10
Puluhan: 9 + 8 = 17
Satuan: 8 + 9 = 17
898 + 3289 = 3₁0₁7₁7

PENTING: ambil HANYA DIGIT SATUAN dari setiap hasil penjumlahan dan
taruh ₁ di depannya. Contoh: 10 → ₁0, 17 → ₁7.

Kita kerjakan angka 1 kecil dari depan (kiri ke kanan):
Ribuan: 3, tapi di kanannya ada ₁0, jadi kita tambahkan 1 ke ribuan:
3 + 1 = 4.
Ratusan: 0 (dari ₁0, angka yang ditulis 0), tapi di kanannya ada ₁7,
jadi kita tambahkan 1 ke ratusan: 0 + 1 = 1.
Puluhan: 7 (dari ₁7, angka yang ditulis 7), tapi di kanannya ada ₁7,
jadi kita tambahkan 1 ke puluhan: 7 + 1 = 8.
Satuan: 7 (dari ₁7, angka yang ditulis 7), tetap.
Maka 898 + 3289 = 4187.

Cara singkat: 898 + 3289 = 0898 + 3289 = 3₁0₁7₁7 = 4187

## Contoh F-10: 8373 + 239889 (operand beda panjang 4d vs 6d)
Langkah pertama: samakan jumlah digit. 8373 menjadi 008373.

Jumlahkan angka dengan nilai tempat yang sama:
Ratus ribuan: 0 + 2 = 2
Puluh ribuan: 0 + 3 = 3
Ribuan: 8 + 9 = 17
Ratusan: 3 + 8 = 11
Puluhan: 7 + 8 = 15
Satuan: 3 + 9 = 12
8373 + 239889 = 23₁7₁1₁5₁2

Kita kerjakan angka 1 kecil dari depan (kiri ke kanan):
Ratus ribuan: 2, tetap.
Puluh ribuan: 3, tapi di kanannya ada ₁7, tambah 1: 3 + 1 = 4.
Ribuan: 7 (dari ₁7), tapi di kanannya ada ₁1, tambah 1: 7 + 1 = 8.
Ratusan: 1 (dari ₁1), tapi di kanannya ada ₁5, tambah 1: 1 + 1 = 2.
Puluhan: 5 (dari ₁5), tapi di kanannya ada ₁2, tambah 1: 5 + 1 = 6.
Satuan: 2 (dari ₁2), tetap.
Maka 8373 + 239889 = 248262.

Cara singkat: 8373 + 239889 = 008373 + 239889 = 23₁7₁1₁5₁2 = 248262

## Contoh F-11: 111111 + 888889 (hasil satuan tepat 10, efek domino penuh)
Jumlahkan angka dengan nilai tempat yang sama:
Ratus ribuan: 1 + 8 = 9
Puluh ribuan: 1 + 8 = 9
Ribuan: 1 + 8 = 9
Ratusan: 1 + 8 = 9
Puluhan: 1 + 8 = 9
Satuan: 1 + 9 = 10
111111 + 888889 = 99999₁0

PERHATIKAN: Satuan 1 + 9 = 10 ditulis ₁0, ambil hanya digit satuan
dari hasil yaitu 0.

Kita kerjakan angka 1 kecil dari depan (kiri ke kanan):
Ratus ribuan: 9, tetap.
Puluh ribuan: 9, tetap.
Ribuan: 9, tetap.
Ratusan: 9, tetap.
Puluhan: 9, tapi di kanannya ada ₁0. Karena 9 + 1 = 10, maka 9 berubah
jadi 0, dan ₁ pindah satu nilai tempat ke kiri.
Ratusan: 9, tapi di kanannya ada ₁ (dari langkah sebelumnya). 9 + 1 =
10, 9 jadi 0, ₁ pindah ke kiri.
[Lanjut sampai semua 9 jadi 0.]
Karena tidak ada angka di kiri 1 kecil, maka muncul angka 1 di paling
kiri.
Maka 111111 + 888889 = 1000000.

Cara singkat: 111111 + 888889 = 99999₁0 = 1000000

## Contoh F-12: 837382 + 82839767 (operand beda panjang 6d vs 8d)
Langkah pertama: samakan jumlah digit. 837382 menjadi 00837382.

Jumlahkan angka dengan nilai tempat yang sama:
Puluh jutaan: 0 + 8 = 8
Jutaan: 0 + 2 = 2
Ratus ribuan: 8 + 8 = 16
Puluh ribuan: 3 + 3 = 6
Ribuan: 7 + 9 = 16
Ratusan: 3 + 7 = 10
Puluhan: 8 + 6 = 14
Satuan: 2 + 7 = 9

837382 + 82839767 = 82₁66₁6₁0₁49

Kita kerjakan angka 1 kecil dari depan (kiri ke kanan):
Puluh jutaan: 8, tetap.
Jutaan: 2, tapi di kanannya ada ₁6, tambah 1 ke jutaan: 2 + 1 = 3.
Ratus ribuan: 6, tetap (dari ₁6, angka yang ditulis 6).
Puluh ribuan: 6, tapi di kanannya ada ₁6, tambah 1: 6 + 1 = 7.
Ribuan: 6 (dari ₁6). Di kanannya ada ₁0, tambah 1: 6 + 1 = 7.
Ratusan: 0 (dari ₁0). Di kanannya ada ₁4, tambah 1: 0 + 1 = 1.
Puluhan: 4 (dari ₁4), tetap.
Satuan: 9, tetap.
Maka 837382 + 82839767 = 83677149.

Cara singkat: 837382 + 82839767 = 82₁66₁6₁0₁49 = 83677149

## Catatan Penting
Resolve ₁ dari KIRI ke KANAN, scan setiap digit. Jika digit
berikutnya punya ₁, tambah 1 ke digit saat ini. JANGAN resolve dari
belakang karena akan menghasilkan urutan operasi yang salah.
"""


# ============================================================================
# J96: Jenis F Mencongak (F-13 s.d. F-23) plus aturan lirik kanan
# ============================================================================
J96 = """---
id: J96_f_mencongak
kategori: per_jenis
jenis_soal: F
sub_kategori: mencongak
topik: penjumlahan
mode_tercakup:
  - mencongak
konsep_terkait:
  - S03_format_mencongak_universal
  - S05_aturan_1_kecil
  - J92_f_alignment_digit
kompleksitas: sangat_tinggi
punya_carry: true
punya_cascade_1_kecil: true
version_modelfile: v44
referensi_bagian_v44: "5.9 contoh F-13 s.d. F-23"
---

# JENIS F MENCONGAK: teknik lirik kanan untuk operand 4+ digit

## Cakupan
Mode mencongak untuk Jenis F (4+ digit), pakai TEKNIK LIRIK KANAN.
Tidak perlu dua cara, cukup satu cara langsung dengan jawaban di awal.

## Aturan Lirik Kanan Mencongak (WAJIB DIIKUTI)
PRINSIP DASAR: setiap posisi yang sum-nya kamu hitung SENDIRI (belum
disentuh kaskade dari posisi atasnya) WAJIB lirik kanan ke posisi
berikutnya, tidak peduli apakah sum < 10 atau >= 10.

Lirik kanan artinya melihat jumlah digit di posisi BERIKUTNYA (satu
posisi ke kanan).

### Aturan Lirik Kanan
1. Kalau jumlah di kanan = 9: LANJUT lirik kanan lagi ke posisi
   berikutnya (cari apakah ada >= 10 di ujung rantai 9).
2. Kalau jumlah di kanan >= 10 (bukan 9): digit saat ini NAIK 1.
   Kalau sum saat ini >= 10, ambil digit satuannya dulu (misal 16 ->
   ambil 6), lalu naik 1 (6+1=7). BUKAN 16+1=17. Tulis hasilnya.
3. Kalau jumlah di kanan < 9 (dan bukan 9): BERHENTI. Tulis digit
   satuan dari sum saat ini.
4. Kalau deretan 9 berakhir dengan >= 10: digit SEBELUM deretan 9
   naik 1, semua 9 jadi 0.
5. Kalau deretan 9 berakhir TANPA >= 10: semua tetap, tulis 9 sebagai 9.

### Pengecualian Penting
Kalau sebuah posisi sudah DIKUNCI nilainya oleh kaskade Aturan 1 kecil
dari posisi di atasnya (kiri), TULIS LANGSUNG nilai yang sudah
ditentukan tanpa lirik kanan ulang. Posisi yang sum-nya kamu hitung
sendiri saja yang lirik kanan.

### Larangan
DILARANG lirik kanan berulang kalau digit berikutnya BUKAN 9. Langsung
berhenti.
DILARANG menulis digit TANPA lirik kanan dulu (kecuali satuan yang
merupakan posisi terakhir, atau posisi yang sudah dikunci kaskade).

## Format Output Mencongak F
Berapa [soal]?
Jawab: [soal] = [jawaban]
Alasan: jumlahkan dari depan sebagai berikut,
[soal] =
[Nilai tempat tertinggi]: [sum], [lirik kanan ...]. Tulis [X].
[Nilai tempat berikutnya]: [sum atau dikunci]. Tulis [X].
...
Satuan: [sum]. Tulis [X].
Jadi: [soal] = [jawaban]
[Catatan opsional: hasil di atas berasal dari [notasi 1 kecil] (lihat
pada contoh Belajar)]

## Contoh F-13: 4859 + 3148
Berapa 4859 + 3148?
Jawab: 4859 + 3148 = 8007
Alasan: jumlahkan dari depan sebagai berikut,
4859 + 3148 =
Ribuan 4 + 3 = 7, lirik kanan ratusan 9, lirik kanan lagi puluhan 9,
lirik kanan lagi satuan lebih dari atau sama dengan 10. Tulis 8.
Ratusan: Tulis 0.
Puluhan: Tulis 0.
Satuan: 9 + 8 = 17. Tulis 7.
Jadi: 4859 + 3148 = 8007
Catatan: hasil di atas berasal dari 799₁ = 800 (lihat pada contoh Belajar)

## Contoh F-14: 83938 + 16067 (kaskade penuh)
Berapa 83938 + 16067?
Jawab: 83938 + 16067 = 100005
Alasan: jumlahkan dari depan sebagai berikut,
83938 + 16067 =
Puluh ribuan 8 + 1 = 9, lirik kanan ribuan 9, lirik kanan lagi ratusan
9, lirik kanan lagi puluhan 9, lirik kanan lagi satuan lebih dari atau
sama dengan 10. Tulis 10.
Ribuan: Tulis 0.
Ratusan: Tulis 0.
Puluhan: Tulis 0.
Satuan: 8 + 7 = 15. Tulis 5.
Jadi: 83938 + 16067 = 100005
Catatan: hasil di atas berasal dari 9999₁ = 10000 (lihat pada contoh
Belajar)

## Contoh F-15: 3473 + 3529 (kaskade pendek)
Berapa 3473 + 3529?
Jawab: 3473 + 3529 = 7002
Alasan: jumlahkan dari depan sebagai berikut,
3473 + 3529 =
Ribuan 3 + 3 = 6, lirik kanan ratusan 9, lirik kanan lagi puluhan 9,
lirik kanan lagi satuan lebih dari atau sama dengan 10. Tulis 7.
Ratusan: Tulis 0.
Puluhan: Tulis 0.
Satuan: 3 + 9 = 12. Tulis 2.
Jadi: 3473 + 3529 = 7002
Catatan: hasil di atas berasal dari 699₁ = 700 (lihat pada contoh Belajar)

## Contoh F-16: 4259 + 3148 (berhenti karena bukan 9)
Berapa 4259 + 3148?
Jawab: 4259 + 3148 = 7407
Alasan: jumlahkan dari depan sebagai berikut,
4259 + 3148 =
Ribuan 4 + 3 = 7, lirik kanan ratusan 3 (bukan 9, berhenti). Tulis 7.
Ratusan 2 + 1 = 3, lirik kanan puluhan 9, lirik kanan lagi satuan
lebih dari atau sama dengan 10. Tulis 4.
Puluhan: Tulis 0.
Satuan: 9 + 8 = 17. Tulis 7.
Jadi: 4259 + 3148 = 7407
Catatan: hasil di atas berasal dari 39₁ = 40 (lihat pada contoh Belajar)

## Contoh F-17: 234259 + 563148
Berapa 234259 + 563148?
Jawab: 234259 + 563148 = 797407
Alasan: jumlahkan dari depan sebagai berikut,
234259 + 563148 =
Ratus ribuan 2 + 5 = 7, lirik kanan puluh ribuan 9, lirik kanan lagi
ribuan 7 (bukan 9, berhenti). Tulis 7.
Puluh ribuan 3 + 6 = 9, lirik kanan ribuan 7 (bukan 9, berhenti).
Tulis 9.
Ribuan 4 + 3 = 7, lirik kanan ratusan 3 (bukan 9, berhenti). Tulis 7.
Ratusan 2 + 1 = 3, lirik kanan puluhan 9, lirik kanan lagi satuan
lebih dari atau sama dengan 10. Tulis 4.
Puluhan: Tulis 0.
Satuan: 9 + 8 = 17. Tulis 7.
Jadi: 234259 + 563148 = 797407

## Contoh F-18: 234859 + 565148 (kaskade penuh)
Berapa 234859 + 565148?
Jawab: 234859 + 565148 = 800007
Alasan: jumlahkan dari depan sebagai berikut,
234859 + 565148 =
Ratus ribuan 2 + 5 = 7, lirik kanan puluh ribuan 9, lirik kanan lagi
ribuan 9, lirik kanan lagi ratusan 9, lirik kanan lagi puluhan 9,
lirik kanan lagi satuan lebih dari atau sama dengan 10. Tulis 8.
Puluh ribuan: Tulis 0.
Ribuan: Tulis 0.
Ratusan: Tulis 0.
Puluhan: Tulis 0.
Satuan: 9 + 8 = 17. Tulis 7.
Jadi: 234859 + 565148 = 800007
Catatan: hasil di atas berasal dari 79999₁ = 80000 (lihat pada contoh
Belajar)

## Contoh F-19: 3264859 + 3763148 (dua kelompok ₁)
Berapa 3264859 + 3763148?
Jawab: 3264859 + 3763148 = 7028007
Alasan: jumlahkan dari depan sebagai berikut,
3264859 + 3763148 =
Jutaan 3 + 3 = 6, lirik kanan ratus ribuan 9, lirik kanan lagi puluh
ribuan lebih dari atau sama dengan 10. Tulis 7.
Ratus ribuan: Tulis 0.
Puluh ribuan: 6 + 6 = 12. Tulis 2.
Ribuan 4 + 3 = 7, lirik kanan ratusan 9, lirik kanan lagi puluhan 9,
lirik kanan lagi satuan lebih dari atau sama dengan 10. Tulis 8.
Ratusan: Tulis 0.
Puluhan: Tulis 0.
Satuan: 9 + 8 = 17. Tulis 7.
Jadi: 3264859 + 3763148 = 7028007

## Contoh F-20: 4778 + 5287 (dua ₁ berinteraksi)
Berapa 4778 + 5287?
Jawab: 4778 + 5287 = 10065
Alasan: jumlahkan dari depan sebagai berikut,
4778 + 5287 =
Ribuan 4 + 5 = 9, lirik kanan ratusan 9, lirik kanan lagi puluhan
lebih dari atau sama dengan 10. Tulis 10.
Ratusan: Tulis 0.
Puluhan: 7 + 8 = 15, lirik kanan satuan lebih dari atau sama dengan 10,
jadi puluhan naik 1 menjadi 16. Tulis 6.
Satuan: 8 + 7 = 15. Tulis 5.
Jadi: 4778 + 5287 = 10065

## Contoh F-21: 898 + 3289 (operand beda panjang, banyak ₁)
Langkah pertama: samakan jumlah digit. 898 menjadi 0898.

Berapa 898 + 3289?
Jawab: 898 + 3289 = 4187
Alasan: jumlahkan dari depan sebagai berikut,
0898 + 3289 =
Ribuan 0 + 3 = 3, lirik kanan ratusan 10 (lebih dari atau sama dengan
10), ribuan naik 1 jadi 4. Tulis 4.
Ratusan 8 + 2 = 10, ambil 0, lirik kanan puluhan 17 (>= 10), ratusan
naik 1 jadi 1. Tulis 1.
Puluhan 9 + 8 = 17, ambil 7, lirik kanan satuan 17 (>= 10), puluhan
naik 1 jadi 8. Tulis 8.
Satuan 8 + 9 = 17. Tulis 7.
Jadi: 898 + 3289 = 4187

## Contoh F-22: 8373 + 239889
Langkah pertama: samakan jumlah digit. 8373 menjadi 008373.

Berapa 8373 + 239889?
Jawab: 8373 + 239889 = 248262
Alasan: jumlahkan dari depan sebagai berikut,
008373 + 239889 =
Ratus ribuan 0 + 2 = 2, lirik kanan puluh ribuan 3 (bukan 9, berhenti).
Tulis 2.
Puluh ribuan 0 + 3 = 3, lirik kanan ribuan 17 (>= 10), puluh ribuan
naik 1 jadi 4. Tulis 4.
Ribuan 8 + 9 = 17, ambil 7, lirik kanan ratusan 11 (>= 10), ribuan
naik 1 jadi 8. Tulis 8.
Ratusan 3 + 8 = 11, ambil 1, lirik kanan puluhan 15 (>= 10), ratusan
naik 1 jadi 2. Tulis 2.
Puluhan 7 + 8 = 15, ambil 5, lirik kanan satuan 12 (>= 10), puluhan
naik 1 jadi 6. Tulis 6.
Satuan 3 + 9 = 12. Tulis 2.
Jadi: 8373 + 239889 = 248262

## Contoh F-23: 837382 + 82839767 (operand beda panjang 6d vs 8d)
Langkah pertama: samakan jumlah digit. 837382 menjadi 00837382.

Berapa 837382 + 82839767?
Jawab: 837382 + 82839767 = 83677149
Alasan: jumlahkan dari depan sebagai berikut,
00837382 + 82839767 =
Puluh jutaan 0 + 8 = 8, lirik kanan jutaan 2 (bukan 9, berhenti).
Tulis 8.
Jutaan 0 + 2 = 2, lirik kanan ratus ribuan 16 (>= 10), jutaan naik 1
jadi 3. Tulis 3.
Ratus ribuan 8 + 8 = 16, ambil 6, lirik kanan puluh ribuan 6 (bukan 9,
berhenti). Tulis 6.
Puluh ribuan 3 + 3 = 6, lirik kanan ribuan 16 (>= 10), puluh ribuan
naik 1 jadi 7. Tulis 7.
Ribuan 7 + 9 = 16, ambil 6, lirik kanan ratusan 10 (>= 10), ribuan
naik 1 jadi 7. Tulis 7.
Ratusan 3 + 7 = 10, ambil 0, lirik kanan puluhan 14 (>= 10), ratusan
naik 1 jadi 1. Tulis 1.
Puluhan 8 + 6 = 14, ambil 4, lirik kanan satuan 9 (bukan >= 10,
berhenti). Tulis 4.
Satuan 2 + 7 = 9. Tulis 9.
Jadi: 837382 + 82839767 = 83677149
"""


# ============================================================================
# Write all chunks to files
# ============================================================================
CHUNKS = {
    "J81_e_tanpa_carry.md": J81,
    "J82_e_carry_satuan_puluhan.md": J82,
    "J83_e_cascade_1_kecil.md": J83,
    "J91_f_pengantar_aturan.md": J91,
    "J92_f_alignment_digit.md": J92,
    "J93_f_belajar_simple.md": J93,
    "J94_f_belajar_cascade.md": J94,
    "J95_f_belajar_diff_digits.md": J95,
    "J96_f_mencongak.md": J96,
}


def main():
    for filename, content in CHUNKS.items():
        path = OUT_DIR / filename
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path} ({len(content)} chars)")
    print(f"\nTotal: {len(CHUNKS)} per-jenis chunks (E dan F) generated")


if __name__ == "__main__":
    main()
