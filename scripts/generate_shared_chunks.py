#!/usr/bin/env python3
"""
Generator chunks shared untuk AI Tutor GASING v44.

Chunks shared adalah konsep dasar yang digunakan lintas jenis soal.
Mereka diambil dari BAGIAN 4 modelfile v44 (Konsep Dasar GASING).

Output: chunks/shared/*.md
"""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "chunks" / "shared"
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# S01: Konfigurasi Jari (urutan jari, aturan tangan, konfigurasi, notasi)
# ============================================================================
S01 = """---
id: S01_konfigurasi_jari
kategori: shared
topik: penjumlahan
referensi_bagian_v44: "4.1, 4.2, 4.3, 4.4, 4.5"
mode_tercakup:
  - belajar
kompleksitas: dasar
jenis_yang_pakai:
  - A1
  - A2
  - B1
  - B2
  - B3
version_modelfile: v44
---

# KONFIGURASI JARI GASING

## Urutan Posisi Jari (1 sampai 10)
Posisi 1: kelingking kanan
Posisi 2: manis kanan
Posisi 3: tengah kanan
Posisi 4: telunjuk kanan
Posisi 5: jempol kanan
Posisi 6: jempol kiri
Posisi 7: telunjuk kiri
Posisi 8: tengah kiri
Posisi 9: manis kiri
Posisi 10: kelingking kiri

## Aturan Tangan
Hasil 1 sampai 5: HANYA tangan kanan.
Hasil 6 sampai 10: penuhkan tangan kanan dulu, lalu tangan kiri.
Hasil 11 sampai 19: konsep "di kepala, di tangan".

## Konfigurasi Jari Standar
6 = 5 kanan + jempol kiri
7 = 5 kanan + jempol, telunjuk kiri
8 = 5 kanan + jempol, telunjuk, tengah kiri
9 = 5 kanan + jempol, telunjuk, tengah, manis kiri
10 = 5 kanan + 5 kiri

## Operand Non-Overlap
Operand 1 menempati posisi 1 sampai a.
Operand 2 MELANJUTKAN dari posisi (a+1).
TIDAK BOLEH ADA OVERLAP.

## Notasi Jari
Jika jumlah jari di satu tangan = 5: tulis "5 kanan" atau "5 kiri" (ringkas).
Jika jumlah jari di satu tangan kurang dari 5: sebutkan nama jari satu per satu.

## Contoh Penggunaan
Soal 2 + 3:
Operand 1 (2): kelingking, manis kanan.
Operand 2 (3): tengah, telunjuk, jempol kanan (lanjut dari posisi 3).

Soal 4 + 5:
Operand 1 (4): kelingking, manis, tengah, telunjuk kanan.
Operand 2 (5): jempol kanan + jempol, telunjuk, tengah, manis kiri.

Soal 7 + 3:
Operand 1 (7): 5 kanan + jempol, telunjuk kiri.
Operand 2 (3): tengah, manis, kelingking kiri (lanjut dari posisi 8).
"""


# ============================================================================
# S02: Komutativitas (kapan ditambah, kapan tidak)
# ============================================================================
S02 = """---
id: S02_komutativitas
kategori: shared
topik: penjumlahan
referensi_bagian_v44: "4.6"
mode_tercakup:
  - belajar
kompleksitas: dasar
jenis_yang_pakai:
  - A1
  - A2
  - B1
  - B2
  - B3
  - C
  - D
jenis_yang_tidak_pakai:
  - E
  - F
version_modelfile: v44
---

# KOMUTATIVITAS GASING

## Prinsip
Penjumlahan bersifat komutatif: a + b = b + a. Hasil tidak berubah
walaupun urutan operand dibalik. Di Metode GASING, prinsip ini
dijelaskan di akhir mode belajar untuk soal dengan operand maksimum
2 digit.

## Aturan Pemakaian
Komutativitas DITAMBAHKAN di akhir mode belajar untuk jenis berikut:
A1, A2, B1, B2, B3, C, D.

Komutativitas TIDAK DITAMBAHKAN untuk:
- Jenis E (3 digit), karena fokus pindah ke struktur nilai tempat.
- Jenis F (4+ digit), karena alasan yang sama.
- Mode mencongak apapun, karena format mencongak ringkas tanpa penutup.

## Template Kalimat (WAJIB DIIKUTI)
"Dan lihat ya, [a] + [b] hasilnya [c], dan kalau dibalik, [b] + [a]
juga hasilnya [c]."

Di mana:
- [a] adalah operand pertama dari soal asli.
- [b] adalah operand kedua dari soal asli.
- [c] adalah jawaban.

## Contoh Penggunaan
Soal 25 + 7 = 32:
"Dan lihat ya, 25 + 7 hasilnya 32, dan kalau dibalik, 7 + 25 juga
hasilnya 32."

Soal 4 + 5 = 9:
"Dan lihat ya, 4 + 5 hasilnya 9, dan kalau dibalik, 5 + 4 juga
hasilnya 9."

Soal 32 + 21 = 53:
"Dan lihat ya, 32 + 21 hasilnya 53, dan kalau dibalik, 21 + 32 juga
hasilnya 53."

## Catatan Penting
Kalimat ini bukan opsional. Untuk jenis-jenis yang masuk daftar wajib,
JANGAN selesaikan jawaban mode belajar tanpa kalimat komutativitas di
akhir. Ini bagian dari pedagogi GASING untuk menanamkan pemahaman
sifat penjumlahan sejak dini.
"""


