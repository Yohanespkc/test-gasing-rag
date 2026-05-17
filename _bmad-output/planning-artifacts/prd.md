---
stepsCompleted: ['step-01-init', 'step-02-discovery', 'step-02b-vision', 'step-02c-executive-summary', 'step-03-success', 'step-04-journeys', 'step-05-domain', 'step-06-innovation', 'step-07-project-type', 'step-08-scoping', 'step-09-functional', 'step-10-nonfunctional', 'step-11-polish', 'step-12-complete']
releaseMode: 'phased'
inputDocuments:
  - '_bmad-output/planning-artifacts/product-brief.md'
  - 'docs/architecture.md'
  - 'docs/development-guide.md'
  - 'docs/component-inventory.md'
  - 'docs/source-tree-analysis.md'
workflowType: 'prd'
briefCount: 1
researchCount: 0
projectDocsCount: 4
classification:
  projectType: 'API Service + Integration Layer'
  domain: 'EdTech - K6 Mathematics Indonesia'
  complexity: 'high'
  projectContext: 'brownfield'
---

# Product Requirements Document - gasing-rag

**Author:** Yohanes  
**Date:** 2026-05-17  

---

## Executive Summary

**gasing-rag** adalah AI Tutor Engine berbasis RAG (Retrieval-Augmented Generation) yang mengintegrasikan Metode GASING ke dalam game edukasi Sacred Octagon. Engine ini dirancang untuk hadir secara real-time ketika siswa SD mengalami kesulitan matematis di dalam game — memberikan bimbingan pedagogis yang otentik, hangat, dan terbukti efektif.

Target pengguna: **siswa SD kelas 1–6** (usia 6–12 tahun) yang bermain Sacred Octagon, dan **guru** yang membutuhkan alat bantu pedagogis berbasis AI yang selaras dengan Metode GASING. Deployment menjangkau sekolah offline (Ollama lokal) hingga sekolah dengan koneksi internet (Gemini API cloud).

### Apa yang Membuatnya Spesial

Pasar AI tutoring dipenuhi oleh sistem yang memberi **jawaban** — gasing-rag memberi **pemahaman**. Tiga diferensiasi utama:

1. **Pedagogis berbasis bukti ilmiah** — bukan AI generik, tapi distilasi dari Metode GASING yang memiliki effect size 5.06 dari 23.633 siswa di 127 kabupaten/kota Indonesia. Setiap respons mengikuti alur Konkret → Abstrak → Mencongak.

2. **Konteks-aware dan in-game** — menerima soal aktif dari Sacred Octagon sebagai konteks, sehingga bantuan yang diberikan tepat sasaran tanpa memutus pengalaman bermain.

3. **Dibuat untuk Indonesia** — bahasa Indonesia, referensi budaya lokal (jari, apel, kelereng), dan berakar pada pengalaman nyata anak-anak di pedalaman Papua hingga Aceh.

## Klasifikasi Project

| Dimensi | Nilai |
|---|---|
| **Project Type** | API Service + Integration Layer |
| **Domain** | EdTech — Matematika SD Indonesia |
| **Complexity** | Tinggi (LLM pipeline + game integration + dual deployment) |
| **Context** | Brownfield — RAG v1.0.0 sudah ada, membangun lapisan API di atasnya |

---

## Success Criteria

### User Success

- Siswa yang minta bantuan **mengerti dan bisa lanjut bermain** dalam 1 sesi tanya-jawab (≤ 3 exchange)
- Respons tutor **tidak pernah memberi jawaban langsung** — selalu mengajar cara berpikir GASING
- Siswa **tidak perlu keluar dari Sacred Octagon** untuk mendapat bantuan (seamless in-game)
- Respons dalam **Bahasa Indonesia yang mudah dipahami anak SD** (divalidasi oleh guru)

### Business Success

