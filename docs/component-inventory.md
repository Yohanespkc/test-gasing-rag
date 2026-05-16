# Inventori Komponen: gasing-rag

**Versi:** 1.0.0
**Tanggal Dokumen:** 2026-05-17

---

## 1. Knowledge Base Chunks (22 chunks)

### 1.1 Chunks Shared (5 chunks)

Chunks ini berisi konsep pedagogik GASING yang berlaku lintas jenis soal. Di-include via mekanisme `konsep_terkait` di frontmatter.

| ID | File | Kompleksitas | Fungsi |
|---|---|---|---|
| S01_konfigurasi_jari | `shared/S01_konfigurasi_jari.md` | Dasar | Konfigurasi menghitung dengan jari, mapping angka → jari |
| S02_komutativitas | `shared/S02_komutativitas.md` | Dasar | Template penutup komutativitas: "kalau dibalik hasilnya sama" |
| S03_format_mencongak_universal | `shared/S03_format_mencongak_universal.md` | Dasar | Format output mode Mencongak (jawaban + alasan singkat) |
| S04_format_dua_cara | `shared/S04_format_dua_cara.md` | Dasar | Format presentasi dua cara untuk soal tertentu |
| S05_aturan_1_kecil | `shared/S05_aturan_1_kecil.md` | Dasar | Aturan dan notasi ₁ (1-kecil) untuk carry dalam GASING |

### 1.2 Chunks Per Jenis (17 chunks)

| ID | File | Jenis Soal | Pola | punya_carry | punya_cascade | Kompleksitas |
|---|---|---|---|---|---|---|
| J00_nol | `per_jenis/J00_nol.md` | Nol | X + 0 atau 0 + X | false | false | Dasar |
| J10_a1 | `per_jenis/J10_a1.md` | A1 | 1d+1d, hasil 1–5 | false | false | Dasar |
| J20_a2 | `per_jenis/J20_a2.md` | A2 | 1d+1d, hasil 6–10 | false | false | Dasar |
| J30_b1 | `per_jenis/J30_b1.md` | B1 | 10 + X | false | false | Dasar |
| J40_b2 | `per_jenis/J40_b2.md` | B2 | X + 10 | false | false | Dasar |
| J50_b3 | `per_jenis/J50_b3.md` | B3 | 1d+1d, hasil 11–19 | true | false | Menengah |
| J60_c | `per_jenis/J60_c.md` | C | 2d+1d | true | false | Menengah |
| J70_d | `per_jenis/J70_d.md` | D | maks 2d (2d+2d / 1d+2d) | true | false | Menengah |
| J81_e_tanpa_carry | `per_jenis/J81_e_tanpa_carry.md` | E | 3d, tanpa carry | false | false | Menengah |
| J82_e_carry_satuan_puluhan | `per_jenis/J82_e_carry_satuan_puluhan.md` | E | 3d, carry di satuan/puluhan | true | false | Tinggi |
| J83_e_cascade_1_kecil | `per_jenis/J83_e_cascade_1_kecil.md` | E | 3d, cascade 1-kecil | true | true | Tinggi |
| J91_f_pengantar_aturan | `per_jenis/J91_f_pengantar_aturan.md` | F | 4d+, pengantar aturan umum | — | — | Tinggi |
| J92_f_alignment_digit | `per_jenis/J92_f_alignment_digit.md` | F | 4d+, alignment kolom | — | — | Tinggi |
| J93_f_belajar_simple | `per_jenis/J93_f_belajar_simple.md` | F | 4d+, belajar tanpa carry | false | false | Tinggi |
| J94_f_belajar_cascade | `per_jenis/J94_f_belajar_cascade.md` | F | 4d+, belajar dengan cascade | true | true | Sangat Tinggi |
| J95_f_belajar_diff_digits | `per_jenis/J95_f_belajar_diff_digits.md` | F | 4d+, operand beda digit | true | true | Sangat Tinggi |
| J96_f_mencongak | `per_jenis/J96_f_mencongak.md` | F | 4d+, mode mencongak | — | — | Sangat Tinggi |

---

## 2. Pipeline Scripts

### 2.1 Core Pipeline

| Script | Entry Point | Fungsi | Dependensi |
|---|---|---|---|
| `utils.py` | (library) | Semua helper function — load, embed, retrieve, format, classify | chromadb, ollama |
| `01_ingest.py` | `main()` | Parse .md → embed → ChromaDB insert | utils.py |
| `02_query.py` | `main()` | Test retrieval standalone CLI | utils.py |
| `03_chat.py` | `chat_loop()` | Interactive chat dengan RAG pipeline | utils.py, ollama |
| `05_validate.py` | `main()` | Automated 40-case validation | utils.py, ollama |

