"""
gasing-rag API Server — Story 1.1
FastAPI application entry point dengan health endpoint dan CORS.
"""
import sys
from contextlib import asynccontextmanager
from pathlib import Path

# Pastikan scripts/ bisa diimport dari api/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.routers import chat, health
from api.core.startup import startup_state


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load ChromaDB collection dan cek Ollama saat startup."""
    await startup_state.initialize()
    yield
    # Cleanup jika dibutuhkan di masa depan


app = FastAPI(
    title="gasing-rag AI Tutor API",
    description=(
        "REST API untuk AI Tutor Metode GASING yang terintegrasi dengan "
        "Sacred Octagon Unity game. Powered by RAG + Gemma via Ollama."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — open untuk v1 (Unity WebGL dan development tools)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(chat.router)


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    """Pastikan semua error return JSON, bukan HTML (Unity tidak bisa parse HTML)."""
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal server error: {type(exc).__name__}"},
    )