- **v1 (3 bulan):** API `POST /chat` berjalan dan berhasil dipanggil oleh Unity Sacred Octagon dalam integration test pertama
- **v1.5 (6 bulan):** Digunakan di minimal **5 sekolah pilot** dalam sesi Sacred Octagon nyata
- **v2 (12 bulan):** Mendukung **3 topik matematika** (penjumlahan, pengurangan, perkalian) dan berjalan di cloud

### Technical Success

- **Math accuracy ≥ 95%** (baseline sudah 100% untuk penjumlahan)
- **Response time ≤ 30 detik** (Ollama lokal) / **≤ 15 detik** (Gemini API cloud)
- **Zero wrong answers** — lebih baik tidak menjawab daripada salah
- API tersedia untuk dipanggil **Unity via UnityWebRequest** tanpa perlu library tambahan

### Measurable Outcomes

| Metrik | Target v1 | Target v2 |
|---|---|---|
| API response time (lokal) | ≤ 30 detik | ≤ 30 detik |
| API response time (cloud) | — | ≤ 15 detik |
| Math accuracy | ≥ 95% | ≥ 95% |
| Topik matematika didukung | 1 (penjumlahan) | 3 |
| Sekolah pilot | 0 | 5 |

## Product Scope

### MVP — Minimum Viable Product

- `POST /chat` endpoint (FastAPI)
- `GET /health` endpoint
- Integrasi RAG: retrieve chunks → format context → call Gemma
- Support teks bebas dari siswa + opsional `soal_context`
- CORS untuk Unity WebGL
- Deployment lokal: Ollama + uvicorn

### Growth Features (Post-MVP)

- Cloud deployment (Docker + Gemini API fallback)
- Support topik pengurangan dan perkalian
- Session context: tutor ingat soal-soal dalam 1 sesi bermain
- Rate limiting & basic auth untuk keamanan API

### Vision (Future)

- Multimodal: siswa foto tulisan tangan → tutor analisis
- Teacher dashboard: log siapa bertanya apa, topik mana yang paling banyak kesulitan
- Adaptive difficulty: tutor tahu progress siswa dan sesuaikan penjelasan
- 10 topik matematika SD lengkap

---

## User Journeys

### Journey 1 — Siswa: Tersandung Soal (Happy Path)

**Persona:** Arif, 9 tahun, kelas 3 SD di Merauke, Papua. Baru pertama kali pakai Sacred Octagon di sekolahnya.

**Opening Scene:** Arif sedang di mode "Asyiknya Berpetualang" — karakternya baru sampai di gerbang kastil. Misi: kalahkan penjaga dengan menjawab 47 + 8. Ia mengetik 53. Salah. Lagi: 51. Salah lagi. Tombol "Minta Bantuan" muncul.

**Rising Action:** Arif ragu sebentar — takut kelihatan bodoh. Tapi ia klik tombol itu. Muncul chat box di pinggir layar: *"Hai Arif! Boleh aku bantu?"* Arif ketik: *"47 + 8 berapa?"*

**Climax:** gasing-rag menjawab: *"Oke! 47 itu 4 puluhan dan 7 satuan. Lirik kanan: 7 + 8 = 15, lebih dari 10. Jadi puluhannya naik jadi 5. Satuannya sisa 5. Jawaban: 55!"* Arif mencoba lagi di game. 55. **Benar!** Gerbang kastil terbuka.

**Resolution:** Arif melanjutkan petualangan. Keesokan harinya ia ingat "lirik kanan" tanpa bantuan.

*Capabilities revealed: POST /chat, context-aware response, bahasa anak SD*

---

### Journey 2 — Siswa: Edge Case (Berulang Tidak Mengerti)

**Persona:** Sari, 7 tahun, kelas 1. Soal: 9 + 5. Sudah tanya tutor 3 kali, masih belum mengerti.

**Challenge:** Sari ketik: *"masih ga ngerti"*. Tutor mendeteksi ini lanjutan sesi yang sama. Alih-alih mengulang penjelasan verbal yang sama, tutor ganti pendekatan kinestetik: *"Oke, kita pakai jari ya! Tunjukkan 9 jari dulu..."*

