#!/usr/bin/env python3
"""
02_query.py - Test retrieval standalone untuk inspeksi kualitas RAG.

Cara pakai:
    python 02_query.py "berapa 25 + 7"
    python 02_query.py "B: 4859 + 3148"
    python 02_query.py "operand 0"
    python 02_query.py "komutativitas"

Tujuan:
    Pak bisa cek apakah retrieval mengambil chunks yang relevan.
    Tidak ada Gemma di sini, hanya embedding dan vector search.

Output:
    Untuk setiap chunk yang ter-retrieve, tampilkan:
    - ID chunk
    - Distance (cosine, makin kecil makin mirip)
    - Apakah dari similarity search atau dari ekspansi shared
    - 200 karakter pertama isi chunk
"""

import sys

from utils import retrieve_chunks


def main():
    # Ambil query dari command line
    query = " ".join(sys.argv[1:]).strip()

    if not query:
        print("Cara pakai: python 02_query.py 'pertanyaan kamu di sini'")
        print("\nContoh:")
        print("  python 02_query.py 'berapa 25 + 7'")
        print("  python 02_query.py 'B: 4859 + 3148'")
        sys.exit(1)

    print(f"Query: {query!r}\n")
    print(f"Retrieving (top_k=3 + ekspansi shared via konsep_terkait)...\n")

    chunks = retrieve_chunks(query, top_k=3, expand_shared=True)

    print(f"Dapat {len(chunks)} chunks total\n")
    print("=" * 70)

    for i, chunk in enumerate(chunks, 1):
        kategori = chunk["metadata"].get("kategori", "?")
        distance_str = (
            f"distance={chunk['distance']:.4f}"
            if chunk["distance"] is not None
            else "via konsep_terkait"
        )

        print(f"\n[{i}] {chunk['id']}")
        print(f"    kategori: {kategori}")
        print(f"    {distance_str}")

        # Tampilkan judul dan klasifikasi (200 char pertama setelah frontmatter)
        body = chunk["document"]
        if body.startswith("---"):
            # Skip frontmatter
            parts = body.split("---", 2)
            if len(parts) >= 3:
                body = parts[2].strip()

        preview = body[:300].replace("\n", " ")
        print(f"    preview: {preview}...")

    print(f"\n{'=' * 70}")

    # Ringkasan urutan
    print("\nUrutan akhir konteks yang akan dikirim ke Gemma:")
    for i, chunk in enumerate(chunks, 1):
        kategori = chunk["metadata"].get("kategori", "?")
        print(f"  {i}. [{kategori:9s}] {chunk['id']}")


if __name__ == "__main__":
    main()
