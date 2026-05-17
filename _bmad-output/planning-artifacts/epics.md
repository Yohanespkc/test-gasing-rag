---
stepsCompleted: ['step-01-validate-prerequisites']
inputDocuments:
  - '_bmad-output/planning-artifacts/prd.md'
  - 'docs/architecture.md'
---

# gasing-rag - Epic Breakdown

## Overview

Dokumen ini menyediakan breakdown epic dan story lengkap untuk **gasing-rag AI Tutor Engine**, menguraikan requirements dari PRD dan Architecture menjadi stories yang dapat diimplementasikan oleh developer.

---

## Requirements Inventory

### Functional Requirements

FR1: Siswa dapat mengirim pertanyaan matematika dalam teks bebas Bahasa Indonesia
FR2: Sistem dapat menerima konteks soal aktif (opsional) dari Sacred Octagon bersama pertanyaan
FR3: Sistem memberikan penjelasan pedagogis GASING mengikuti alur Konkret → Abstrak → Mencongak
FR4: Sistem tidak pernah memberikan jawaban langsung tanpa penjelasan proses
FR5: Sistem mendeteksi topik matematika dari pertanyaan dan mengambil chunks yang relevan
FR6: Sistem merespons dalam Bahasa Indonesia yang sesuai untuk siswa SD (kelas 1–6)
FR7: Sistem dapat meretrieve knowledge chunks berdasarkan semantic similarity query
FR8: Sistem dapat memfilter chunks berdasarkan topik (penjumlahan / filosofi_gasing / semua)
FR9: Sistem menyertakan shared chunks secara otomatis untuk soal relevan
FR10: Sistem dapat menampilkan daftar chunks yang digunakan dalam response (untuk debug)
FR11: Sacred Octagon (Unity) dapat memanggil endpoint `/chat` via HTTP POST
FR12: Sistem mengembalikan respons dalam format JSON yang dapat diparse Unity
FR13: Sacred Octagon dapat memeriksa status sistem via endpoint `/health`
FR14: Sistem mendukung CORS untuk memungkinkan request dari Unity WebGL
FR15: Sistem mengembalikan pesan error dalam format JSON untuk semua kasus gagal
FR16: Sistem dapat berjalan sepenuhnya offline menggunakan Ollama lokal
FR17: Sistem dapat dikonfigurasi untuk menggunakan Gemini API sebagai alternatif Ollama
FR18: Administrator dapat memeriksa status koneksi Ollama dan ChromaDB via health check
FR19: Sistem dapat dijalankan dengan perintah tunggal (`uvicorn`) tanpa konfigurasi kompleks
FR20: Sistem menolak request dengan query kosong atau di bawah panjang minimum
FR21: Sistem membatasi jumlah request per IP dalam periode waktu tertentu (v2)
FR22: Sistem memvalidasi API key untuk request dari client yang diizinkan (v2)

### Non-Functional Requirements

NFR1: Endpoint `/chat` mengembalikan respons dalam ≤ 30 detik (Ollama lokal)
NFR2: Endpoint `/chat` mengembalikan respons dalam ≤ 15 detik (Gemini API cloud)
NFR3: Endpoint `/health` mengembalikan respons dalam ≤ 500 ms
NFR4: Sistem mendukung minimum 5 concurrent requests tanpa degradasi signifikan
NFR5: ChromaDB collection di-load saat startup, bukan per-request
NFR6: Sistem mengembalikan HTTP 503 JSON jika Ollama tidak tersedia
NFR7: Sistem mengembalikan HTTP 503 JSON jika ChromaDB tidak dapat diakses
NFR8: Math accuracy ≥ 95% untuk topik penjumlahan (diukur via 05_validate.py)
NFR9: Sistem tidak pernah mengembalikan jawaban matematika yang salah tanpa indikasi
NFR10: Response JSON kompatibel dengan Unity JsonUtility atau Newtonsoft.Json
NFR11: API menerima request dalam ≤ 5 detik setelah server startup
NFR12: CORS headers hadir di semua response untuk mendukung Unity WebGL
NFR13: Arsitektur stateless memungkinkan horizontal scaling tanpa refactoring
NFR14: Penambahan topik matematika baru tidak memerlukan perubahan kode API

### Additional Requirements (dari Architecture)

- RAG engine (ChromaDB + nomic-embed-text) sudah berjalan — perlu di-wrap dalam FastAPI
- Ollama sudah terinstall lokal dengan model gemma4:e4b
- 35 chunks sudah ter-index di ChromaDB (22 penjumlahan + 13 filosofi)
- `utils.py` (retrieve_chunks) sudah tersedia sebagai library — tidak perlu diubah
- System prompt GASING sudah terdefinisi di scripts lama — perlu diekstrak ke FastAPI server
- Tidak ada database eksternal — ChromaDB adalah satu-satunya persistent store
- Python environment: `.venv` dengan dependencies di `pyproject.toml`
- Tidak perlu starter template — project sudah ada (brownfield)

