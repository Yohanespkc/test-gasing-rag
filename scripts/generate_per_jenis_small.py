#!/usr/bin/env python3
"""
Generator chunks per-jenis (Nol, A1, A2, B1, B2, B3, C, D) untuk
AI Tutor GASING v44.

Output: chunks/per_jenis/J00_nol.md sampai J70_d.md
"""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "chunks" / "per_jenis"
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# J00: Jenis Nol (salah satu atau kedua operand 0)
# ============================================================================
J00 = """---
id: J00_nol
kategori: per_jenis
jenis_soal: Nol
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 4
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S03_format_mencongak_universal
kompleksitas: dasar
punya_carry: false
punya_cascade_1_kecil: false
version_modelfile: v44
referensi_bagian_v44: "5.0"
---

# JENIS NOL: ada operand 0

## Klasifikasi
Jenis Nol berlaku jika salah satu atau kedua operand adalah 0.
Contoh: 7+0, 52+0, 0+8, 100+0, 0+0, 3+0, 0+25.
Jenis ini diprioritaskan di atas semua jenis lain. Kalau ada 0,
selalu klasifikasikan sebagai Jenis Nol.

## Strategi
Prinsip: 0 artinya tidak ada jumlah. Sesuatu ditambah tidak ada
hasilnya tidak berubah.
JANGAN pakai cara cepat, pasangan 10, atau enumerasi pasangan.
Pakai analogi konkret (apel, kelereng, jeruk).

## Frasa Baku (Ikuti Urutan Operand Soal Asli)
- Pola X + 0: "[X] ditambah tidak ada ya tetap [X]"
- Pola 0 + Y: "tidak ada ditambah [Y] hasilnya [Y]"
- Pola 0 + 0: "tidak ada apel ditambah tidak ada apel hasilnya
  tentu tidak ada apel juga"

## Template Mode Mencongak (X+0 atau 0+Y)
[soal]?
Jawab: [soal] = [jawaban]
Alasan: 0 artinya tidak ada jumlah. Jadi [frasa sesuai pola].

## Template Mode Mencongak (0+0)
0 + 0?
Jawab 0.
Alasan 0 berarti tidak ada jumlah. Tidak ada apel ditambah tidak ada
apel hasilnya tentu tidak ada apel juga.

## Template Mode Belajar (X+0 atau 0+Y)
0 artinya tidak ada jumlah.
Sesuatu ditambah tidak ada hasilnya tidak berubah.
Jadi [soal] = [jawaban].
[Tambah analogi konkret kontekstual: jeruk, apel, atau kelereng.]

## Contoh Mencongak 7 + 0
7 + 0?
Jawab: 7 + 0 = 7
Alasan: 0 artinya tidak ada jumlah. Jadi 7 ditambah tidak ada ya
tetap 7.

## Contoh Mencongak 0 + 8
0 + 8?
Jawab: 0 + 8 = 8
Alasan: 0 artinya tidak ada jumlah. Jadi tidak ada ditambah 8
hasilnya 8.

## Contoh Mencongak 0 + 0
0 + 0?
Jawab 0.
Alasan 0 berarti tidak ada jumlah. Tidak ada apel ditambah tidak ada
apel hasilnya tentu tidak ada apel juga.

## Contoh Belajar 7 + 0
0 artinya tidak ada jumlah.
Sesuatu ditambah tidak ada hasilnya tidak berubah.
Jadi 7 + 0 = 7.
Misalnya kamu punya 7 apel di tangan, temanmu memberi 0 apel
(tidak ada apel), maka jumlah apel kamu tentu tetap 7 bukan?

## Contoh Belajar 52 + 0
0 artinya tidak ada jumlah.
Bayangkan kamu punya 52 kelereng di dalam kotak. Teman kamu bilang
"aku tambah 0 kelereng ya". Berapa kelereng di kotak sekarang?
Tentu tetap 52, karena tidak ada yang ditambahkan.
Jadi 52 + 0 = 52.

## Contoh Belajar 0 + 8
0 artinya tidak ada jumlah.
Bayangkan meja kosong, tidak ada apel sama sekali. Lalu ibu taruh
8 apel di meja. Berapa apel di meja sekarang? Tentu 8, karena yang
ada hanya apel dari ibu.
Jadi 0 + 8 = 8.

## Contoh Belajar 0 + 0
0 + 0?
Jawab 0 artinya tidak ada jumlah.
Bayangkan di tanganmu ada 2 jeruk dan tidak ada apel. Lalu teman
kamu memberi 3 jeruk lagi tapi tidak ada apel. Berapa apel ada
di tanganmu? Tentu kamu bilang tidak ada apel alias 0.
Jadi 0 + 0 = 0.

## Catatan Khusus Jenis Nol
- Komutativitas TIDAK ditambahkan untuk Jenis Nol (mengikuti pola
  modelfile v44).
- Jangan pakai jari atau enumerasi pasangan untuk Jenis Nol.
- Tetap pakai analogi konkret di mode belajar agar pedagogis.
"""


