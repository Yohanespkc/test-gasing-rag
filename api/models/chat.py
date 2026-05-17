"""
Pydantic models untuk request/response POST /chat.
"""
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    """Request body dari Unity Sacred Octagon."""

    query: str = Field(
        ...,
        description="Pertanyaan siswa dalam Bahasa Indonesia (teks bebas)",
        examples=["47 + 8 berapa?"],
    )
    soal_context: Optional[str] = Field(
        default=None,
        description="Soal aktif di game (opsional, untuk context-aware response)",
        examples=["47 + 8"],
    )
    mode: Optional[str] = Field(
        default="B",
        description="Mode pembelajaran: 'B' (belajar/step-by-step) atau 'C' (mencongak/cepat)",
        examples=["B"],
    )
    filter_topik: Optional[str] = Field(
        default=None,
        description="Filter topik RAG: null (semua) | 'penjumlahan' | 'filosofi_gasing'",
        examples=[None],
    )

    @field_validator("query")
    @classmethod
    def validate_query(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3:
            raise ValueError("Query terlalu pendek (minimum 3 karakter)")
        if len(v) > 500:
            raise ValueError("Query terlalu panjang (maksimum 500 karakter)")
        return v


class ChatResponse(BaseModel):
    """Response JSON yang diterima Unity."""

    response: str = Field(description="Penjelasan pedagogis GASING dari AI Tutor")
    topik_terdeteksi: str = Field(description="Topik yang terdeteksi: 'penjumlahan' | 'filosofi_gasing' | 'umum'")
    chunks_digunakan: List[str] = Field(description="Daftar chunk ID yang digunakan untuk RAG")
    latency_ms: int = Field(description="Waktu respons dalam milidetik")