### UX Design Requirements

Tidak ada — produk ini adalah API backend. Tidak ada UI yang perlu didesain di MVP.

### FR Coverage Map

| FR | Epic | Story |
|---|---|---|
| FR1, FR2, FR3, FR4, FR5, FR6 | Epic 1 | Story 1.2, 1.3 |
| FR7, FR8, FR9, FR10 | Epic 1 | Story 1.3 |
| FR11, FR12, FR14, FR15 | Epic 1 | Story 1.1, 1.2 |
| FR13, FR18 | Epic 1 | Story 1.1 |
| FR16, FR19 | Epic 1 | Story 1.1 |
| FR17 | Epic 2 | Story 2.2 |
| FR20 | Epic 1 | Story 1.4 |
| FR21, FR22 | Epic 2 | Story 2.3 |
| NFR1–NFR9 | Epic 1 | Story 1.3, 1.5 |
| NFR10–NFR12 | Epic 1 | Story 1.2 |
| NFR13–NFR14 | Epic 2 | Story 2.1 |

---

## Epic List

- **Epic 1:** FastAPI Server MVP — Core AI Tutor API (POST /chat + GET /health)
- **Epic 2:** Cloud Deployment & Hardening — Docker + Gemini API fallback + Rate Limiting
- **Epic 3:** Knowledge Expansion — Topik Pengurangan & Perkalian

---

## Epic 1: FastAPI Server MVP — Core AI Tutor API

**Goal:** Membangun REST API server yang dapat dipanggil Unity Sacred Octagon untuk mendapatkan penjelasan pedagogis GASING, berjalan lokal dengan Ollama, dengan math accuracy ≥ 95%.

**Definition of Done:**
- `POST /chat` dan `GET /health` berjalan
- Unity dapat memanggil API dan mendapat respons JSON valid
- Math accuracy ≥ 95% divalidasi via `05_validate.py`
- Server dapat dijalankan dengan `uvicorn app.main:app`

---

### Story 1.1: Setup FastAPI Project & Health Endpoint

As a **developer Sacred Octagon**,
I want a running FastAPI server with a `/health` endpoint,
So that I can verify the AI Tutor service is online before sending chat requests.

**Acceptance Criteria:**

**Given** saya menjalankan `uvicorn app.main:app --host 0.0.0.0 --port 8000`
**When** saya kirim `GET /health`
**Then** server mengembalikan HTTP 200 dengan JSON:
```json
{"status": "ok", "ollama": "connected", "chromadb": "connected", "model": "gemma4:e4b", "chunks_loaded": 35}
```

**Given** Ollama tidak berjalan
**When** saya kirim `GET /health`
**Then** server mengembalikan HTTP 200 dengan `"ollama": "disconnected"` (tidak crash)

**Given** server baru saja distart
**When** saya kirim `GET /health`
**Then** response time ≤ 500 ms (NFR3)

**Technical Notes:**
- Buat struktur `api/` di root project: `api/main.py`, `api/routers/chat.py`, `api/routers/health.py`
- CORS middleware: `allow_origins=["*"]` untuk v1
- ChromaDB collection di-load saat startup (`@asynccontextmanager` lifespan)
- Cek Ollama dengan `ollama.list()` di health check

---

### Story 1.2: Implement POST /chat Endpoint (Skeleton)

As a **developer Sacred Octagon**,
I want a `/chat` endpoint yang menerima query dan mengembalikan respons JSON valid,
So that saya dapat mengintegrasikan API ke Unity tanpa menunggu RAG selesai.

**Acceptance Criteria:**

**Given** saya kirim `POST /chat` dengan body `{"query": "47 + 8 berapa?"}`
**When** endpoint diproses
**Then** server mengembalikan HTTP 200 dengan JSON yang mengandung field: `response`, `topik_terdeteksi`, `chunks_digunakan`, `latency_ms`

**Given** saya kirim `POST /chat` dengan body `{"query": ""}`
**When** endpoint diproses
**Then** server mengembalikan HTTP 422 dengan pesan error JSON (bukan HTML)

**Given** saya kirim `POST /chat` tanpa field `query`
**When** endpoint diproses
**Then** server mengembalikan HTTP 422 dengan pesan error JSON

**Given** Unity WebGL mengirim request dengan header `Origin: null`
**When** server menerima request
**Then** response mengandung CORS headers yang valid (NFR12)

