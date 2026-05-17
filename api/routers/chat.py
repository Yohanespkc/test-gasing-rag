"""
Chat router — POST /chat
Menerima query siswa, jalankan RAG pipeline, return penjelasan GASING.
"""
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import ollama
from fastapi import APIRouter, HTTPException

from api.models.chat import ChatRequest, ChatResponse
from api.core.startup import startup_state
from scripts.utils import retrieve_chunks, format_context

router = APIRouter(tags=["Chat"])

# Kata kunci untuk deteksi topik penjumlahan
_MATH_KEYWORDS = {"+", "tambah", "penjumlahan", "jumlahkan", "berapa hasil", "ditambah"}
_FILO_KEYWORDS = {"gasing", "metode", "filosofi", "kenapa", "mengapa", "cara belajar",
                  "takut matematika", "senang belajar", "konkret", "abstrak"}


def _detect_topik(query: str, filter_topik: str | None) -> str:
    """Deteksi topik dari query untuk label response."""
    if filter_topik:
        return filter_topik
    q = query.lower()
    if any(k in q for k in _MATH_KEYWORDS) or "+" in q:
        return "penjumlahan"
    if any(k in q for k in _FILO_KEYWORDS):
        return "filosofi_gasing"
    return "umum"


@router.post("/chat", response_model=ChatResponse, summary="AI Tutor Chat")
async def chat(req: ChatRequest):
    """
    Endpoint utama: terima pertanyaan siswa, return penjelasan pedagogis GASING.

    - **query**: Pertanyaan dalam Bahasa Indonesia (wajib)
    - **soal_context**: Soal aktif di Sacred Octagon (opsional)
    - **mode**: 'B' untuk belajar step-by-step, 'C' untuk mencongak
    - **filter_topik**: Filter RAG per topik (opsional)
    """
    if not startup_state.chromadb_ok:
        raise HTTPException(
            status_code=503,
            detail="Knowledge base tidak tersedia. Pastikan ChromaDB sudah ter-index.",
        )
    if not startup_state.ollama_ok:
        raise HTTPException(
            status_code=503,
            detail="AI Tutor sedang tidak tersedia. Pastikan Ollama berjalan.",
        )

    t_start = time.perf_counter()

    # 1. RAG — retrieve chunks relevan
    try:
        query_for_rag = req.query
        if req.soal_context:
            query_for_rag = f"{req.soal_context} {req.query}"

        chunks = retrieve_chunks(
            query=query_for_rag,
            top_k=3,
            expand_shared=True,
            filter_topik=req.filter_topik,
            use_rule_based=True,
        )
        context = format_context(chunks)
        chunk_ids = [c["id"] for c in chunks]
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Gagal mengambil knowledge base: {str(e)}",
        )

    # 2. Build prompt
    mode_label = "Belajar (step-by-step)" if req.mode == "B" else "Mencongak (cepat)"
    context_note = f"\nSoal yang sedang dikerjakan siswa: {req.soal_context}" if req.soal_context else ""

    user_message = (
        f"Mode: {mode_label}{context_note}\n\n"
        f"Pertanyaan siswa: {req.query}\n\n"
        f"--- Panduan Metode GASING ---\n{context}"
    )

    # 3. Call Ollama
    try:
        result = ollama.chat(
            model=startup_state.model_name,
            messages=[
                {"role": "system", "content": startup_state.system_prompt},
                {"role": "user", "content": user_message},
            ],
            options={"temperature": 0.3, "num_predict": 512},
        )
        response_text = result["message"]["content"].strip()
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"AI Tutor sedang tidak tersedia. Coba lagi dalam beberapa detik. ({type(e).__name__})",
        )

    latency_ms = int((time.perf_counter() - t_start) * 1000)
    topik = _detect_topik(req.query, req.filter_topik)

    return ChatResponse(
        response=response_text,
        topik_terdeteksi=topik,
        chunks_digunakan=chunk_ids,
        latency_ms=latency_ms,
    )
