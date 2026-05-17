"""State yang diinisialisasi saat startup FastAPI server."""
import ollama
import chromadb
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.utils import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    load_system_prompt,
)


class StartupState:
    """Singleton yang menyimpan koneksi dan state yang di-load saat startup."""

    def __init__(self):
        self.chroma_collection = None
        self.system_prompt: str = ""
        self.ollama_ok: bool = False
        self.chromadb_ok: bool = False
        self.model_name: str = "gemma4:e4b"
        self.chunks_loaded: int = 0

    async def initialize(self):
        """Load ChromaDB dan cek Ollama. Dipanggil saat server start."""
        # 1. Load ChromaDB
        try:
            client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
            self.chroma_collection = client.get_collection(name=COLLECTION_NAME)
            self.chunks_loaded = self.chroma_collection.count()
            self.chromadb_ok = True
            print(f"[startup] ChromaDB OK — {self.chunks_loaded} chunks loaded")
        except Exception as e:
            self.chromadb_ok = False
            print(f"[startup] ChromaDB ERROR: {e}")

        # 2. Cek Ollama
        try:
            models = ollama.list()
            available = [m.model for m in models.models]
            self.ollama_ok = any(self.model_name in m for m in available)
            status = "OK" if self.ollama_ok else f"model {self.model_name} tidak ditemukan"
            print(f"[startup] Ollama {status} — models: {available}")
        except Exception as e:
            self.ollama_ok = False
            print(f"[startup] Ollama ERROR: {e}")

        # 3. Load system prompt
        try:
            self.system_prompt = load_system_prompt()
            print(f"[startup] System prompt loaded ({len(self.system_prompt)} chars)")
        except Exception as e:
            self.system_prompt = (
                "Kamu adalah tutor Metode GASING. Jelaskan matematika dengan "
                "cara konkret, hangat, dan dalam Bahasa Indonesia untuk siswa SD."
            )
            print(f"[startup] System prompt fallback: {e}")


# Singleton instance — diakses oleh router via import
startup_state = StartupState()
