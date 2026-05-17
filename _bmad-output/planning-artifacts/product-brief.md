# Product Brief: GASING RAG — AI Tutor Engine untuk Sacred Octagon

**Versi:** 1.0  
**Tanggal:** 2026-05-17  
**Author:** Yohanes Surya (domain expert) + BMAD Product Brief Skill  
**Status:** Draft — menunggu review  

---

## 1. Ringkasan Eksekutif

**gasing-rag** adalah AI Tutor Engine berbasis Retrieval-Augmented Generation (RAG) yang mengajarkan matematika SD menggunakan Metode GASING. Engine ini akan diintegrasikan sebagai **layanan backend** ke dalam game edukasi **Sacred Octagon** — sehingga ketika siswa mengalami kesulitan di dalam game, AI Tutor hadir memberikan bimbingan pedagogis yang otentik, hangat, dan efektif sesuai filosofi GASING.

Ini bukan sekadar chatbot matematika. Ini adalah distilasi digital dari pengalaman 23.633 siswa di 127 kabupaten/kota Indonesia yang telah dibuktikan secara ilmiah memiliki effect size 5.06 — anomali positif dalam literatur global pendidikan.

---

## 2. Konteks dan Masalah

### Sacred Octagon: Ekosistem Belajar yang Sedang Dibangun

Sacred Octagon adalah game edukasi matematika berbasis Unity dengan tiga mode:

| Mode | Pengalaman Siswa |
|---|---|
| **Asyiknya Belajar** | Pembelajaran interaktif metode GASING |
| **Asyiknya Bermain** | Berlatih melalui berbagai mini-games |
| **Asyiknya Berpetualang** | Mengerjakan soal sambil menjalani petualangan |

### Masalah yang Ingin Dipecahkan

Dalam game apapun — termasuk Sacred Octagon — ada momen ketika siswa **tersandung**. Jawaban salah. Frustrasi. Tidak mengerti. Di sinilah sistem pendidikan konvensional gagal: tidak ada guru yang hadir di saat yang tepat.

Tanpa AI Tutor yang tepat:
- Siswa menebak-nebak sampai jawaban benar (tanpa pemahaman)
- Siswa menyerah dan berhenti bermain
- Momentum belajar yang sudah dibangun game terputus

### Peluang

gasing-rag sudah memiliki fondasi yang kuat: 35 chunks knowledge GASING yang telah divalidasi (100% math accuracy, 40 test cases), sistem retrieval hybrid, dan pemahaman mendalam tentang pedagogi Metode GASING dari 4 volume buku sumber. Ini adalah peluang untuk mengubah fondasi itu menjadi **layanan yang dapat dipanggil Sacred Octagon secara real-time**.

---

## 3. Pengguna dan Kebutuhan Mereka

### Pengguna Primer: Siswa SD (6–12 tahun)

| Kebutuhan | Solusi gasing-rag |
|---|---|
| Penjelasan yang bisa dimengerti anak | Bahasa sederhana, analogi konkret (apel, jari) |
| Tidak ingin merasa "bodoh" | Respons encouraging, tidak menghakimi |
| Butuh bantuan di soal yang spesifik | Context-aware: tahu soal apa yang sedang dikerjakan |
| Ingin cepat balik bermain | Jawaban efisien, tidak bertele-tele |

### Pengguna Sekunder: Guru

| Kebutuhan | Solusi |
|---|---|
| Memantau siswa mana yang sering butuh bantuan | Dashboard/log (v2) |
| Memastikan AI mengajar dengan cara GASING yang benar | Pedagogi terkunci via RAG + system prompt |
| Bisa pakai di kelas offline | Deployment lokal via Ollama |

---

## 4. Solusi yang Diusulkan

### Arsitektur: gasing-rag sebagai Embedded AI Tutor Service

```
Sacred Octagon (Unity)
       │
       │  HTTP POST /chat
       │  { "query": "...", "soal": "25+7", "siswa": {...} }
       ▼
┌─────────────────────────────────┐
│     gasing-rag FastAPI Server    │
│                                  │
│  1. Retrieve chunks (RAG)        │
│  2. Build context                │
│  3. Call Gemma via Ollama        │
│  4. Return pedagogical response  │
└─────────────────────────────────┘
       │
       │  { "response": "...", "chunks_used": [...] }
       ▼
Sacred Octagon (tampilkan ke siswa)
```

### Komponen yang Perlu Dibangun