# ============================================================================
# J10: Jenis A1 (1d + 1d, hasil 1-5)
# ============================================================================
J10 = """---
id: J10_a1
kategori: per_jenis
jenis_soal: A1
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 1
hasil_min: 1
hasil_max: 5
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S01_konfigurasi_jari
  - S02_komutativitas
  - S03_format_mencongak_universal
kompleksitas: dasar
punya_carry: false
punya_cascade_1_kecil: false
version_modelfile: v44
referensi_bagian_v44: "5.1"
---

# JENIS A1: kedua operand 1 digit, hasil 1 sampai 5

## Klasifikasi
Jenis A1 berlaku jika kedua operand 1 digit DAN hasilnya 1 sampai 5.
Contoh: 1+1, 2+3, 1+4, 2+2, 3+1, 4+1, 3+2.

## Strategi
Triple verification dengan jari tangan kanan, enumerasi semua pasangan.
Pakai HANYA tangan kanan karena hasil maksimum 5.

## Pola Triple Verification (4 Langkah Wajib)
1. Tunjukkan A jari, tanya "ini berapa?". Betul, ini A.
2. Tunjukkan B jari, tanya "ini berapa?". Betul, ini B.
3. Gabungkan, tanya "kalau digabung hasilnya berapa?". Betul, ini X.
4. Simpulkan "jadi X adalah A dan B".

## Enumerasi Pasangan Wajib (per hasil)
- Hasil 2: 1+1
- Hasil 3: 2+1
- Hasil 4: 3+1, 2+2
- Hasil 5: 4+1, 3+2

## Template Mode Mencongak
[soal]?
Jawab [soal] = [jawaban]
Alasan: kita lihat bentuk jarinya, [A] jari ditambah [B] jari hasilnya
[C] jari.

## Template Mode Belajar
[Sapaan pembuka variasi.] Kita akan hitung [soal] ini pakai cara GASING.

Tunjukkan [A] jari ([sebutkan jari kanan]). Tanya "ini berapa?".
Betul, ini [A]. Tunjukkan [B] jari ([sebutkan jari kanan, lanjut]).
Tanya "ini berapa?". Betul, ini [B]. Tanya "kalau digabung hasilnya
berapa?". Betul, ini [C], karena ia lihat bentuk jarinya.

Tulis [soal] = [C].

Jumlah [C] juga bisa diperoleh dari penjumlahan berikut ini:
[Enumerasi semua pasangan yang menghasilkan C.]

Lihat kan, [C] itu terbentuk dari [pasangan-1], juga dari [pasangan-2].

Dan lihat ya, [a] + [b] hasilnya [c], dan kalau dibalik, [b] + [a]
juga hasilnya [c].

## Contoh Mencongak 2 + 3
2 + 3?
Jawab 2 + 3 = 5
Alasan: kita lihat bentuk jarinya, 2 jari ditambah 3 jari hasilnya
5 jari.

## Contoh Belajar 2 + 3
Hai, kamu hebat sekali sudah mau belajar matematika. Kita akan hitung
2 + 3 ini pakai cara GASING.

Tunjukkan 2 jari (kelingking, manis kanan). Tanya "ini berapa?".
Betul, ini dua. Tunjukkan 3 jari (tengah, telunjuk, jempol kanan).
Tanya "ini berapa?". Betul, ini tiga. Tanya "kalau digabung hasilnya
berapa?". Betul, ini lima, karena ia lihat bentuk jarinya.

Tulis 2 + 3 = 5.

Jumlah 5 juga bisa diperoleh dari penjumlahan berikut ini:

Kita mulai dengan menunjukkan 5 jari tangan kanan. Tanya "ini berapa?".
Betul, ini lima.

Tunjukkan 4 jari (kelingking, manis, tengah, telunjuk kanan). Tanya
"ini berapa?". Betul, ini empat. Tunjukkan 1 jari (jempol kanan).
Tanya "ini berapa?". Betul, ini satu. Gabungkan, tanya "kalau digabung
hasilnya berapa?". Betul, ini lima. Simpulkan "jadi lima adalah empat
dan satu".

Tunjukkan 3 jari (kelingking, manis, tengah kanan). Tanya "ini berapa?".
Betul, ini tiga. Tunjukkan 2 jari (telunjuk, jempol kanan). Tanya "ini
berapa?". Betul, ini dua. Gabungkan, tanya "kalau digabung hasilnya
berapa?". Betul, ini lima. Simpulkan "jadi lima adalah tiga dan dua".

Lihat kan, 5 itu terbentuk dari 4 dan 1, juga dari 3 dan 2.

Dan lihat ya, 2 + 3 hasilnya 5, dan kalau dibalik, 3 + 2 juga
hasilnya 5.
"""


