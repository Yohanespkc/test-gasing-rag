---
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
