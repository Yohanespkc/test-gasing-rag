#!/usr/bin/env python3
"""
01_ingest.py - Ingest semua chunks GASING ke ChromaDB.

Cara pakai:
    python 01_ingest.py

Hasil:
    Direktori chroma_db/ berisi vector store dengan 22 chunks ter-embed.

Idempotent: jika dijalankan ulang, akan hapus koleksi lama dan buat baru.
Cocok untuk re-indexing setelah Pak edit chunks.

Persiapan:
    1. Pastikan Ollama running (ollama serve)
    2. Pull model embedding: `ollama pull nomic-embed-text`
    3. Pastikan virtualenv aktif dengan dependencies terinstall
"""

import sys
import time

import ollama

from utils import (
    EMBEDDING_MODEL,
    embed,
    flatten_metadata,
    get_chroma_collection,
    load_chunks,
)


def check_ollama_available() -> bool:
    """Cek apakah Ollama service jalan dan model embedding tersedia."""
    try:
        models = ollama.list()
    except Exception as e:
        print(f"ERROR: Tidak bisa konek ke Ollama. Pastikan `ollama serve` jalan.")
        print(f"Detail: {e}")
        return False

    # Cek apakah model embedding ada
    available_models = [m.get("name", m.get("model", "")) for m in models.get("models", [])]

    if not any(EMBEDDING_MODEL in name for name in available_models):
        print(f"ERROR: Model {EMBEDDING_MODEL} belum di-pull.")
        print(f"Jalankan: ollama pull {EMBEDDING_MODEL}")
        print(f"Model yang ada: {available_models}")
        return False

    return True


def main():
    print("=" * 60)
    print("GASING RAG: Ingest Chunks ke ChromaDB")
    print("=" * 60)

    # Pre-check
    print(f"\n[1/4] Cek Ollama dan model {EMBEDDING_MODEL}...")
    if not check_ollama_available():
        sys.exit(1)
    print("      OK")

    # Load chunks
    print(f"\n[2/4] Load chunks dari disk...")
    chunks = load_chunks()
    print(f"      Loaded {len(chunks)} chunks:")
    shared_count = sum(1 for c in chunks if c["metadata"].get("kategori") == "shared")
    per_jenis_count = len(chunks) - shared_count
    print(f"        shared: {shared_count}")
    print(f"        per_jenis: {per_jenis_count}")

    # Buat koleksi baru
    print(f"\n[3/4] Buat koleksi ChromaDB (delete koleksi lama kalau ada)...")
    coll = get_chroma_collection(create_if_missing=True)
    print(f"      Koleksi siap")

    # Embed dan add ke ChromaDB
    print(f"\n[4/4] Embed setiap chunk dan add ke ChromaDB...")
    start = time.time()

    ids = []
    embeddings = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks, 1):
        # Embed isi chunk
        # Strategi: embed seluruh konten (termasuk metadata YAML).
        # Metadata YAML juga membantu retrieval karena ada keyword
        # seperti "Jenis C", "operand 2 digit", dll.
        emb = embed(chunk["content"][:5000])

        ids.append(chunk["id"])
        embeddings.append(emb)
        documents.append(chunk["content"])
        metadatas.append(flatten_metadata(chunk["metadata"]))

        print(f"      [{i:2d}/{len(chunks)}] {chunk['id']:40s} "
              f"({len(chunk['content']):5d} chars)")

    # Batch add ke ChromaDB
    coll.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )

    elapsed = time.time() - start

    print(f"\n{'=' * 60}")
    print(f"Selesai dalam {elapsed:.1f} detik")
    print(f"Total chunks ter-index: {len(chunks)}")
    print(f"ChromaDB persistence: ./chroma_db/")
    print(f"{'=' * 60}")
    print(f"\nLangkah berikut:")
    print(f"  Test retrieval: python 02_query.py 'berapa 25 + 7'")
    print(f"  Mulai chat:     python 03_chat.py")


if __name__ == "__main__":
    main()