# ============================================================================
# J20: Jenis A2 (1d + 1d, hasil 6-10)
# ============================================================================
J20 = """---
id: J20_a2
kategori: per_jenis
jenis_soal: A2
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 1
hasil_min: 6
hasil_max: 10
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S01_konfigurasi_jari
  - S02_komutativitas
  - S03_format_mencongak_universal
kompleksitas: dasar
punya_carry: false
punya_cascade_1_kecil: false
punya_pasangan_10: true
version_modelfile: v44
referensi_bagian_v44: "5.2"
---

# JENIS A2: kedua operand 1 digit, hasil 6 sampai 10

## Klasifikasi
Jenis A2 berlaku jika kedua operand 1 digit DAN hasilnya 6 sampai 10.
Contoh: 4+5, 3+4, 6+2, 7+3, 5+5, 4+4, 6+3.

## Strategi
Sama dengan A1 (triple verification + enumerasi pasangan), tetapi pakai
KEDUA tangan karena hasil lebih dari 5. Konfigurasi: tangan kanan
penuh dulu (5 jari), lalu lanjut ke tangan kiri.

## Enumerasi Pasangan Lanjutan (per hasil)
- Hasil 6: 5+1, 4+2, 3+3
- Hasil 7: 6+1, 5+2, 4+3
- Hasil 8: 7+1, 6+2, 5+3, 4+4
- Hasil 9: 8+1, 7+2, 6+3, 5+4
- Hasil 10: 9+1, 8+2, 7+3, 6+4, 5+5

## Aturan Khusus Hasil 10: Pasangan 10
Setelah enumerasi pasangan dan SEBELUM kalimat komutativitas, WAJIB
tambahkan kalimat ini:

"Pasangan bilangan yang jumlahnya 10 ini disebut pasangan 10. Pasangan
ini istimewa karena dua bilangan yang hurufnya sama mempunyai jumlah
10. Satu Sembilan, sama-sama mulai dengan huruf S. Dua Delapan,
sama-sama D. Tiga Tujuh, sama-sama T. Empat Enam, sama-sama E. Lima
Lima, sama-sama L. Semuanya pasangan 10. Mudah sekali diingat."

## Template Mode Mencongak (sama format dengan A1)
[soal]?
Jawab [soal] = [jawaban]
Alasan: kita lihat bentuk jarinya, [A] jari ditambah [B] jari hasilnya
[C] jari.

## Contoh Mencongak 4 + 5
4 + 5?
Jawab 4 + 5 = 9
Alasan: kita lihat bentuk jarinya, 4 jari ditambah 5 jari hasilnya
9 jari.

## Contoh Mencongak 7 + 3 (hasil 10)
7 + 3?
Jawab 7 + 3 = 10
Alasan: kita lihat bentuk jarinya, 7 jari ditambah 3 jari hasilnya
10 jari.

## Contoh Belajar 4 + 5
Mantap! Kita akan belajar 4 + 5 pakai cara GASING.

Tunjukkan 4 jari (kelingking, manis, tengah, telunjuk kanan). Tanya
"ini berapa?". Betul, ini empat. Tunjukkan 5 jari (jempol kanan +
jempol, telunjuk, tengah, manis kiri). Tanya "ini berapa?". Betul,
ini lima. Tanya "kalau digabung hasilnya berapa?". Betul, ini sembilan,
karena ia lihat bentuk jarinya.

Tulis 4 + 5 = 9.

Jumlah 9 juga bisa diperoleh dari penjumlahan berikut ini:

Kita mulai dengan menunjukkan 9 jari (5 kanan + jempol, telunjuk,
tengah, manis kiri). Tanya "ini berapa?". Betul, ini sembilan.

Tunjukkan 8 jari (5 kanan + jempol, telunjuk, tengah kiri). Tanya
"ini berapa?". Betul, ini delapan. Tunjukkan 1 jari (manis kiri).
Tanya "ini berapa?". Betul, ini satu. Gabungkan, tanya "kalau digabung
hasilnya berapa?". Betul, ini sembilan. Simpulkan "jadi sembilan
adalah delapan dan satu".

[Lanjutkan enumerasi: 7+2, 6+3, 5+4.]

Lihat kan, 9 itu terbentuk dari 8 dan 1, dari 7 dan 2, dari 6 dan 3,
juga dari 5 dan 4.

Dan lihat ya, 4 + 5 hasilnya 9, dan kalau dibalik, 5 + 4 juga
hasilnya 9.

## Contoh Belajar 7 + 3 (HASIL 10, WAJIB PASANGAN 10)
Wah keren pertanyaannya. Kita akan hitung 7 + 3 pakai cara GASING.

Tunjukkan 7 jari (5 kanan + jempol, telunjuk kiri). Tanya "ini berapa?".
Betul, ini tujuh. Tunjukkan 3 jari (tengah, manis, kelingking kiri).
Tanya "ini berapa?". Betul, ini tiga. Tanya "kalau digabung hasilnya
berapa?". Betul, ini sepuluh, karena ia lihat bentuk jarinya.

Tulis 7 + 3 = 10.

Jumlah 10 juga bisa diperoleh dari penjumlahan berikut ini:
[Enumerasi 9+1, 8+2, 7+3, 6+4, 5+5.]

Pasangan bilangan yang jumlahnya 10 ini disebut pasangan 10. Pasangan
ini istimewa karena dua bilangan yang hurufnya sama mempunyai jumlah
10. Satu Sembilan, sama-sama mulai dengan huruf S. Dua Delapan,
sama-sama D. Tiga Tujuh, sama-sama T. Empat Enam, sama-sama E. Lima
Lima, sama-sama L. Semuanya pasangan 10. Mudah sekali diingat.

Dan lihat ya, 7 + 3 hasilnya 10, dan kalau dibalik, 3 + 7 juga
hasilnya 10.
"""


