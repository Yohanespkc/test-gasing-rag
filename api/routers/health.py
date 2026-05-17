"""
Health router — GET /health
Mengembalikan status Ollama, ChromaDB, dan info server.
"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from api.core.startup import startup_state

router = APIRouter(tags=["Health"])


@router.get("/health", summary="Server Health Check")
async def health():
    """
    Cek status server, Ollama, dan ChromaDB.

    Selalu return HTTP 200 — status detail ada di field masing-masing.
    Unity memanggil endpoint ini sebelum mengirim request /chat.
    """
    return {
        "status": "ok",
        "ollama": "connected" if startup_state.ollama_ok else "disconnected",
        "chromadb": "connected" if startup_state.chromadb_ok else "disconnected",
        "model": startup_state.model_name,
        "chunks_loaded": startup_state.chunks_loaded,
    }