### 2.2 Content Generation Scripts

| Script | Fungsi | Output |
|---|---|---|
| `generate_shared_chunks.py` | Regenerasi 5 shared chunks | `chunks/shared/*.md` |
| `generate_per_jenis_small.py` | Regenerasi chunks Nol–D | `chunks/per_jenis/J00–J70*.md` |
| `generate_per_jenis_complex.py` | Regenerasi chunks E dan F | `chunks/per_jenis/J81–J96*.md` |
| `generate_aux_files.py` | Regenerasi file pendukung (index, dll.) | `chunks_index.json` dll |

### 2.3 Fungsi Kunci di utils.py

| Fungsi | Signature | Peran |
|---|---|---|
| `classify_soal` | `(text: str) → str\|None` | Rule-based classifier → Jenis soal |
| `embed` | `(text: str) → list[float]` | Ollama embedding → 768-dim vector |
| `retrieve_chunks` | `(query, top_k, expand_shared, filter_topik, use_rule_based) → list` | Hybrid retrieval engine |
| `format_context` | `(chunks: list) → str` | Format chunks → string konteks |
| `load_chunks` | `() → list` | Load + parse semua .md dari disk |
| `parse_frontmatter` | `(content: str) → (dict, str)` | Parse YAML frontmatter + body |
| `flatten_metadata` | `(m: dict) → dict` | Serialize list → string untuk ChromaDB |
| `load_system_prompt` | `() → str` | Load system_prompt.txt |

---

## 3. Konfigurasi

| File | Fungsi | Dipakai Oleh |
|---|---|---|
| `system_prompt.txt` | SYSTEM prompt runtime (suntik via Python) | `03_chat.py`, `05_validate.py` |
| `system_prompt_v44_ramping.md` | SYSTEM prompt versi dokumentasi (referensi) | Manual review |
| `Model-gasing-rag.modelfile` | Custom Ollama modelfile (embed SYSTEM + parameter) | `ollama create gasing-rag` |
| `requirements.txt` | Python dependencies | `pip install` |
| `chunks_index.json` | Metadata index semua chunks | Referensi / tooling |
| `_bmad/config.toml` | BMAD project configuration | BMAD tooling |

---

## 4. Data Stores

| Store | Lokasi | Teknologi | Isi | Dikelola Oleh |
|---|---|---|---|---|
| Vector Store | `chroma_db/` | ChromaDB (persistent) | 22 chunk embeddings + metadata | `01_ingest.py` |
| Knowledge Base | `chunks/` | Markdown files | 22 file .md pedagogik GASING | Manual + generate scripts |
| Validation Results | `scripts/validation_report.json` | JSON | Hasil 40 test cases terakhir | `05_validate.py` |
| Validation Log | `scripts/validation_log.txt` | Plain text | Full Gemma responses | `05_validate.py` |

---

## 5. Graf Dependensi Chunks (konsep_terkait)

```
J00_nol          → (tidak ada shared dependency)
J10_a1           → S01_konfigurasi_jari
J20_a2           → S01_konfigurasi_jari
J30_b1           → S01_konfigurasi_jari
J40_b2           → S01_konfigurasi_jari
J50_b3           → S01_konfigurasi_jari, S02_komutativitas (implied)
J60_c            → S02_komutativitas, S03_format_mencongak_universal
J70_d            → S02_komutativitas, S04_format_dua_cara
J81_e_*          → S05_aturan_1_kecil, S03_format_mencongak_universal
J82_e_*          → S05_aturan_1_kecil, S03_format_mencongak_universal
J83_e_*          → S05_aturan_1_kecil
J91-J96_f_*      → S05_aturan_1_kecil, S03_format_mencongak_universal, S04_format_dua_cara
```

*Catatan: Graf eksak ada di field `konsep_terkait` di setiap frontmatter chunk.*

---

## 6. Mapping Jenis → Chunks (JENIS_TO_CHUNKS)

```python
{
    "Nol": ["J00_nol"],
    "A1":  ["J10_a1"],
    "A2":  ["J20_a2"],
    "B1":  ["J30_b1"],
    "B2":  ["J40_b2"],
    "B3":  ["J50_b3"],
    "C":   ["J60_c"],
    "D":   ["J70_d"],
    "E":   ["J81_e_tanpa_carry", "J82_e_carry_satuan_puluhan", "J83_e_cascade_1_kecil"],
    "F":   ["J91_f_pengantar_aturan", "J92_f_alignment_digit", "J93_f_belajar_simple",
            "J94_f_belajar_cascade", "J95_f_belajar_diff_digits", "J96_f_mencongak"],
}
```

Jenis E dan F punya **multiple chunks** karena terdapat sub-kasus yang berbeda (tanpa carry, dengan carry, cascade).