# ============================================================================
# J30: Jenis B1 (10 + X)
# ============================================================================
J30 = """---
id: J30_b1
kategori: per_jenis
jenis_soal: B1
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 2
pola: "10 + X (X = 1 sampai 9)"
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S01_konfigurasi_jari
  - S02_komutativitas
  - S03_format_mencongak_universal
kompleksitas: dasar
punya_carry: false
version_modelfile: v44
referensi_bagian_v44: "5.3"
---

# JENIS B1: 10 + X (X = 1 sampai 9)

## Klasifikasi
Jenis B1 berlaku jika operand pertama adalah TEPAT 10 dan operand
kedua adalah 1 digit (1 sampai 9).
Contoh: 10+1, 10+5, 10+9, 10+3, 10+7.

## Strategi
Pola "10 di kepala, X di tangan". 10 dimasukkan ke kepala sebagai
abstraksi, X tetap di tangan sebagai konkret.

## Langkah Inti Mode Belajar
1. Tunjukkan 10 (5 kanan + 5 kiri). Tanya "ini berapa?". Betul,
   ini sepuluh.
2. Masukkan 10 ke kepala. Tutup mata sebentar, bayangkan 10 ada di
   kepala. Buka mata, tangan kosong.
3. Tunjukkan X jari (mulai kelingking kanan).
4. Dekatkan X ke kepala. Di kepala ada 10, di tangan ada X.
5. Kalau dijumlah, 10 dan X adalah 1X.
6. Tutup dengan komutativitas.

## Template Mode Mencongak
[soal]?
Jawab [soal] = [jawaban]
Alasan: 10 di kepala, X di tangan, 10 dan X adalah 1X.

## Contoh Mencongak 10 + 5
10 + 5?
Jawab 10 + 5 = 15
Alasan: 10 di kepala, 5 di tangan, 10 dan 5 adalah 15.

## Contoh Belajar 10 + 1
Hai, kamu hebat sekali. Kita akan hitung 10 + 1 ini pakai cara GASING.

Pertama, kita lihat angka 10. Kita tunjukkan semua jari, 5 jari di
tangan kanan dan 5 jari di tangan kiri. Tanya "ini berapa?". Betul,
ini sepuluh.

Sekarang, kita masukkan 10 ini ke kepala. Tutup mata sebentar,
bayangkan 10 ada di kepala. Buka mata, tangan kosong.

Selanjutnya, kita lihat angka 1. Kita tunjukkan 1 jari (kelingking
kanan). Tanya "ini berapa?". Betul, ini satu.

Sekarang kita dekatkan 1 ke kepala. Di kepala ada 10, di tangan ada
1. Kalau dijumlah, 10 dan 1 adalah 11.

Tulis 10 + 1 = 11.

Dan lihat ya, 10 + 1 hasilnya 11, dan kalau dibalik, 1 + 10 juga
hasilnya 11.
"""


# ============================================================================
# J40: Jenis B2 (X + 10)
# ============================================================================
J40 = """---
id: J40_b2
kategori: per_jenis
jenis_soal: B2
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 2
pola: "X + 10 (X = 1 sampai 9)"
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S01_konfigurasi_jari
  - S02_komutativitas
  - S03_format_mencongak_universal
kompleksitas: dasar
punya_carry: false
version_modelfile: v44
referensi_bagian_v44: "5.4"
---

# JENIS B2: X + 10 (X = 1 sampai 9)

## Klasifikasi
Jenis B2 berlaku jika operand pertama adalah 1 digit (1 sampai 9)
dan operand kedua adalah TEPAT 10.
Contoh: 3+10, 7+10, 9+10, 5+10, 2+10.

## Strategi
Konversi ke Jenis B1 via komutativitas, lalu pakai pola B1
("10 di kepala, X di tangan").

## Template Mode Mencongak
[soal]?
Jawab [soal] = [jawaban]
Alasan: X + 10 sama dengan 10 + X (kalau dibalik hasilnya sama),
10 di kepala, X di tangan, jadi 1X.

## Contoh Mencongak 7 + 10
7 + 10?
Jawab 7 + 10 = 17
Alasan: 7 + 10 sama dengan 10 + 7 (kalau dibalik hasilnya sama),
10 di kepala, 7 di tangan, jadi 17.

## Contoh Belajar 7 + 10
Bagus sekali pertanyaan kamu. Kita akan hitung 7 + 10 pakai cara GASING.

Karena 7 + 10 sama dengan 10 + 7 (kalau dibalik hasilnya sama), kita
pakai cara yang lebih mudah: taruh 10 di kepala.

Kita tunjukkan semua jari, 5 kanan dan 5 kiri. Tanya "ini berapa?".
Betul, ini sepuluh. Masukkan 10 ke kepala. Tutup mata sebentar,
bayangkan 10 ada di kepala. Buka mata, tangan kosong.

Sekarang tunjukkan 7 jari (5 kanan + jempol, telunjuk kiri). Tanya
"ini berapa?". Betul, ini tujuh.

Dekatkan 7 ke kepala. Di kepala ada 10, di tangan ada 7. Kalau
dijumlah, 10 dan 7 adalah 17.

Tulis 7 + 10 = 17.

Dan lihat ya, 7 + 10 hasilnya 17, dan kalau dibalik, 10 + 7 juga
hasilnya 17.
"""


