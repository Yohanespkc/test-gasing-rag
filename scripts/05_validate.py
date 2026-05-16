#!/usr/bin/env python3
"""
05_validate.py - Validasi besar pipeline RAG GASING.

40 test cases (4 per jenis x 10 jenis) dengan auto-checking:
- Classification (rule-based jenis identification)
- Retrieval (chunk benar ada di hasil)
- Math accuracy (extract dari response Gemma, compare dengan expected)
- Format compliance (komutativitas, notasi 1 kecil, lirik kanan, dll)

Cara pakai:
    python 05_validate.py
        Run all 40 cases dengan Gemma, generate report

    python 05_validate.py --quick
        Run cuma classification + retrieval (no Gemma, ~30 detik)

    python 05_validate.py --model gemma4:e4b
        Pilih model spesifik

    python 05_validate.py --limit 10
        Run cuma 10 cases pertama (untuk test cepat)

Output:
    - Console: ringkasan per jenis dan summary total
    - validation_report.json: detail per-case results
    - validation_log.txt: full Gemma responses untuk forensic
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import ollama

from utils import (
    JENIS_TO_CHUNKS,
    classify_soal,
    format_context,
    load_system_prompt,
    retrieve_chunks,
)


# ============================================================================
# Test Cases (40 soal: 4 per jenis x 10 jenis)
# ============================================================================
# Setiap case: id, query, expected_jenis, expected_answer, mode, features
# features = {nama_feature: True/False} - True artinya HARUS muncul,
# False artinya TIDAK boleh muncul di response.

TEST_CASES = [
    # ====== Jenis Nol ======
    {"id": "Nol-01", "query": "B: berapa 7 + 0", "expected_jenis": "Nol",
     "expected_answer": 7, "mode": "B",
     "features": {"komutativitas": False, "analogi": True}},
    {"id": "Nol-02", "query": "B: berapa 0 + 8", "expected_jenis": "Nol",
     "expected_answer": 8, "mode": "B",
     "features": {"komutativitas": False, "analogi": True}},
    {"id": "Nol-03", "query": "B: berapa 25 + 0", "expected_jenis": "Nol",
     "expected_answer": 25, "mode": "B",
     "features": {"komutativitas": False, "analogi": True}},
    {"id": "Nol-04", "query": "C: berapa 0 + 0", "expected_jenis": "Nol",
     "expected_answer": 0, "mode": "C",
     "features": {"komutativitas": False}},

    # ====== Jenis A1 (1d+1d, hasil 1-5) ======
    {"id": "A1-01", "query": "B: berapa 1 + 1", "expected_jenis": "A1",
     "expected_answer": 2, "mode": "B",
     "features": {"komutativitas": True, "jari": True}},
    {"id": "A1-02", "query": "B: berapa 2 + 3", "expected_jenis": "A1",
     "expected_answer": 5, "mode": "B",
     "features": {"komutativitas": True, "jari": True}},
    {"id": "A1-03", "query": "B: berapa 3 + 1", "expected_jenis": "A1",
     "expected_answer": 4, "mode": "B",
     "features": {"komutativitas": True, "jari": True}},
    {"id": "A1-04", "query": "C: berapa 2 + 2", "expected_jenis": "A1",
     "expected_answer": 4, "mode": "C",
     "features": {"komutativitas": False, "jari": True}},

    # ====== Jenis A2 (1d+1d, hasil 6-10) ======
    {"id": "A2-01", "query": "B: berapa 4 + 5", "expected_jenis": "A2",
     "expected_answer": 9, "mode": "B",
     "features": {"komutativitas": True, "jari": True}},
    {"id": "A2-02", "query": "B: berapa 6 + 3", "expected_jenis": "A2",
     "expected_answer": 9, "mode": "B",
     "features": {"komutativitas": True, "jari": True}},
    {"id": "A2-03", "query": "B: berapa 7 + 3", "expected_jenis": "A2",
     "expected_answer": 10, "mode": "B",
     "features": {"komutativitas": True, "jari": True, "pasangan_10": True}},
    {"id": "A2-04", "query": "C: berapa 5 + 5", "expected_jenis": "A2",
     "expected_answer": 10, "mode": "C",
     "features": {"komutativitas": False, "jari": True}},

    # ====== Jenis B1 (10 + X) ======
    {"id": "B1-01", "query": "B: berapa 10 + 1", "expected_jenis": "B1",
     "expected_answer": 11, "mode": "B",
     "features": {"komutativitas": True, "kepala": True}},
    {"id": "B1-02", "query": "B: berapa 10 + 5", "expected_jenis": "B1",
     "expected_answer": 15, "mode": "B",
     "features": {"komutativitas": True, "kepala": True}},
    {"id": "B1-03", "query": "B: berapa 10 + 9", "expected_jenis": "B1",
     "expected_answer": 19, "mode": "B",
     "features": {"komutativitas": True, "kepala": True}},
    {"id": "B1-04", "query": "C: berapa 10 + 3", "expected_jenis": "B1",
     "expected_answer": 13, "mode": "C",
     "features": {"komutativitas": False}},

    # ====== Jenis B2 (X + 10) ======
    {"id": "B2-01", "query": "B: berapa 7 + 10", "expected_jenis": "B2",
     "expected_answer": 17, "mode": "B",
     "features": {"komutativitas": True, "kepala": True}},
    {"id": "B2-02", "query": "B: berapa 4 + 10", "expected_jenis": "B2",
     "expected_answer": 14, "mode": "B",
     "features": {"komutativitas": True, "kepala": True}},
    {"id": "B2-03", "query": "B: berapa 9 + 10", "expected_jenis": "B2",
     "expected_answer": 19, "mode": "B",
     "features": {"komutativitas": True, "kepala": True}},
    {"id": "B2-04", "query": "C: berapa 6 + 10", "expected_jenis": "B2",
     "expected_answer": 16, "mode": "C",
     "features": {"komutativitas": False}},

    # ====== Jenis B3 (1d+1d, hasil 11-19) ======
    {"id": "B3-01", "query": "B: berapa 9 + 5", "expected_jenis": "B3",
     "expected_answer": 14, "mode": "B",
     "features": {"komutativitas": True, "pasangan_10": True, "kepala": True}},
    {"id": "B3-02", "query": "B: berapa 8 + 7", "expected_jenis": "B3",
     "expected_answer": 15, "mode": "B",
     "features": {"komutativitas": True, "pasangan_10": True}},
    {"id": "B3-03", "query": "B: berapa 5 + 9", "expected_jenis": "B3",
     "expected_answer": 14, "mode": "B",
     "features": {"komutativitas": True, "pasangan_10": True}},
    {"id": "B3-04", "query": "C: berapa 7 + 6", "expected_jenis": "B3",
     "expected_answer": 13, "mode": "C",
     "features": {"komutativitas": False}},

    # ====== Jenis C (2d+1d) ======
    {"id": "C-01", "query": "B: berapa 13 + 4", "expected_jenis": "C",
     "expected_answer": 17, "mode": "B",
     "features": {"komutativitas": True, "cara_cepat": True, "lirik_kanan": True}},
    {"id": "C-02", "query": "B: berapa 25 + 7", "expected_jenis": "C",
     "expected_answer": 32, "mode": "B",
     "features": {"komutativitas": True, "cara_cepat": True, "lirik_kanan": True}},
    {"id": "C-03", "query": "B: berapa 47 + 8", "expected_jenis": "C",
     "expected_answer": 55, "mode": "B",
     "features": {"komutativitas": True, "cara_cepat": True, "lirik_kanan": True}},
    {"id": "C-04", "query": "C: berapa 38 + 5", "expected_jenis": "C",
     "expected_answer": 43, "mode": "C",
     "features": {"komutativitas": False, "cara_cepat": True}},

    # ====== Jenis D (max 2d) ======
    {"id": "D-01", "query": "B: berapa 32 + 21", "expected_jenis": "D",
     "expected_answer": 53, "mode": "B",
     "features": {"komutativitas": True, "bracket": True}},
    {"id": "D-02", "query": "B: berapa 37 + 29", "expected_jenis": "D",
     "expected_answer": 66, "mode": "B",
     "features": {"komutativitas": True, "bracket": True}},
    {"id": "D-03", "query": "B: berapa 2 + 21", "expected_jenis": "D",
     "expected_answer": 23, "mode": "B",
     "features": {"komutativitas": True}},
    {"id": "D-04", "query": "C: berapa 45 + 38", "expected_jenis": "D",
     "expected_answer": 83, "mode": "C",
     "features": {"komutativitas": False}},

    # ====== Jenis E (3 digit) ======
    {"id": "E-01", "query": "B: berapa 106 + 283", "expected_jenis": "E",
     "expected_answer": 389, "mode": "B",
     "features": {"komutativitas": False}},
    {"id": "E-02", "query": "B: berapa 106 + 287", "expected_jenis": "E",
     "expected_answer": 393, "mode": "B",
     "features": {"komutativitas": False, "notasi_1_kecil": True}},
    {"id": "E-03", "query": "C: berapa 113 + 287", "expected_jenis": "E",
     "expected_answer": 400, "mode": "C",
     "features": {"komutativitas": False, "notasi_1_kecil": True}},
    {"id": "E-04", "query": "B: berapa 46 + 287", "expected_jenis": "E",
     "expected_answer": 333, "mode": "B",
     "features": {"komutativitas": False, "notasi_1_kecil": True}},

    # ====== Jenis F (4+ digit) ======
    {"id": "F-01", "query": "B: berapa 4859 + 3148", "expected_jenis": "F",
     "expected_answer": 8007, "mode": "B",
     "features": {"komutativitas": False, "notasi_1_kecil": True}},
    {"id": "F-02", "query": "B: berapa 4259 + 3148", "expected_jenis": "F",
     "expected_answer": 7407, "mode": "B",
     "features": {"komutativitas": False, "notasi_1_kecil": True}},
    {"id": "F-03", "query": "B: berapa 3473 + 3529", "expected_jenis": "F",
     "expected_answer": 7002, "mode": "B",
     "features": {"komutativitas": False, "notasi_1_kecil": True}},
    {"id": "F-04", "query": "C: berapa 4859 + 3148", "expected_jenis": "F",
     "expected_answer": 8007, "mode": "C",
     "features": {"komutativitas": False, "lirik_kanan": True}},
]


# ============================================================================
# Feature detectors (regex-based)
# ============================================================================

def detect_features(response_text: str) -> dict:
    """Deteksi feature di response Gemma. Returns dict feature: bool."""
    text = response_text.lower()
    return {
        "komutativitas": bool(re.search(r"kalau dibalik", text)),
        "jari": bool(re.search(r"\bjari\b|kelingking|telunjuk|jempol|manis|tengah", text)),
        "pasangan_10": bool(re.search(r"pasangan\s+10|pasangan\s+\d+\s+supaya\s+10", text)),
        "kepala": bool(re.search(r"di kepala|ke kepala|masukkan.*ke kepala", text)),
        "cara_cepat": bool(re.search(r"cara cepat", text)),
        "lirik_kanan": bool(re.search(r"lirik kanan", text)),
        "notasi_1_kecil": bool(re.search(r"₁|1 kecil", text)),
        "bracket": bool(re.search(r"\[\s*\d+\s*\+\s*\d+\s*\]", response_text)),
        "analogi": bool(re.search(r"apel|kelereng|jeruk", text)),
    }


def extract_answer(response_text: str, query_a: int, query_b: int) -> int:
    """Extract jawaban matematika dari response Gemma.

    Strategi: cari pola "a + b = X" atau "a+b = X" dimana a dan b sesuai query.
    Kalau tidak ketemu, cari pola "Jadi ... = X" di akhir response.
    Returns int atau None.
    """
    # Pattern 1: exact match "query_a + query_b = X"
    pattern1 = rf"{query_a}\s*\+\s*{query_b}\s*=\s*(\d+)"
    matches = re.findall(pattern1, response_text)
    if matches:
        # Ambil yang terakhir (biasanya yang paling akhir adalah jawaban final)
        return int(matches[-1])

    # Pattern 2: "Jadi ... = X" di mana saja
    pattern2 = r"[Jj]adi[^=]*=\s*(\d+)"
    matches = re.findall(pattern2, response_text)
    if matches:
        return int(matches[-1])

    # Pattern 3: "Jawab: ... = X"
    pattern3 = r"[Jj]awab[^=]*=\s*(\d+)"
    matches = re.findall(pattern3, response_text)
    if matches:
        return int(matches[-1])

    return None


# ============================================================================
# Test runners
# ============================================================================

def run_classify(case):
    """Test classifier. Returns (passed, actual_jenis)."""
    actual = classify_soal(case["query"])
    return actual == case["expected_jenis"], actual


def run_retrieve(case):
    """Test retrieval. Returns (passed, chunks)."""
    chunks = retrieve_chunks(case["query"])
    expected_ids = JENIS_TO_CHUNKS.get(case["expected_jenis"], [])
    retrieved_ids = [c["id"] for c in chunks]
    found = [eid for eid in expected_ids if eid in retrieved_ids]
    return len(found) > 0, chunks


def run_gemma(case, model):
    """Run query through Gemma. Returns response text."""
    system = load_system_prompt()
    chunks = retrieve_chunks(case["query"])
    context = format_context(chunks)
    user_msg = f"{case['query']}\n\n<konteks_dokumen>\n{context}\n</konteks_dokumen>"

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user_msg},
    ]

    response = ollama.chat(model=model, messages=messages)
    return response["message"]["content"]


def check_math(case, response):
    """Check math accuracy. Returns (passed, extracted_answer)."""
    # Extract operand dari query
    match = re.search(r"(\d+)\s*\+\s*(\d+)", case["query"])
    if not match:
        return False, None
    a, b = int(match.group(1)), int(match.group(2))

    extracted = extract_answer(response, a, b)
    if extracted is None:
        return False, None
    return extracted == case["expected_answer"], extracted


def check_format(case, response):
    """Check format compliance. Returns (passed, issues_list)."""
    detected = detect_features(response)
    issues = []
    for feature, expected in case["features"].items():
        actual = detected.get(feature, False)
        if expected and not actual:
            issues.append(f"missing_{feature}")
        elif not expected and actual:
            issues.append(f"unexpected_{feature}")
    return len(issues) == 0, issues


# ============================================================================
# Main validator
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Validasi besar pipeline RAG GASING")
    parser.add_argument("--quick", action="store_true",
                        help="Skip Gemma, cuma classify + retrieve (~30 detik)")
    parser.add_argument("--model", default="gemma4:e4b",
                        help="Model Ollama (default: gemma4:e4b)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit jumlah cases (untuk test cepat)")
    args = parser.parse_args()

    cases = TEST_CASES[:args.limit] if args.limit else TEST_CASES
    n = len(cases)

    print()
    print("=" * 70)
    print(f"GASING RAG: Validasi Besar ({n} test cases)")
    if args.quick:
        print(f"Mode: QUICK (classify + retrieve, no Gemma)")
    else:
        print(f"Mode: FULL (classify + retrieve + Gemma {args.model})")
        estimated_min = (n * 12) / 60
        print(f"Estimasi waktu: ~{estimated_min:.0f} menit")
    print("=" * 70)
    print()

    start_time = time.time()
    results = []

    for i, case in enumerate(cases, 1):
        result = {
            "id": case["id"],
            "query": case["query"],
            "expected_jenis": case["expected_jenis"],
            "expected_answer": case["expected_answer"],
        }

        # Classify
        cls_pass, cls_actual = run_classify(case)
        result["classify_pass"] = cls_pass
        result["classify_actual"] = cls_actual

        # Retrieve
        ret_pass, chunks = run_retrieve(case)
        result["retrieve_pass"] = ret_pass
        result["retrieved_ids"] = [c["id"] for c in chunks]

        # Gemma + checks
        if not args.quick:
            try:
                response = run_gemma(case, args.model)
                result["gemma_response"] = response
                math_pass, math_actual = check_math(case, response)
                result["math_pass"] = math_pass
                result["math_actual"] = math_actual
                fmt_pass, fmt_issues = check_format(case, response)
                result["format_pass"] = fmt_pass
                result["format_issues"] = fmt_issues
            except Exception as e:
                result["gemma_response"] = f"ERROR: {e}"
                result["math_pass"] = False
                result["format_pass"] = False
                result["format_issues"] = ["gemma_error"]

        results.append(result)

        # Print per-case status
        status_parts = [f"[{i:2d}/{n}] {case['id']:7s}"]
        status_parts.append(f"cls={'+' if cls_pass else '-'}")
        status_parts.append(f"ret={'+' if ret_pass else '-'}")
        if not args.quick:
            math_pass_val = result.get("math_pass", False)
            fmt_pass_val = result.get("format_pass", False)
            math_actual_val = result.get("math_actual")
            status_parts.append(f"math={'+' if math_pass_val else '-'}")
            if not math_pass_val:
                status_parts.append(f"(got {math_actual_val}, want {case['expected_answer']})")
            status_parts.append(f"fmt={'+' if fmt_pass_val else '-'}")
            if not fmt_pass_val:
                status_parts.append(f"({','.join(result.get('format_issues', []))})")
        print(" ".join(status_parts))

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print(f"Selesai dalam {elapsed:.1f} detik ({elapsed/60:.1f} menit)")
    print("=" * 70)
    print()

    # Per-jenis summary
    by_jenis = {}
    for r in results:
        case_id = r["id"]
        jenis = case_id.split("-")[0]
        if jenis not in by_jenis:
            by_jenis[jenis] = {"total": 0, "cls": 0, "ret": 0, "math": 0, "fmt": 0}
        by_jenis[jenis]["total"] += 1
        if r.get("classify_pass"): by_jenis[jenis]["cls"] += 1
        if r.get("retrieve_pass"): by_jenis[jenis]["ret"] += 1
        if not args.quick:
            if r.get("math_pass"): by_jenis[jenis]["math"] += 1
            if r.get("format_pass"): by_jenis[jenis]["fmt"] += 1

    print("Per-Jenis Summary:")
    print(f"  {'Jenis':6s} {'Cls':>5s} {'Ret':>5s} {'Math':>6s} {'Fmt':>5s}")
    for jenis in ["Nol", "A1", "A2", "B1", "B2", "B3", "C", "D", "E", "F"]:
        if jenis not in by_jenis:
            continue
        b = by_jenis[jenis]
        cls_s = f"{b['cls']}/{b['total']}"
        ret_s = f"{b['ret']}/{b['total']}"
        if args.quick:
            math_s, fmt_s = "n/a", "n/a"
        else:
            math_s = f"{b['math']}/{b['total']}"
            fmt_s = f"{b['fmt']}/{b['total']}"
        print(f"  {jenis:6s} {cls_s:>5s} {ret_s:>5s} {math_s:>6s} {fmt_s:>5s}")

    # Totals
    n_cls = sum(1 for r in results if r.get("classify_pass"))
    n_ret = sum(1 for r in results if r.get("retrieve_pass"))
    print()
    print(f"TOTAL:")
    print(f"  Classify : {n_cls}/{n} ({100*n_cls/n:.0f}%)")
    print(f"  Retrieve : {n_ret}/{n} ({100*n_ret/n:.0f}%)")
    if not args.quick:
        n_math = sum(1 for r in results if r.get("math_pass"))
        n_fmt = sum(1 for r in results if r.get("format_pass"))
        print(f"  Math     : {n_math}/{n} ({100*n_math/n:.0f}%)")
        print(f"  Format   : {n_fmt}/{n} ({100*n_fmt/n:.0f}%)")

    # Save detailed report
    report_path = Path("validation_report.json")
    report = {
        "timestamp": datetime.now().isoformat(),
        "model": args.model if not args.quick else "n/a",
        "mode": "quick" if args.quick else "full",
        "total_cases": n,
        "duration_seconds": elapsed,
        "results": results,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                           encoding="utf-8")
    print()
    print(f"Detailed report saved to: {report_path.absolute()}")

    if not args.quick:
        log_path = Path("validation_log.txt")
        with log_path.open("w", encoding="utf-8") as f:
            for r in results:
                f.write("=" * 70 + "\n")
                f.write(f"Case: {r['id']}\n")
                f.write(f"Query: {r['query']}\n")
                f.write(f"Expected answer: {r['expected_answer']}\n")
                f.write(f"Math pass: {r.get('math_pass')}\n")
                f.write(f"Math actual: {r.get('math_actual')}\n")
                f.write(f"Format pass: {r.get('format_pass')}\n")
                f.write(f"Format issues: {r.get('format_issues', [])}\n")
                f.write(f"\nGemma response:\n{r.get('gemma_response', 'N/A')}\n\n")
        print(f"Full Gemma log saved to: {log_path.absolute()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
