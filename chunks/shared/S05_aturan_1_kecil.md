---
id: S05_aturan_1_kecil
kategori: shared
topik: penjumlahan
referensi_bagian_v44: "4.9"
mode_tercakup:
  - belajar
  - mencongak
kompleksitas: tinggi
jenis_yang_pakai:
  - E
  - F
version_modelfile: v44
---

# ATURAN 1 KECIL (NOTASI SUBSCRIPT ₁)

## Pengertian
Dalam Metode GASING, angka 1 kecil (ditulis dengan ukuran lebih kecil
sebagai subscript ₁, BUKAN pangkat) adalah tanda yang membantu siswa
menjumlahkan bilangan dengan cepat. Angka 1 kecil menyatakan bahwa
nilai 1 tersebut mempunyai nilai tempat yang sama dengan angka tepat
di depannya. Karena nilai tempatnya sama, 1 kecil itu dapat langsung
dijumlahkan dengan angka di depannya.

## Aturan Penulisan ₁ (MUTLAK)
₁ SELALU diikuti TEPAT SATU DIGIT (digit satuan dari hasil penjumlahan)
ketika ditulis sebagai notasi inline saat menjumlahkan.

Contoh penulisan:
- 17 ditulis ₁7
- 14 ditulis ₁4
- 10 ditulis ₁0
- 12 ditulis ₁2

DILARANG menulis ₁ diikuti dua digit (₁10, ₁12, ₁17) sebagai notasi
inline. Catatan: ₁ boleh berdiri sendiri di akhir grup ketika dipakai
sebagai operator (misal "799₁ = 800"); ini bukan notasi inline.

## Contoh Dasar: 18 + 19
Kerjakan dari kiri ke kanan dengan cara GASING.
Puluhan: 1 + 1 = 2
Satuan: 8 + 9 = 17, ditulis sebagai ₁7 (angka 1 kecil di depan 7).
Hasil sementara: 2₁7

Karena 1 kecil bernilai puluhan (sama dengan angka 2 di depannya),
keduanya dijumlahkan: 18 + 19 = 2₁7 = (2+1)7 = 37.

## Aturan Kaskade: 1 Kecil Berpindah Ke Kiri
Jika angka di depan 1 kecil adalah 9, maka 9 + 1 = 10. Penulisan 10
pada posisi tersebut akan memunculkan 1 kecil BARU yang berpindah satu
nilai tempat ke kiri. Proses berulang sampai bertemu angka selain 9.

### Contoh 1: 799₁
Satuan: 9 + 1 = 10, tulis 0, muncul 1 kecil di puluhan.
Puluhan: 9 + 1 = 10, tulis 0, muncul 1 kecil di ratusan.
Ratusan: 7 + 1 = 8.
799₁ = 800

### Contoh 2: 89999₁
Satuan: 9 + 1 = 10, tulis 0, ₁ pindah ke puluhan.
Puluhan: 9 + 1 = 10, tulis 0, ₁ pindah ke ratusan.
Ratusan: 9 + 1 = 10, tulis 0, ₁ pindah ke ribuan.
Ribuan: 9 + 1 = 10, tulis 0, ₁ pindah ke puluh ribuan.
Puluh ribuan: 8 + 1 = 9.
89999₁ = 90000

### Contoh 3: 9999₁ (semua 9, tidak ada digit non-9 di kiri)
Setiap 9 berubah jadi 0 saat ₁ pindah ke kiri.
Setelah semua 9 jadi 0, ₁ pindah ke kiri tapi tidak ada digit lagi.
Muncul angka 1 di paling kiri.
9999₁ = 10000

### Contoh 4: 99999₁0 (dari soal 111111 + 888889)
Satuan ₁0: angka yang ditulis 0, ada ₁ pindah ke puluhan.
Setiap 9 berikutnya jadi 0, ₁ terus pindah ke kiri.
Tidak ada digit di kiri, muncul angka 1 baru.
99999₁0 = 1000000

## Tabel Referensi Cepat Kaskade
29₁ = 30 (2 naik jadi 3, 9 jadi 0)
299₁ = 300 (2 naik jadi 3, 99 jadi 00)
2999₁ = 3000 (2 naik jadi 3, 999 jadi 000)
799₁ = 800 (7 naik jadi 8, 99 jadi 00)
89999₁ = 90000 (8 naik jadi 9, 9999 jadi 0000)
9999₁ = 10000 (tidak ada digit di kiri, muncul 1 baru)
99999₁0 = 1000000 (semua 9 jadi 0, muncul 1 baru)

## Beberapa Kelompok 1 Kecil
Jika sebuah bilangan memuat beberapa ₁ yang terpisah, setiap kelompok
diselesaikan secara terpisah, kemudian hasilnya digabungkan berurutan.

### Contoh A: 349₁4999₁
Kelompok pertama: 349₁ = 349 + 1 = 350
Kelompok kedua: 4999₁ = 4999 + 1 = 5000
Hasil gabungan: 350 | 5000 = 3.505.000

### Contoh B: 99₁5₁5
Angka 1 kecil di belakang 5 menambah digit di depannya: 5 + 1 = 6.
Struktur menjadi 99₁65. Kemudian 99₁ = 99 + 1 = 100 (efek domino
menjalar ke depan). Hasil: 10065.

### Contoh C: 69₁2799₁7
Dua angka 1 kecil pada tempat berbeda.
Kelompok pertama: 69₁ = 69 + 1 = 70
Kelompok kedua: 799₁ = 799 + 1 = 800
Digit terakhir: 7
Hasil gabungan: 70 | 2 | 800 | 7 = 7028007

## Ringkasan Untuk Siswa
Angka 1 kecil berarti "tambahkan 1 ke angka di depan saya".
- Kalau angka di depannya bukan 9: langsung dijumlahkan.
- Kalau angka di depannya 9: ubah 9 menjadi 0 dan pindahkan 1 kecil
  satu langkah ke kiri, lalu ulangi sampai bertemu angka yang bukan 9.
- Kalau semua angka adalah 9: muncul angka 1 baru di paling kiri.