# ============================================================================
# J50: Jenis B3 (1d + 1d, hasil 11-19)
# ============================================================================
J50 = """---
id: J50_b3
kategori: per_jenis
jenis_soal: B3
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 1
hasil_min: 11
hasil_max: 19
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S01_konfigurasi_jari
  - S02_komutativitas
  - S03_format_mencongak_universal
kompleksitas: menengah
punya_carry: true
pakai_pasangan_10: true
version_modelfile: v44
referensi_bagian_v44: "5.5"
---

# JENIS B3: kedua operand 1 digit, hasil 11 sampai 19

## Klasifikasi
Jenis B3 berlaku jika kedua operand 1 digit DAN hasilnya 11 sampai 19.
Contoh: 9+5, 8+7, 7+6, 5+9, 6+8, 9+9, 8+4.

## Strategi
Pasangan 10. Operand BESAR masuk kepala, cari pasangan supaya 10,
pindahkan sejumlah jari dari operand kecil, sisa di tangan.

## Aturan Konversi
- Operand 1 LEBIH BESAR dari operand 2: langsung pakai pasangan 10.
- Operand 1 LEBIH KECIL dari operand 2: KONVERSI dulu via komutativitas
  (yang besar di kepala).
  - Mode belajar: "kalau dibalik hasilnya sama, yang lebih besar
    di kepala"
  - Mode mencongak: "[a] + [b] sama dengan [b] + [a] (yang lebih besar
    di kepala)"

## Gesture Mode Belajar
- "Tutup mata sebentar, bayangkan [operand besar] ada di kepala.
  Buka mata, tangan kosong."
- Pemindahan jari: jari paling kiri menuju jempol kiri. Setelah
  jempol kiri, tekuk jempol kanan dulu, lalu telunjuk, lalu tengah,
  urut ke kelingking.
- Pemindahan 1 jari mode belajar: detail.
- Pemindahan 2 jari atau lebih: WAJIB detail urutan tekuk.

## Template Mode Mencongak
[soal]?
Jawab [soal] = [jawaban]
Alasan: bayangkan [operand besar] di kepala, [operand kecil] di tangan,
pasangan [operand besar] supaya 10 itu [Y], pindahkan [Y] jari,
sisanya [Z], jadi 10 dan [Z] itu [jawaban].

## Contoh Mencongak 9 + 5
9 + 5?
Jawab 9 + 5 = 14
Alasan: bayangkan 9 di kepala, 5 di tangan, pasangan 9 supaya 10
itu 1, pindahkan 1 jari dari 5 ke kepala, sisanya 4, jadi 10 dan
4 itu 14.

## Contoh Mencongak 5 + 9 (operand 1 lebih kecil, konversi)
5 + 9?
Jawab 5 + 9 = 14
Alasan: 5 + 9 sama dengan 9 + 5 (yang lebih besar di kepala),
bayangkan 9 di kepala, 5 di tangan, pasangan 9 supaya 10 itu 1,
pindahkan 1 jari, sisanya 4, jadi 10 dan 4 itu 14.

## Contoh Mencongak 8 + 5 (pemindahan 2 jari)
8 + 5?
Jawab 8 + 5 = 13
Alasan: bayangkan 8 di kepala, 5 di tangan, pasangan 8 supaya 10
itu 2, pindahkan 2 jari (jempol kanan dulu, lalu telunjuk kanan),
sisanya 3 (kelingking, manis, tengah kanan), jadi 10 dan 3 itu 13.

## Contoh Belajar 9 + 5
Hai, kamu hebat sekali. Kita akan hitung 9 + 5 ini pakai cara GASING.

Pertama, kita lihat angka 9. Tunjukkan 9 jari (5 kanan + jempol,
telunjuk, tengah, manis kiri). Tanya "ini berapa?". Betul, ini sembilan.

Sekarang masukkan 9 ke kepala. Tutup mata sebentar, bayangkan 9 ada
di kepala. Buka mata, tangan kosong.

Selanjutnya, kita lihat angka 5. Tunjukkan 5 jari (5 kanan, mulai
dari kelingking). Tanya "ini berapa?". Betul, ini lima.

Pasangan 9 supaya 10 adalah 1. Jadi kita pindahkan 1 jari dari 5 ke
kepala. Tekuk jempol kanan, pindahkan ke kepala. Sisanya berapa?
Betul, ini empat (kelingking, manis, tengah, telunjuk kanan).

Sekarang di kepala ada 10, di tangan ada 4. Kalau dijumlah, 10 dan
4 adalah 14.

Tulis 9 + 5 = 14.

Dan lihat ya, 9 + 5 hasilnya 14, dan kalau dibalik, 5 + 9 juga
hasilnya 14.

## Contoh Belajar 5 + 9 (Operand 1 Lebih Kecil)
Mantaaaap! Yuk kita pelajari 5 + 9 pakai cara GASING.

Karena 5 lebih kecil dari 9, kita balik dulu: 5 + 9 sama dengan
9 + 5 (kalau dibalik hasilnya sama). Yang lebih besar masuk kepala.

[Lanjutkan persis seperti contoh 9 + 5 di atas, tutup dengan
komutativitas berbasis soal ASLI: "5 + 9 hasilnya 14, dan kalau
dibalik, 9 + 5 juga hasilnya 14."]

## Contoh Belajar 8 + 5 (Pemindahan 2 Jari)
Wah pintar sekali kamu menanyakan ini. Kita akan hitung 8 + 5 pakai
cara GASING.

Tunjukkan 8 jari (5 kanan + jempol, telunjuk, tengah kiri). Tanya
"ini berapa?". Betul, ini delapan. Masukkan 8 ke kepala.

Tunjukkan 5 jari (5 kanan). Pasangan 8 supaya 10 adalah 2. Pindahkan
2 jari dari 5 ke kepala. Tekuk jempol kanan dulu, pindahkan ke kepala.
Lalu tekuk telunjuk kanan, pindahkan ke kepala. Sisanya berapa?
Betul, ini tiga (kelingking, manis, tengah kanan).

Sekarang di kepala ada 10, di tangan ada 3. Kalau dijumlah, 10 dan
3 adalah 13.

Tulis 8 + 5 = 13.

Dan lihat ya, 8 + 5 hasilnya 13, dan kalau dibalik, 5 + 8 juga
hasilnya 13.
"""


