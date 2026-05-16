# Indeks Dokumentasi: gasing-rag

**Versi:** 1.0.0 | **Tanggal:** 2026-05-17 | **Dihasilkan oleh:** BMAD Document Project v6.6.0

---

## Gambaran Proyek

- **Tipe:** Monolith — AI/Data Pipeline
- **Bahasa Utama:** Python 3.10+
- **Arsitektur:** Hybrid Retrieval-Augmented Generation (RAG)
- **Repository:** [github.com/Yohanespkc/test-gasing-rag](https://github.com/Yohanespkc/test-gasing-rag)

## Referensi Cepat

| Aspek | Detail |
|---|---|
| **Stack** | Python · Ollama · ChromaDB · nomic-embed-text · Gemma 4 (gemma4:e4b) |
| **Chunks** | 22 (5 shared + 17 per jenis) |
| **Topik** | Penjumlahan (v1.0.0) |
| **Validation** | 100% math accuracy, 40 test cases |
| **Entry Point** | `python scripts/03_chat.py` |

---

## Memulai (Getting Started)

### Untuk Developer Baru (Tim IT-DEL)

1. Baca [Panduan Developer](./development-guide.md) — setup dari nol hingga chat berjalan
2. Pahami arsitektur di [Architecture](./architecture.md)
3. Lihat daftar komponen di [Component Inventory](./component-inventory.md)

### Untuk Content Editor (GASING Academy)

1. Baca [Project Overview](./project-overview.md) — pahami sistem secara keseluruhan
2. Lihat [Source Tree](./source-tree-analysis.md) — cari file yang perlu diedit
3. Edit chunk `.md` di `chunks/` sesuai kebutuhan
4. Jalankan `python scripts/01_ingest.py` setelah edit

---

## Dokumentasi yang Dihasilkan

| Dokumen | Deskripsi |
|---|---|
| [Project Overview](./project-overview.md) | Ringkasan eksekutif, stack, klasifikasi jenis soal |
| [Architecture](./architecture.md) | Arsitektur teknis lengkap, data flow, keputusan desain |
| [Development Guide](./development-guide.md) | Setup, cara menjalankan, workflow pengembangan, troubleshooting |
| [Component Inventory](./component-inventory.md) | Semua chunks, scripts, data stores, dependensi |
| [Source Tree Analysis](./source-tree-analysis.md) | Struktur direktori beranotasi, entry points, folder kritis |

---

## Dokumentasi yang Sudah Ada di Proyek

| Dokumen | Lokasi | Deskripsi |
|---|---|---|
| README | [README.md](../README.md) | Arsitektur RAG, skema metadata chunk, strategi retrieval |
| Setup Guide | [SETUP.md](../SETUP.md) | Panduan setup step-by-step untuk Mac |

---

## Roadmap (dari SETUP.md)

| Fase | Keterangan |
|---|---|
| **v1.0.0 ✅** | Topik penjumlahan stabil, 100% accuracy |
| **A1** | Test bank 50 soal, validasi menyeluruh |
| **A2** | Review dengan pelatih senior GASING Academy |
| **A3** | Multimodal — dukungan gambar konfigurasi jari |
| **v2.0** | Ekspansi topik: pengurangan, perkalian, pembagian |
| **v3.0** | Web interface + multi-user support |

---

*Dokumentasi ini dihasilkan dengan BMAD Document Project v6.6.0 pada 2026-05-17.*
*Untuk update dokumentasi, jalankan ulang skill `bmad-document-project`.*