*Capabilities revealed: Multi-turn session context, variasi strategi pedagogis per jalur multimodal*

---

### Journey 3 — Developer Sacred Octagon (Integrasi API)

**Persona:** Budi, developer Unity dari tim Sacred Octagon.

**Opening Scene:** Budi butuh implementasi tombol "Minta Bantuan" yang memanggil gasing-rag dari Unity.

**Journey:** Budi test `GET /health` → OK. Lalu `POST /chat` dengan Postman: kirim `{"query": "47 + 8 berapa?", "soal_context": "47 + 8"}`. Dapat JSON response dalam 12 detik. Implementasi di Unity dengan UnityWebRequest + coroutine. Integration test pertama: **berhasil**.

**Resolution:** Sacred Octagon kini punya AI Tutor yang callable dari dalam game.

*Capabilities revealed: JSON API contract, response time predictable, CORS headers, GET /health*

---

### Journey 4 — Guru: Monitoring (v2)

**Persona:** Bu Ratna, guru SD kelas 4 Makassar yang memantau siswa bermain Sacred Octagon.

**v1:** Bu Ratna observasi langsung — ia perhatikan 3 siswa sering klik "Minta Bantuan" untuk soal dua digit.

**v2:** Bu Ratna buka teacher dashboard. Arif bertanya 5x tentang jenis C, Sari 8x tentang jenis A2. Bu Ratna tahu: perlu drilling lebih di topik itu minggu depan.

*Capabilities revealed (v2): Request logging, teacher dashboard, aggregasi per siswa dan topik*

---

### Journey Requirements Summary

| Capability | MVP | Growth | Vision |
|---|---|---|---|
| `POST /chat` endpoint | ✅ | ✅ | ✅ |
| `GET /health` endpoint | ✅ | ✅ | ✅ |
| Context-aware (soal aktif) | ✅ | ✅ | ✅ |
| JSON API + CORS | ✅ | ✅ | ✅ |
| Response time < 30 detik | ✅ | ✅ | ✅ |
| Multi-turn session context | ⬜ | ✅ | ✅ |
| Variasi strategi pedagogis | ⬜ | ✅ | ✅ |
| Request logging | ⬜ | ✅ | ✅ |
| Teacher dashboard | ⬜ | ⬜ | ✅ |

---

## Domain-Specific Requirements

### Compliance & Regulatory

- **Tidak ada regulasi ketat** (HIPAA/GDPR) untuk v1 — produk edukasi tanpa data sensitif
- **Perlindungan data anak (PDPA Indonesia):** Sistem tidak boleh simpan nama asli siswa tanpa consent. Di v1 (no auth, no logging) ini otomatis terpenuhi
- **Zero PII di v1:** API tidak menerima nama, NIK, atau identitas siswa — hanya teks pertanyaan

### Technical Constraints

- **Bahasa:** Semua respons **wajib Bahasa Indonesia** — tidak boleh campur bahasa Inggris dalam penjelasan matematika
- **Pedagogis:** Sistem **tidak boleh memberi jawaban langsung** tanpa penjelasan — ini constraint domain, bukan sekadar teknis
- **Akurasi zero-tolerance:** Lebih baik *"aku belum bisa bantu soal ini"* daripada jawaban keliru yang merusak konsep anak
- **Offline-first:** Deployment lokal harus berjalan **tanpa internet** (Ollama lokal)
- **Low-spec hardware:** API harus ringan di sisi client, tidak butuh GPU di Unity

### Integration Requirements

- **Unity → FastAPI:** UnityWebRequest (HTTP/1.1), timeout 60 detik, response JSON
- **Ollama:** Lokal port 11434, model `gemma4:e4b`
- **Gemini API (v2):** Google AI Studio key, model gemini-2.0-flash atau equivalent
- **ChromaDB:** Lokal, tidak butuh jaringan

