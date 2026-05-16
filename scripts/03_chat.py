#!/usr/bin/env python3
"""
03_chat.py - Interactive chat dengan GASING RAG.

Cara pakai:
    python 03_chat.py
    python 03_chat.py --model gemma3:4b
    python 03_chat.py --model qwen2.5:7b
    python 03_chat.py --no-retrieval   # mode baseline tanpa RAG (testing)
    python 03_chat.py --debug          # tampilkan chunks yang ter-retrieve

Alur per turn:
    1. User input via terminal
    2. Cek apakah perlu retrieval (skip untuk follow-up "B" / "C" saja
       dan greeting non-matematika)
    3. Embed query, retrieve top-3 chunks, ekspansi shared
    4. Format konteks dokumen
    5. Build augmented user message: pertanyaan asli + tag konteks
    6. Panggil Ollama chat dengan SYSTEM + history + augmented user
    7. Print response
    8. Update history (simpan input asli, bukan augmented version)

Untuk keluar: Ctrl+C atau ketik "/quit"
"""

import argparse
import sys
from typing import Optional

import ollama

from utils import (
    format_context,
    load_system_prompt,
    retrieve_chunks,
)


def is_followup_trigger(text: str) -> bool:
    """Cek apakah pesan hanya berisi trigger B/C tanpa soal."""
    stripped = text.strip().lower().rstrip(":.")
    return stripped in ("b", "c")


def is_math_query(text: str) -> bool:
    """Cek apakah pesan kemungkinan soal matematika.

    Heuristik sederhana: ada digit dan tanda + (atau kata kunci penjumlahan).
    """
    has_digit = any(c.isdigit() for c in text)
    has_plus = "+" in text or "tambah" in text.lower() or "ditambah" in text.lower()
    return has_digit and has_plus


def should_retrieve(user_input: str) -> bool:
    """Tentukan apakah perlu retrieval untuk pesan ini."""
    if is_followup_trigger(user_input):
        return True  # User pilih mode untuk soal sebelumnya, butuh konteks
    if is_math_query(user_input):
        return True
    # Greeting, pertanyaan umum tentang GASING: skip retrieval
    return False


def build_augmented_message(user_input: str, context: str) -> str:
    """Build user message dengan konteks dokumen di akhir.

    Trigger B/C harus tetap di awal supaya SYSTEM prompt mendeteksi.
    Konteks dokumen ditempel setelah pesan asli dengan tag.
    """
    return f"""{user_input}

<konteks_dokumen>
{context}
</konteks_dokumen>"""


def chat_loop(model: str, use_retrieval: bool, debug: bool, filter_topik: Optional[str] = None):
    """Main interactive loop."""
    topik_label = filter_topik if filter_topik else "semua (no filter)"
    print("=" * 70)
    print(f"GASING Tutor RAG (model: {model}, retrieval: {use_retrieval})")
    print(f"Topik filter : {topik_label}")
    print("Perintah dalam sesi:")
    print("  /quit    - keluar")
    print("  /debug   - toggle mode debug")
    print("  /clear   - reset riwayat percakapan")
    print("  /topik   - lihat atau ganti topik filter")
    print("=" * 70)

    system_prompt = load_system_prompt()
    history = [{"role": "system", "content": system_prompt}]

    while True:
        try:
            user_input = input("\nUser: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break

        if not user_input:
            continue

        # Commands
        if user_input == "/quit":
            print("Bye!")
            break
        if user_input == "/debug":
            debug = not debug
            print(f"[debug mode: {debug}]")
            continue
        if user_input == "/clear":
            history = [{"role": "system", "content": system_prompt}]
            print("[history cleared]")
            continue
        if user_input.startswith("/topik"):
            parts = user_input.split(maxsplit=1)
            if len(parts) == 1:
                current = filter_topik if filter_topik else "semua"
                print(f"Topik aktif: {current}")
                print("Cara ganti:")
                print("  /topik penjumlahan")
                print("  /topik filosofi_gasing")
                print("  /topik all")
            else:
                new_topik = parts[1].strip()
                if new_topik == "all":
                    filter_topik = None
                    print("Topik diubah ke: semua (no filter)")
                elif new_topik in ("penjumlahan", "filosofi_gasing"):
                    filter_topik = new_topik
                    print(f"Topik diubah ke: {new_topik}")
                else:
                    print(f"Topik tidak dikenal: {new_topik}")
                    print("Pilihan valid: penjumlahan, filosofi_gasing, all")
            continue

        # Retrieval (kalau diaktifkan dan diperlukan)
        if use_retrieval and should_retrieve(user_input):
            try:
                retrieved = retrieve_chunks(user_input, top_k=5, expand_shared=True,
                                            filter_topik=filter_topik)
            except Exception as e:
                print(f"[ERROR retrieval: {e}]")
                retrieved = []

            if debug and retrieved:
                print(f"\n[DEBUG] Retrieved {len(retrieved)} chunks:")
                for c in retrieved:
                    kat = c["metadata"].get("kategori", "?")
                    dist = (f"{c['distance']:.3f}" if c["distance"] is not None
                            else "expanded")
                    print(f"  [{kat:9s}] {c['id']:40s} ({dist})")

            if retrieved:
                context = format_context(retrieved)
                user_message = build_augmented_message(user_input, context)
            else:
                user_message = user_input
        else:
            if debug:
                print("[DEBUG] Skip retrieval untuk pesan ini")
            user_message = user_input

        # Panggil Ollama
        history.append({"role": "user", "content": user_message})

        try:
            print("\nTutor: ", end="", flush=True)
            response_text = ""
            stream = ollama.chat(
                model=model,
                messages=history,
                stream=True,
            )
            for chunk in stream:
                token = chunk.get("message", {}).get("content", "")
                print(token, end="", flush=True)
                response_text += token
            print()  # newline

        except Exception as e:
            print(f"\n[ERROR memanggil Ollama: {e}]")
            # Hapus pesan user yang gagal
            history.pop()
            continue

        # Simpan ke history TAPI pakai input ASLI (bukan augmented version),
        # supaya history tidak bloat dengan konteks dokumen lama.
        history[-1] = {"role": "user", "content": user_input}
        history.append({"role": "assistant", "content": response_text})


def main():
    parser = argparse.ArgumentParser(description="GASING RAG interactive chat")
    parser.add_argument(
        "--model",
        default="gemma3:4b",
        help="Ollama model untuk LLM (default: gemma3:4b)",
    )
    parser.add_argument(
        "--no-retrieval",
        action="store_true",
        help="Mode baseline tanpa RAG (untuk testing)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Tampilkan chunks yang ter-retrieve di setiap turn",
    )
    parser.add_argument(
        "--topik",
        default=None,
        choices=["penjumlahan", "filosofi_gasing"],
        help="Filter retrieval ke topik tertentu (default: semua topik)",
    )
    args = parser.parse_args()

    chat_loop(
        model=args.model,
        use_retrieval=not args.no_retrieval,
        debug=args.debug,
        filter_topik=args.topik,
    )


if __name__ == "__main__":
    main()