**Technical Notes:**
- Pydantic model: `ChatRequest(query: str, soal_context: str = None, mode: str = "B", filter_topik: str = None)`
- Pydantic model: `ChatResponse(response: str, topik_terdeteksi: str, chunks_digunakan: list, latency_ms: int)`
- Di story ini, `response` boleh hardcoded/stub — RAG diintegrasikan di Story 1.3

---

### Story 1.3: Integrate RAG Pipeline ke POST /chat

As a **siswa SD yang bermain Sacred Octagon**,
I want the AI Tutor to answer my math question using GASING method,
So that I understand how to solve the problem, not just get the answer.

**Acceptance Criteria:**

**Given** saya kirim `POST /chat` dengan `{"query": "berapa 25 + 7?", "soal_context": "25 + 7"}`
**When** RAG pipeline dijalankan
**Then** response berisi penjelasan GASING dengan langkah konkret (menyebut "lirik kanan" atau "puluhan" atau "satuan")
**And** `chunks_digunakan` mengandung minimal 1 chunk yang relevan (misalnya "J60_c")
**And** response TIDAK berisi jawaban saja tanpa penjelasan (FR4)

**Given** saya kirim pertanyaan filosofi `{"query": "kenapa anak takut matematika?"}`
**When** RAG pipeline dijalankan
**Then** response menggunakan chunks filosofi (F05 atau F06)
**And** topik_terdeteksi = "filosofi_gasing"

**Given** RAG berhasil retrieve chunks
**When** Gemma menghasilkan response
**Then** latency_ms ≤ 30000 (30 detik) untuk Ollama lokal (NFR1)

**Given** `filter_topik: "penjumlahan"` dikirim
**When** RAG retrieve chunks
**Then** hanya chunks dengan kategori "penjumlahan" atau "shared" yang digunakan (FR8)

**Technical Notes:**
- Import `retrieve_chunks` dari `scripts/utils.py` (atau copy ke `api/`)
- System prompt: ekstrak dari `scripts/03_chat.py` (SYSTEM_PROMPT constant)
- Gunakan `ollama.chat()` dengan `stream=False` untuk API (bukan streaming CLI)
- Hitung `latency_ms` dari awal hingga response diterima

---

### Story 1.4: Input Validation & Error Handling

As a **developer Sacred Octagon**,
I want the API to return clear JSON error messages for all failure cases,
So that Unity can display appropriate feedback to the student.

**Acceptance Criteria:**

**Given** query kurang dari 3 karakter
**When** `POST /chat` diproses
**Then** HTTP 422 dengan JSON `{"detail": "Query terlalu pendek (minimum 3 karakter)"}`

**Given** query lebih dari 500 karakter
**When** `POST /chat` diproses
**Then** HTTP 422 dengan JSON `{"detail": "Query terlalu panjang (maksimum 500 karakter)"}`

**Given** Ollama tidak merespons (timeout)
**When** `POST /chat` diproses
**Then** HTTP 503 dengan JSON `{"detail": "AI Tutor sedang tidak tersedia. Coba lagi dalam beberapa detik."}` (FR15)

**Given** ChromaDB tidak dapat diakses
**When** `POST /chat` diproses
**Then** HTTP 503 dengan JSON `{"detail": "Knowledge base tidak tersedia."}` (NFR7)

**Technical Notes:**
- Gunakan FastAPI exception handlers (`@app.exception_handler`)
- Jangan pernah return HTML error (default Starlette behaviour harus di-override)
- Timeout Ollama: 60 detik

---

### Story 1.5: Validation Test — Math Accuracy

As a **project owner (Yohanes)**,
I want to verify the FastAPI-wrapped RAG achieves ≥ 95% math accuracy,
So that I can confirm the API integration doesn't degrade the validated baseline.

**Acceptance Criteria:**

**Given** server berjalan di `localhost:8000`
**When** saya jalankan `python scripts/05_validate.py --mode api --base-url http://localhost:8000`
**Then** accuracy ≥ 95% (40 test cases)
**And** tidak ada test case dengan jawaban matematika yang salah sama sekali

**Given** hasil validasi selesai
**When** saya review output
**Then** format report sama dengan validasi CLI sebelumnya (JSON + summary)

**Technical Notes:**
- Tambahkan flag `--mode api` ke `05_validate.py` yang memanggil `POST /chat` via HTTP alih-alih langsung memanggil utils.py
- Bandingkan hasil dengan baseline CLI (100% = 40/40)

---

## Epic 2: Cloud Deployment & Hardening

**Goal:** Deploy gasing-rag ke cloud (Docker + Gemini API), tambahkan rate limiting dan API key authentication, sehingga Sacred Octagon bisa diakses dari sekolah yang punya internet.