### Risk Mitigations

| Risiko | Mitigasi |
|---|---|
| Gemma jawab salah (halusinasi) | RAG + system prompt ketat + validasi chunk penjumlahan |
| Ollama lambat di hardware tua | Timeout 60 detik, loading indicator di Unity |
| Koneksi putus di cloud mode | Fallback ke Ollama lokal, graceful error message |
| Siswa salah paham respons | Response selalu konkret (jari, analogi), bukan abstrak saja |
| API spam (banyak siswa bersamaan) | Rate limiting di growth phase, connection pooling uvicorn |

---

## Innovation & Novel Patterns

### Detected Innovation Areas

1. **RAG + Pedagogi Berbasis Bukti** — Menggabungkan RAG dengan metodologi pengajaran tervalidasi ilmiah (effect size 5.06). Mayoritas AI tutor pakai prompting generik; gasing-rag pakai knowledge base terstruktur dari domain expert nyata.

2. **In-Game AI Tutor Context-Aware** — Tutor AI yang menerima konteks soal aktif dari game engine dan merespons dalam konteks tersebut, tanpa memutus pengalaman bermain.

3. **Offline-First AI untuk Sekolah Terpencil** — Deployment Ollama lokal memungkinkan AI Tutor berfungsi tanpa internet di Papua, NTT, dll. Mengatasi digital divide yang diabaikan EdTech arus utama.

4. **Dual-Topic RAG** — Satu engine melayani query matematika (konkret) dan filosofi pedagogis (mengapa metode ini berhasil), dengan retrieval cerdas yang memisahkan konteks.

### Market Context & Competitive Landscape

- **AI Tutor global** (Khanmigo, Duolingo Max, Photomath): Semua bergantung cloud, zero offline-first untuk pasar terpencil
- **EdTech Indonesia** (Ruangguru, Zenius): Fokus konten video, bukan AI tutor adaptif real-time
- **Celah:** Tidak ada produk yang mengkombinasikan game edukasi + AI tutor pedagogis berbasis bukti + offline-first untuk konteks Indonesia

### Validation Approach

- **Math accuracy:** Sudah tervalidasi 100% (40 test cases) — baseline terkuat
- **Pedagogy fidelity:** Validasi kualitatif oleh guru GASING yang review sampel respons
- **Integration test:** Unity team call API, verifikasi response time dan format
- **Pilot test:** 5 sekolah, observe apakah siswa yang dapat bantuan tutor lebih berhasil lanjut level berikutnya

### Risk Mitigation Inovasi

| Risiko | Mitigasi |
|---|---|
| Gemma tidak cukup pintar untuk pedagogik | RAG meminimalisir hallucination; system prompt ketat |
| Offline Ollama terlalu lambat | Cache common responses; async loading indicator |
| Unity-FastAPI latency terlalu tinggi | Target < 30 detik; streaming response jika > 10 detik |


---

## API Service Specific Requirements

### Project-Type Overview

gasing-rag v1 adalah **stateless REST API** berbasis FastAPI. Setiap request berdiri sendiri — tidak ada session server-side di MVP. Unity mengirim pertanyaan siswa, server merespons dengan penjelasan pedagogis GASING, Unity menampilkannya di game.

### API Endpoint Specification

**POST /chat — Endpoint Utama**
```json
Request:
{
  "query": "47 + 8 berapa?",
  "soal_context": "47 + 8",
  "mode": "B",
  "filter_topik": null
}

Response 200:
{
  "response": "Oke! 47 itu 4 puluhan...",
  "topik_terdeteksi": "penjumlahan",
  "chunks_digunakan": ["J60_c", "S05_aturan_1_kecil"],
  "latency_ms": 8420
}
```

**GET /health — Health Check**
```json
Response 200:
{
  "status": "ok",
  "ollama": "connected",
  "chromadb": "connected",
  "model": "gemma4:e4b",
  "chunks_loaded": 35
}
```

### Authentication Model

