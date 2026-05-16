---
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
