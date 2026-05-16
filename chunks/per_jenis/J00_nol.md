---
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