- **v1 (MVP):** Tanpa autentikasi — open di jaringan lokal sekolah
- **v2 (Growth):** API key di header `X-API-Key`
- **v3 (Vision):** JWT per institusi untuk audit logging

### Technical Architecture Considerations

- **Async handlers:** FastAPI async untuk non-blocking Ollama calls
- **Timeout:** 60 detik Ollama / 20 detik Gemini API
- **Error format:** Semua error return JSON (bukan HTML) — Unity tidak bisa parse HTML
- **Startup:** Pre-load ChromaDB collection saat start, bukan per-request
- **CORS:** Open di v1, restrict per origin di v2

### Implementation Considerations

- **Encoding:** UTF-8 wajib untuk aksara Indonesia
- **Max query:** 500 karakter
- **Rate limiting:** 10 req/menit per IP (v2), 100 req/menit per API key (v2)

---

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach:** Problem-solving MVP — buktikan bahwa Unity bisa memanggil gasing-rag dan mendapat respons pedagogis yang benar.

**Resource Requirements:** 1 developer Python (Yohanes), koordinasi dengan 1 developer Unity (tim Sacred Octagon).

### MVP Feature Set (Phase 1 — v1, target 3 bulan)

**Core User Journeys Supported:** Journey 1 (siswa happy path) + Journey 3 (developer integrasi)

**Must-Have Capabilities:**
- `POST /chat` endpoint dengan RAG + Gemma
- `GET /health` endpoint
- CORS untuk Unity WebGL
- Response JSON dengan `response`, `topik_terdeteksi`, `chunks_digunakan`
- Math accuracy ≥ 95% (penjumlahan)
- Deployment lokal: Ollama + uvicorn

### Post-MVP Features

**Phase 2 — v2 (Growth, target 6–12 bulan):**
- Cloud deployment: Docker + Gemini API fallback
- Topik pengurangan dan perkalian
- API key authentication
- Rate limiting
- Basic request logging

**Phase 3 — v3 (Vision):**
- Multimodal input (foto soal tulisan tangan)
- Teacher dashboard
- Session context (multi-turn memory)
- 10 topik matematika SD

### Risk Mitigation Strategy

**Technical Risks:** RAG + system prompt ketat meminimalisir Gemma hallucination; timeout 60 detik prevent hanging  
**Market Risks:** Pilot 5 sekolah sebagai validasi sebelum scale  
**Resource Risks:** MVP sangat lean — 2 endpoint, 1 developer, bisa selesai dalam 3 bulan

---

## Functional Requirements

### Tutor Interaction (Core)

- FR1: Siswa dapat mengirim pertanyaan matematika dalam teks bebas Bahasa Indonesia
- FR2: Sistem dapat menerima konteks soal aktif (opsional) dari Sacred Octagon bersama pertanyaan
- FR3: Sistem memberikan penjelasan pedagogis GASING yang mengikuti alur Konkret → Abstrak → Mencongak
- FR4: Sistem tidak pernah memberikan jawaban langsung tanpa penjelasan proses
- FR5: Sistem mendeteksi topik matematika dari pertanyaan dan mengambil chunks yang relevan
- FR6: Sistem merespons dalam Bahasa Indonesia yang sesuai untuk siswa SD (kelas 1–6)

### RAG & Knowledge Retrieval

- FR7: Sistem dapat meretrieve knowledge chunks berdasarkan semantic similarity query
- FR8: Sistem dapat memfilter chunks berdasarkan topik (penjumlahan / filosofi_gasing / semua)
- FR9: Sistem menyertakan shared chunks (konfigurasi jari, aturan 1-kecil) secara otomatis untuk soal relevan
- FR10: Sistem dapat menampilkan daftar chunks yang digunakan dalam response (untuk debug)

### API & Integration