#### v1: API Server (Prioritas Tinggi)
- **FastAPI** REST API endpoint `POST /chat`
- Request: `{ query, soal_context (optional), mode (B/C) }`
- Response: `{ response, topik, chunks_used }`
- CORS support untuk Unity WebGL / local Unity
- Health check endpoint `GET /health`
- Deployment lokal: `uvicorn` + Ollama

#### v2: Cloud Deployment (Prioritas Menengah)
- Docker container (FastAPI + dependencies)
- Gemma via **Gemini API** (Google Cloud) untuk cloud — menggantikan Ollama lokal
- Fallback logic: coba Ollama lokal → fallback ke Gemini API
- Target platform: Railway / Render / VPS sederhana

#### v3: Multimodal & Dashboard (Prioritas Rendah)
- Input gambar (foto soal tulisan tangan siswa)
- Teacher dashboard: log siapa bertanya apa
- Analytics: soal mana yang paling sering membuat siswa kesulitan

---

## 5. Definisi Keberhasilan

### Untuk v1 (API Server)

| Metrik | Target |
|---|---|
| API response time | < 30 detik (Gemma local) |
| Math accuracy | ≥ 95% (baseline sudah 100%) |
| Uptime lokal | 99% saat Ollama running |
| Integration test | Unity dapat call dan parse response dengan benar |

### Untuk v2 (Cloud)

| Metrik | Target |
|---|---|
| API response time (cloud) | < 15 detik (Gemini API lebih cepat) |
| Concurrent users | 10 siswa simultan |
| Cost | Dalam free tier Gemini API |

---

## 6. Asumsi Kunci

| Asumsi | Risiko jika salah |
|---|---|
| Unity dapat call REST HTTP API | Rendah — UnityWebRequest sudah standar |
| Teman Yohanes akan buat Unity client berdasarkan API spec yang kita buat | Medium — perlu koordinasi API contract |
| Ollama + Gemma tersedia di mesin deployment lokal | Rendah — sudah terbukti di development |
| Gemini API bisa reproduce kualitas Gemma lokal | Medium — perlu validasi, model berbeda |
| Siswa SD mengetik dalam Bahasa Indonesia | Rendah — confirmed dari konteks |

---

## 7. Yang Tidak Termasuk Scope (v1)

- ❌ Autentikasi / sistem login siswa
- ❌ Penyimpanan riwayat percakapan per siswa
- ❌ Multimodal (gambar, suara) — masuk v3
- ❌ Dashboard guru — masuk v3
- ❌ Topik matematika selain penjumlahan — masuk fase berikutnya

---

## 8. Rekomendasi Stack Teknis

| Layer | Teknologi | Alasan |
|---|---|---|
| API Framework | **FastAPI** (Python) | Native Python, async, auto-docs, sudah 1 ekosistem dengan gasing-rag |
| LLM (lokal) | **Gemma via Ollama** | Sudah tervalidasi 100% math accuracy |
| LLM (cloud) | **Gemini API** (google-generativeai) | Gratis tier, hosted Gemma-family models |
| Deployment lokal | **uvicorn** | Standar FastAPI |
| Deployment cloud | **Railway** atau **Render** | Free tier, simple deploy dari GitHub |
| Unity client | **UnityWebRequest** | Standar Unity HTTP |

---

## 9. Langkah Berikutnya (Post-Brief)

1. **Buat API Contract** — dokumen JSON spec request/response untuk koordinasi dengan teman yang mengerjakan Unity client
2. **Jalankan `bmad-create-prd`** — Requirements Document detail
3. **Jalankan `bmad-create-epics-and-stories`** — Pecah ke stories yang bisa dikerjakan
4. **Story 1: FastAPI skeleton** — `/health` + `/chat` endpoint basic
5. **Story 2: RAG integration** — retrieve_chunks → format context → call Gemma
6. **Story 3: Unity integration test** — coordinate dengan Sacred Octagon team
7. **Story 4: Cloud deployment** — Docker + Gemini API fallback

---

## 10. Kutipan Visi

> "Ketika seorang anak di pedalaman Papua tersandung soal perkalian di tengah petualangan Sacred Octagon — GASING RAG hadir dalam hitungan detik, mengajarkan dengan cara yang sama hangat dan efektifnya seperti Prof. Yohanes Surya duduk di sebelahnya."

---

*Dokumen ini dibuat dengan BMAD Product Brief Skill v6.6.0 *  
*Untuk dilanjutkan: `bmad-create-prd` menggunakan dokumen ini sebagai input*
