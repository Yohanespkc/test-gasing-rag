---
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