- FR11: Sacred Octagon (Unity) dapat memanggil endpoint `/chat` via HTTP POST
- FR12: Sistem mengembalikan respons dalam format JSON yang dapat diparse Unity
- FR13: Sacred Octagon dapat memeriksa status sistem via endpoint `/health`
- FR14: Sistem mendukung CORS untuk memungkinkan request dari Unity WebGL
- FR15: Sistem mengembalikan pesan error dalam format JSON (bukan HTML) untuk semua kasus gagal

### Deployment & Operasional

- FR16: Sistem dapat berjalan sepenuhnya offline menggunakan Ollama lokal (tanpa internet)
- FR17: Sistem dapat dikonfigurasi untuk menggunakan Gemini API sebagai alternatif Ollama
- FR18: Administrator dapat memeriksa status koneksi Ollama dan ChromaDB via health check
- FR19: Sistem dapat dijalankan dengan perintah tunggal (`uvicorn`) tanpa konfigurasi kompleks

### Keamanan & Kualitas (Growth)

- FR20: Sistem menolak request dengan query kosong atau di bawah panjang minimum
- FR21: Sistem membatasi jumlah request per IP dalam periode waktu tertentu (v2)
- FR22: Sistem memvalidasi API key untuk request dari client yang diizinkan (v2)

---

## Non-Functional Requirements

### Performance

- NFR1: Endpoint `/chat` mengembalikan respons dalam ≤ 30 detik untuk Ollama lokal (gemma4:e4b)
- NFR2: Endpoint `/chat` mengembalikan respons dalam ≤ 15 detik untuk Gemini API cloud
- NFR3: Endpoint `/health` mengembalikan respons dalam ≤ 500 ms
- NFR4: Sistem mendukung minimum 5 concurrent requests tanpa degradasi signifikan (lokal)
- NFR5: ChromaDB collection di-load saat startup — bukan per-request — untuk meminimalisir latency

### Reliability

- NFR6: Sistem mengembalikan HTTP 503 dengan pesan JSON jika Ollama tidak tersedia (bukan crash)
- NFR7: Sistem mengembalikan HTTP 503 dengan pesan JSON jika ChromaDB tidak dapat diakses
- NFR8: Math accuracy ≥ 95% untuk topik penjumlahan (diukur via 05_validate.py — 40 test cases)
- NFR9: Sistem tidak pernah mengembalikan jawaban matematika yang salah tanpa indikasi ketidakpastian

### Integration

- NFR10: Response JSON harus kompatibel dengan Unity `JsonUtility.FromJson` atau `Newtonsoft.Json`
- NFR11: API harus menerima request dalam ≤ 5 detik setelah server startup
- NFR12: CORS headers harus hadir di semua response untuk mendukung Unity WebGL

### Scalability

- NFR13: Arsitektur stateless memungkinkan horizontal scaling tanpa refactoring (v2+)
- NFR14: Penambahan topik matematika baru tidak memerlukan perubahan kode API — hanya tambah chunks

---

## Ringkasan & Langkah Selanjutnya

PRD ini mendefinisikan **Capability Contract** lengkap untuk gasing-rag AI Tutor Engine v1. Semua fitur yang tidak terdaftar di Functional Requirements (FR1–FR22) dianggap **di luar scope** kecuali ada amandemen eksplisit.

### Dokumen Turunan yang Diperlukan

1. **Architecture Document** — desain teknis FastAPI server, dependency injection, error handling
2. **Epics & Stories** — pecahan FR ke user stories yang dapat dikerjakan
3. **API Contract** — dokumen JSON spec untuk koordinasi dengan tim Unity Sacred Octagon

### Status PRD

✅ **SELESAI** — Semua 12 step BMAD `bmad-create-prd` telah dieksekusi.  
📁 **Output:** `_bmad-output/planning-artifacts/prd.md`  
🔜 **Next:** `bmad-create-epics-and-stories`

---

*Dokumen ini dibuat dengan BMAD Create PRD Skill v6.6.0*  
*Untuk dilanjutkan: `bmad-create-epics-and-stories` menggunakan PRD ini sebagai input*
