---
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