# ============================================================================
# J60: Jenis C (2d + 1d)
# ============================================================================
J60 = """---
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

## Klasifikasi
Jenis C berlaku jika operand pertama 2 digit DAN operand kedua 1 digit.
Contoh: 13+4, 25+7, 38+5, 47+8, 14+3.

## Strategi
Pakai cara cepat GASING. Mulai dari PULUHAN (depan), lirik kanan ke
satuan. JANGAN pakai pola Jenis D (dekomposisi penuh nilai tempat).

## Template Mode Belajar
Pakai cara cepat GASING.
Puluhan: [puluhan dari operand 1]
Lirik kanan satuan [satuan op1] + [op2] = [hasil satuan].

KALAU hasil satuan kurang dari 10:
  Puluhan: tetap [puluhan] (tidak perlu tambah karena satuan kurang
  dari 10).
  Satuan: [hasil satuan].

KALAU hasil satuan lebih besar atau sama dengan 10:
  Puluhan: tambah 1 jadi [puluhan+1].
  Satuan: [hasil-10] (ambil [hasil-10] karena 1-nya ke puluhan).

Jadi [soal] = [jawaban].

Tutup dengan komutativitas: "Dan lihat ya, [a] + [b] hasilnya
[jawaban], dan kalau dibalik, [b] + [a] juga hasilnya [jawaban]."

## Template Mode Mencongak
Berapa [soal]?
Jawab: [soal] = [jawaban]
Alasan: Pakai cara cepat GASING.
Puluhan [tetap/jadi] [nilai] karena satuannya [operasi] = [hasil],
[kurang dari/lebih dari atau sama dengan] 10.
[Kalau >= 10: Tambah 1 ke puluhan.]
[Satuan jadi [nilai].]
Jadi [soal] = [jawaban].

## Contoh Belajar 13 + 4 (satuan kurang dari 10)
Pakai cara cepat GASING.
Puluhan: 1
Lirik kanan satuan 3 + 4 = 7, kurang dari 10.
Puluhan: tetap 1 (tidak perlu tambah karena satuan kurang dari 10).
Satuan: 7.
Jadi 13 + 4 = 17.

Dan lihat ya, 13 + 4 hasilnya 17, dan kalau dibalik, 4 + 13 juga
hasilnya 17.

## Contoh Belajar 25 + 7 (satuan lebih dari atau sama dengan 10)
Pakai cara cepat GASING.
Puluhan: 2
Lirik kanan satuan 5 + 7 = 12, lebih dari atau sama dengan 10.
Tambah 1 ke puluhan.
Puluhan jadi 2 + 1 = 3.
Satuan: 12, ambil 2 (karena 1-nya ke puluhan).
Jadi 25 + 7 = 32.

Dan lihat ya, 25 + 7 hasilnya 32, dan kalau dibalik, 7 + 25 juga
hasilnya 32.

## Contoh Mencongak 13 + 4 (satuan kurang dari 10)
Berapa 13 + 4?
Jawab: 13 + 4 = 17
Alasan: Pakai cara cepat GASING.
Puluhan tetap 1 karena satuannya 3 + 4 = 7, kurang dari 10.
Jadi 13 + 4 = 17.

## Contoh Mencongak 25 + 7 (satuan lebih dari atau sama dengan 10)
Berapa 25 + 7?
Jawab: 25 + 7 = 32
Alasan: Pakai cara cepat GASING.
Puluhan jadi 3 karena satuannya 5 + 7 = 12, lebih dari atau sama
dengan 10. Tambah 1 ke puluhan.
Satuan jadi 2.
Jadi 25 + 7 = 32.
"""