**Definition of Done:**
- Docker image dapat dijalankan lokal dan di cloud
- Gemini API berfungsi sebagai fallback Ollama
- Rate limiting aktif (10 req/menit per IP)

---

### Story 2.1: Dockerize FastAPI Server

As a **developer Sacred Octagon**,
I want a Docker image untuk gasing-rag,
So that kita dapat deploy ke cloud platform tanpa setup manual.

**Acceptance Criteria:**

**Given** saya jalankan `docker build -t gasing-rag .`
**When** build selesai
**Then** image berhasil dibuat tanpa error

**Given** saya jalankan `docker run -p 8000:8000 gasing-rag`
**When** container berjalan
**Then** `GET /health` merespons HTTP 200

**Technical Notes:**
- `Dockerfile` di root project
- Multi-stage build untuk minimalisir image size
- ChromaDB dan model di-mount via volume untuk persistence
- Environment variables: `OLLAMA_HOST`, `CHROMA_PATH`, `MODEL_NAME`

---

### Story 2.2: Gemini API Fallback

As a **sekolah dengan koneksi internet**,
I want the AI Tutor to use Gemini API when Ollama is not available,
So that siswa tetap bisa dapat bantuan meskipun Ollama tidak terinstall.

**Acceptance Criteria:**

**Given** environment variable `GEMINI_API_KEY` di-set
**When** `POST /chat` diproses
**Then** sistem menggunakan Gemini API jika Ollama tidak tersedia (FR17)

**Given** Gemini API digunakan
**When** response diterima
**Then** latency_ms ≤ 15000 (15 detik) (NFR2)

**Technical Notes:**
- Library: `google-generativeai`
- Fallback logic: coba Ollama dulu → jika gagal/timeout → pakai Gemini
- Model: `gemini-2.0-flash` atau `gemini-1.5-flash`

---

### Story 2.3: Rate Limiting & API Key Auth

As a **system administrator**,
I want rate limiting and API key validation,
So that API tidak bisa diakses sembarangan atau di-spam.

**Acceptance Criteria:**

**Given** 1 IP mengirim > 10 request dalam 1 menit
**When** request ke-11 diterima
**Then** HTTP 429 dengan JSON `{"detail": "Terlalu banyak request. Coba lagi dalam 1 menit."}` (FR21)

**Given** request tanpa header `X-API-Key` yang valid
**When** `POST /chat` diproses
**Then** HTTP 401 dengan JSON `{"detail": "API key tidak valid"}` (FR22)

**Technical Notes:**
- Library: `slowapi` untuk rate limiting
- API keys: simpan di environment variable atau `.env` file (bukan database)

---

## Epic 3: Knowledge Expansion — Pengurangan & Perkalian

**Goal:** Tambahkan topik pengurangan dan perkalian ke knowledge base, sehingga AI Tutor bisa membantu siswa di lebih banyak soal Sacred Octagon.

**Definition of Done:**
- Chunks pengurangan ter-index di ChromaDB
- Chunks perkalian ter-index di ChromaDB
- `POST /chat` bisa jawab soal pengurangan dan perkalian
- Validasi accuracy ≥ 95% untuk masing-masing topik

---

### Story 3.1: Chunks Pengurangan — Knowledge Base

As a **siswa yang kesulitan soal pengurangan**,
I want the AI Tutor to explain subtraction using GASING method,
So that I understand the step-by-step process.

**Acceptance Criteria:**

**Given** saya tanya `{"query": "75 - 28 berapa?"}`
**When** RAG dijalankan
**Then** response menjelaskan metode GASING untuk pengurangan
**And** `chunks_digunakan` mengandung chunk kategori "pengurangan"

**Technical Notes:**
- Buat chunks pengurangan di `chunks/per_jenis/` (format sama dengan J-series)
- Sumber: `Sources/converted/` volume yang membahas pengurangan
- Re-ingest dengan `rebuild-gasing` alias

---

### Story 3.2: Chunks Perkalian — Knowledge Base

As a **siswa yang kesulitan soal perkalian**,
I want the AI Tutor to explain multiplication using GASING method,
So that I understand how to multiply quickly.

**Acceptance Criteria:**

**Given** saya tanya `{"query": "7 x 8 berapa?"}`
**When** RAG dijalankan
**Then** response menjelaskan metode GASING untuk perkalian
**And** `chunks_digunakan` mengandung chunk kategori "perkalian"

**Technical Notes:**
- Buat chunks perkalian di `chunks/per_jenis/`
- Sumber: `Sources/Perkalian.md` yang sudah ada di project

---

*Dokumen ini dibuat dengan BMAD Create Epics and Stories Skill v6.6.0*  
*Next: `bmad-sprint-planning` untuk generate sprint plan*