# ============================================================================
# S03: Format Mencongak Universal
# ============================================================================
S03 = """---
id: S03_format_mencongak_universal
kategori: shared
topik: penjumlahan
referensi_bagian_v44: "4.7"
mode_tercakup:
  - mencongak
kompleksitas: dasar
jenis_yang_pakai:
  - Nol
  - A1
  - A2
  - B1
  - B2
  - B3
  - C
  - D
  - E
  - F
version_modelfile: v44
---

# FORMAT MENCONGAK UNIVERSAL

## Struktur Output Wajib
Untuk SEMUA jenis soal dalam mode mencongak, struktur output:

[soal]?
Jawab: [soal] = [jawaban]
Alasan: [alasan sesuai template jenis soal].

## Aturan Mutlak Mencongak
1. Jawaban WAJIB di awal setelah label "Jawab:". Bukan di akhir.
2. Alasan menyusul dengan label "Alasan:" (titik dua, BUKAN "Alasannya").
3. Format alasan WAJIB ikuti template per jenis. JANGAN dikarang.
4. Sapaan opsional. Yang penting jawaban di awal.
5. DILARANG frasa "Mari kita hitung" di mode mencongak.
6. Jawaban berada di baris kedua atau awal jawaban, bukan setelah
   penjelasan panjang.

## Contoh Struktur (Jenis A1)
Berapa 2 + 3?
Jawab: 2 + 3 = 5
Alasan: kita lihat bentuk jarinya, 2 jari ditambah 3 jari hasilnya
5 jari.

## Contoh Struktur (Jenis C)
Berapa 25 + 7?
Jawab: 25 + 7 = 32
Alasan: Pakai cara cepat GASING. Puluhan jadi 3 karena satuannya
5 + 7 = 12, lebih dari atau sama dengan 10. Tambah 1 ke puluhan.
Satuan jadi 2. Jadi 25 + 7 = 32.

## Catatan Penting
Berbeda dengan mode belajar yang panjang dan pedagogis, mode mencongak
bertujuan melatih kecepatan dan ketepatan. Karena itu format wajib
ringkas dan jawaban harus terlihat di awal. Detail langkah hanya muncul
di bagian "Alasan:" dengan format spesifik per jenis soal.
"""


# ============================================================================
# S04: Format Dua Cara (untuk Jenis D, E, F)
# ============================================================================
S04 = """---
id: S04_format_dua_cara
kategori: shared
topik: penjumlahan
referensi_bagian_v44: "4.8"
mode_tercakup:
  - belajar
  - mencongak
kompleksitas: menengah
jenis_yang_pakai:
  - D
  - E
  - F
version_modelfile: v44
---

# FORMAT DUA CARA (LENGKAP + SINGKAT)

## Prinsip Umum
Untuk Jenis D, E, dan F, jawaban WAJIB menampilkan dua bentuk:
cara lengkap (dekomposisi nilai tempat per baris) DAN cara singkat
(satu baris ringkas dengan notasi yang sesuai).

## Aturan Per Jenis

### Jenis D
- Mode belajar: cara lengkap dekomposisi nilai tempat + cara singkat
  pakai bracket [ ].
- Mode mencongak: cara lengkap + cara singkat 1 baris tanpa bracket
  dan tanpa notasi 1 kecil (karena hasil 2 digit).

### Jenis E
- Mode belajar: cara lengkap dekomposisi 3-level (Ratusan, Puluhan,
  Satuan) + cara singkat 1 baris pakai NOTASI 1 KECIL (BUKAN bracket).
- Mode mencongak: cara lengkap + cara singkat 1 baris pakai notasi 1
  kecil.

### Jenis F
- Mode belajar: cara lengkap dengan rincian nilai tempat per baris
  + cara singkat 1 baris pakai notasi 1 kecil.
- Mode mencongak: CUKUP SATU CARA (pakai lirik kanan dan Aturan
  1 kecil). Tidak ada cara singkat tambahan.

## Notasi Yang Dipakai

### Bracket [ ] (HANYA Jenis D)
Contoh: 32 + 21 = [3+2][2+1] = [5][3] = 53
Contoh: 37 + 29 = [3+2][7+9] = [5][16] = [5+1][6] = 66

### Notasi 1 Kecil ₁ (Jenis E dan F)
Subscript 1 yang menandai nilai tempat yang sama dengan digit di depannya.
Lihat chunk S05_aturan_1_kecil untuk aturan penulisan lengkap.
Contoh: 106 + 287 = 38₁3 = 393
Contoh: 4859 + 3148 = 799₁7 = 8007

## Catatan Penting
JANGAN tukar pakai bracket dan notasi 1 kecil. Bracket eksklusif untuk
Jenis D. Notasi 1 kecil eksklusif untuk Jenis E dan F. Di v44, bracket
dihilangkan total dari Jenis E (perubahan dari v43).
"""


# ============================================================================
# S05: Aturan 1 Kecil (paling komprehensif, dipakai E dan F)
# ============================================================================
S05 = """---
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
"""


# ============================================================================
# Write all chunks to files
# ============================================================================
CHUNKS = {
    "S01_konfigurasi_jari.md": S01,
    "S02_komutativitas.md": S02,
    "S03_format_mencongak_universal.md": S03,
    "S04_format_dua_cara.md": S04,
    "S05_aturan_1_kecil.md": S05,
}


def main():
    for filename, content in CHUNKS.items():
        path = OUT_DIR / filename
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path} ({len(content)} chars)")
    print(f"\nTotal: {len(CHUNKS)} shared chunks generated")


if __name__ == "__main__":
    main()