# ============================================================================
# J70: Jenis D (maks 2 digit: 2d+2d atau 1d+2d)
# ============================================================================
J70 = """---
id: J70_d
kategori: per_jenis
jenis_soal: D
topik: penjumlahan
operand_min_digit: 1
operand_max_digit: 2
pola: "maks 2 digit (2d+2d atau 1d+2d)"
mode_tercakup:
  - belajar
  - mencongak
konsep_terkait:
  - S02_komutativitas
  - S03_format_mencongak_universal
  - S04_format_dua_cara
kompleksitas: menengah
punya_carry: true
punya_cascade_1_kecil: false
sub_kasus:
  - D1: 2d+2d, satuan kurang dari 10
  - D2: 2d+2d, satuan lebih atau sama dengan 10
  - D3: 1d+2d, satuan kurang dari 10
  - D4: 1d+2d, satuan lebih atau sama dengan 10
version_modelfile: v44
referensi_bagian_v44: "5.7"
---

# JENIS D: maks 2 digit (2d+2d atau 1d+2d)

## Klasifikasi
Jenis D berlaku jika operand maksimum 2 digit dan kedua operand bukan
TEPAT 10 (kalau salah satu tepat 10, masuk B1/B2). Bisa 2d+2d atau
1d+2d. Tidak termasuk Jenis C (2d+1d), karena urutan klasifikasi
mendahulukan C.
Contoh: 32+21, 37+29, 2+21, 7+29, 45+38.

## Strategi
Dekomposisi nilai tempat 2-level. Hitung puluhan dulu, lirik kanan
satuan, sesuaikan jika satuan lebih dari atau sama dengan 10. KEDUA
CARA WAJIB DITAMPILKAN (cara lengkap + cara singkat dengan bracket).

## Aturan Penting
- JANGAN pakai pola Jenis C (cara cepat dengan "puluhan dari operand 1"
  saja). Pakai pola Jenis D (dekomposisi penuh).
- WAJIB hitung kedua puluhan (atau identifikasi salah satu operand
  tidak punya puluhan).
- Untuk angka 1 digit di Jenis D: JANGAN pakai "puluhannya nol" atau
  "0 puluhan".
  Frasa baku: "puluhannya tidak ada alias 0" atau "puluhan dari [a]
  tidak ada alias 0".
- Mode mencongak: pakai format matematis "0 + [P2] = [P2]" untuk
  puluhan kosong.
- Mode belajar: pakai format pedagogis "tidak ada + [P2]" untuk
  puluhan kosong.

## Cara Singkat (Bracket) - HANYA Jenis D
Format: [puluhan op1 + puluhan op2][satuan op1 + satuan op2]
Contoh: 32 + 21 = [3+2][2+1] = [5][3] = 53
Contoh dengan carry: 37 + 29 = [3+2][7+9] = [5][16] = [5+1][6] = 66

## Sub Kasus D1: 2d+2d, satuan kurang dari 10

### Contoh D1 Mencongak: berapa 32 + 21?
Berapa 32 + 21?
Jawab: 32 + 21 = 53
Alasan: Dikerjakan dari depan (mulai dari puluhan)
puluhan 3 + 2 = 5
lirik kanan, jumlah satuan kurang dari 10, puluhan tetap 5.
Satuan 2 + 1 = 3
Jadi 32 + 21 = 53

Cara singkat:
32 + 21 =
Puluhan 3+2 = 5, lirik kanan satuan kurang dari 10, puluhan 5
Satuan 2 + 1 = 3
Jadi 32 + 21 = 53

### Contoh D1 Belajar: berapa 32 + 21?
Berapa 32 + 21?
32 terdiri dari 3 puluhan dan 2 satuan
21 terdiri dari 2 puluhan dan 1 satuan
Jumlahkan sesuai dengan nilai tempatnya
Puluhan: 3 puluhan + 2 puluhan = 5 puluhan
Satuan: 2 satuan + 1 satuan = 3 satuan
32 + 21 = 53

Cara singkat:
32 + 21 = [3+2][2+1] = [5][3] = 53

Dan lihat ya, 32 + 21 hasilnya 53, dan kalau dibalik, 21 + 32 juga
hasilnya 53.

## Sub Kasus D2: 2d+2d, satuan lebih dari atau sama dengan 10

### Contoh D2 Mencongak: berapa 37 + 29?
Berapa 37 + 29?
Jawab: 37 + 29 = 66
Alasan: Dikerjakan dari depan (mulai dari puluhan)
puluhan 3 + 2 = 5
lirik kanan, jumlah satuan lebih dari atau sama dengan 10, puluhan
tambah 1, jadi 6.
Satuan 7 + 9 = 16 (ambil 6)
Jadi 37 + 29 = 66

Cara singkat:
37 + 29 =
Puluhan 3+2 = 5, lirik kanan satuan lebih dari atau sama dengan 10,
puluhan 6
Satuan 7+9 = 16, ambil 6
Jadi 37 + 29 = 66

### Contoh D2 Belajar: berapa 37 + 29?
Berapa 37 + 29?
37 terdiri dari 3 puluhan dan 7 satuan
29 terdiri dari 2 puluhan dan 9 satuan
Jumlahkan sesuai dengan nilai tempatnya
Puluhan: 3 puluhan + 2 puluhan = 5 puluhan
Satuan: 7 satuan + 9 satuan = 16 satuan = 1 puluhan 6 satuan
Puluhan: 5 puluhan + 1 puluhan = 6 puluhan
Satuan: 6 satuan
37 + 29 = 66

Cara singkat:
37 + 29 = [3+2][7+9] = [5][16] = [5+1][6] = 66

Dan lihat ya, 37 + 29 hasilnya 66, dan kalau dibalik, 29 + 37 juga
hasilnya 66.

## Sub Kasus D3: 1d+2d, satuan kurang dari 10

### Contoh D3 Mencongak: berapa 2 + 21?
Berapa 2 + 21?
Jawab: 2 + 21 = 23
Alasan: Dikerjakan dari depan (mulai dari puluhan)
puluhan dari 2 tidak ada alias 0, puluhan dari 21 adalah 2.
Puluhan 0 + 2 = 2
lirik kanan, jumlah satuan kurang dari 10, puluhan tetap 2.
Satuan 2 + 1 = 3
Jadi 2 + 21 = 23

### Contoh D3 Belajar: berapa 2 + 21?
2 + 21 =
2 terdiri dari tidak ada puluhan alias 0 puluhan dan 2 satuan
21 terdiri dari 2 puluhan dan 1 satuan
Puluhannya dijumlahkan tidak ada + 2
Hasilnya 2 puluhan
lirik kanan, jumlah satuan kurang dari 10, puluhan tetap 2
Satuannya dijumlahkan 2 + 1
Hasilnya 3 satuan
Jadi 2 + 21 = 23 yang terdiri dari 2 puluhan dan 3 satuan.

Dan lihat ya, 2 + 21 hasilnya 23, dan kalau dibalik, 21 + 2 juga
hasilnya 23.

## Sub Kasus D4: 1d+2d, satuan lebih dari atau sama dengan 10

### Contoh D4 Mencongak: berapa 7 + 29?
Berapa 7 + 29?
Jawab: 7 + 29 = 36
Alasan: Dikerjakan dari depan (mulai dari puluhan)
puluhan dari 7 tidak ada alias 0, puluhan dari 29 adalah 2.
Puluhan 0 + 2 = 2
lirik kanan, jumlah satuan lebih dari atau sama dengan 10, puluhan
tambah 1, jadi 3.
Satuan 7 + 9 = 16 (ambil 6)
Jadi 7 + 29 = 36

### Contoh D4 Belajar: berapa 7 + 29?
7 + 29 =
7 terdiri dari tidak ada puluhan alias 0 puluhan dan 7 satuan
29 terdiri dari 2 puluhan dan 9 satuan
Puluhannya dijumlahkan tidak ada + 2
Hasilnya 2 puluhan
lirik kanan, jumlah satuan lebih besar atau sama dengan 10, puluhannya
ditambah 1.
Puluhan 2 + 1 = 3
Satuannya dijumlahkan 7 + 9 = 16 (ambil 6, satuannya saja, karena
1 nya sudah ditambahkan ke puluhan)
Hasilnya 6 satuan
Jadi 7 + 29 = 36 yang terdiri dari 3 puluhan dan 6 satuan.

Dan lihat ya, 7 + 29 hasilnya 36, dan kalau dibalik, 29 + 7 juga
hasilnya 36.
"""


# ============================================================================
# Write all chunks to files
# ============================================================================
CHUNKS = {
    "J00_nol.md": J00,
    "J10_a1.md": J10,
    "J20_a2.md": J20,
    "J30_b1.md": J30,
    "J40_b2.md": J40,
    "J50_b3.md": J50,
    "J60_c.md": J60,
    "J70_d.md": J70,
}


def main():
    for filename, content in CHUNKS.items():
        path = OUT_DIR / filename
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path} ({len(content)} chars)")
    print(f"\nTotal: {len(CHUNKS)} per-jenis chunks (Nol s.d. D) generated")


if __name__ == "__main__":
    main()
