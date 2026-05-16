---
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
