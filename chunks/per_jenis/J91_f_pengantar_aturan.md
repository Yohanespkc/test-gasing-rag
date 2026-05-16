---
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
