"""utils.py v1.2 - Helper functions untuk GASING RAG pipeline."""
import re
from pathlib import Path
from typing import Optional
import chromadb
import ollama

BASE = Path(__file__).resolve().parent.parent
CHUNKS_DIR = BASE / "chunks"
CHROMA_DB_PATH = BASE / "chroma_db"
COLLECTION_NAME = "gasing_chunks"
EMBEDDING_MODEL = "nomic-embed-text"
EMBEDDING_CTX = 8192
LIST_METADATA_FIELDS = {"mode_tercakup", "konsep_terkait", "jenis_yang_pakai", "jenis_yang_tidak_pakai", "sub_kasus"}

JENIS_TO_CHUNKS = {
    "Nol": ["J00_nol"], "A1": ["J10_a1"], "A2": ["J20_a2"],
    "B1": ["J30_b1"], "B2": ["J40_b2"], "B3": ["J50_b3"],
    "C": ["J60_c"], "D": ["J70_d"],
    "E": ["J81_e_tanpa_carry", "J82_e_carry_satuan_puluhan", "J83_e_cascade_1_kecil"],
    "F": ["J91_f_pengantar_aturan", "J92_f_alignment_digit", "J93_f_belajar_simple",
          "J94_f_belajar_cascade", "J95_f_belajar_diff_digits", "J96_f_mencongak"],
}

def classify_soal(text):
    text_clean = re.sub(r'^[BbCc][\s:.]+', '', text.strip())
    match = re.search(r'(\d+)\s*\+\s*(\d+)', text_clean)
    if not match: return None
    a, b = int(match.group(1)), int(match.group(2))
    if a == 0 or b == 0: return "Nol"
    if a == 10 and 1 <= b <= 9: return "B1"
    if b == 10 and 1 <= a <= 9: return "B2"
    da, db, r = len(str(a)), len(str(b)), a + b
    if da == 1 and db == 1:
        if 1 <= r <= 5: return "A1"
        if 6 <= r <= 10: return "A2"
        if 11 <= r <= 19: return "B3"
    if da == 2 and db == 1: return "C"
    if max(da, db) == 2: return "D"
    if max(da, db) == 3: return "E"
    if max(da, db) >= 4: return "F"
    return None

def parse_frontmatter(content):
    if not content.startswith("---"): return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3: return {}, content
    fm, body = parts[1], parts[2].lstrip("\n")
    metadata, current_list_key = {}, None
    for line in fm.strip().split("\n"):
        if not line.strip() or line.strip().startswith("#"): continue
        if line.startswith("  - "):
            if current_list_key is not None:
                metadata[current_list_key].append(line.strip()[2:].strip())
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key, value = key.strip(), value.strip()
            if value == "":
                current_list_key = key
                metadata[key] = []
            else:
                current_list_key = None
                if value.startswith('"') and value.endswith('"'): value = value[1:-1]
                if value == "true": value = True
                elif value == "false": value = False
                elif value.lstrip("-").isdigit(): value = int(value)
                metadata[key] = value
    return metadata, body

def load_chunks():
    chunks = []
    for subdir in ("shared", "per_jenis", "filosofi"):
        subdir_path = CHUNKS_DIR / subdir
        if not subdir_path.exists():
            continue
        for path in sorted(subdir_path.glob("*.md")):
            content = path.read_text(encoding="utf-8")
            metadata, body = parse_frontmatter(content)
            chunks.append({"id": metadata.get("id", path.stem),
                          "file": str(path.relative_to(BASE)),
                          "metadata": metadata, "content": content, "body": body})
    return chunks

def flatten_metadata(m):
    flat = {}
    for k, v in m.items():
        if isinstance(v, list):
            flat[k] = ",".join(str(i) for i in v)
        elif isinstance(v, (str, int, float, bool)):
            flat[k] = v
    return flat

def unflatten_metadata(m):
    out = {}
    for k, v in m.items():
        if k in LIST_METADATA_FIELDS and isinstance(v, str):
            out[k] = [i.strip() for i in v.split(",") if i.strip()]
        else:
            out[k] = v
    return out

def embed(text):
    r = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text, options={"num_ctx": EMBEDDING_CTX})
    return r["embedding"]

def get_chroma_collection(create_if_missing=False):
    client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    if create_if_missing:
        try: client.delete_collection(COLLECTION_NAME)
        except: pass
        return client.create_collection(name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"})
    return client.get_collection(name=COLLECTION_NAME)

def retrieve_chunks(query, top_k=3, expand_shared=True, filter_topik="penjumlahan", use_rule_based=True):
    coll = get_chroma_collection(create_if_missing=False)
    forced_ids, classified_jenis = set(), None
    if use_rule_based:
        classified_jenis = classify_soal(query)
        if classified_jenis:
            forced_ids = set(JENIS_TO_CHUNKS.get(classified_jenis, []))
    effective_top_k = 2 if classified_jenis else top_k
    query_emb = embed(query)
    where = {"topik": filter_topik} if filter_topik else None
    sem = coll.query(query_embeddings=[query_emb], n_results=effective_top_k, where=where)
    retrieved, seen = [], set()
    if forced_ids:
        forced = coll.get(ids=list(forced_ids))
        for i in range(len(forced["ids"])):
            cid = forced["ids"][i]
            retrieved.append({"id": cid, "document": forced["documents"][i],
                "metadata": unflatten_metadata(forced["metadatas"][i]),
                "distance": None, "source": f"rule:{classified_jenis}"})
            seen.add(cid)
    for i in range(len(sem["ids"][0])):
        cid = sem["ids"][0][i]
        if cid in seen: continue
        retrieved.append({"id": cid, "document": sem["documents"][0][i],
            "metadata": unflatten_metadata(sem["metadatas"][0][i]),
            "distance": sem["distances"][0][i], "source": "semantic"})
        seen.add(cid)
    if expand_shared:
        needed = set()
        for c in retrieved:
            for sid in c["metadata"].get("konsep_terkait", []):
                if sid not in seen: needed.add(sid)
        if needed:
            sh = coll.get(ids=list(needed))
            for i in range(len(sh["ids"])):
                retrieved.append({"id": sh["ids"][i], "document": sh["documents"][i],
                    "metadata": unflatten_metadata(sh["metadatas"][i]),
                    "distance": None, "source": "expanded"})
                seen.add(sh["ids"][i])
    def sk(c):
        src, kat = c.get("source", ""), c["metadata"].get("kategori", "")
        if src.startswith("rule"): return (0, c["id"])
        if kat == "shared": return (1, c["id"])
        return (2, c["id"])
    retrieved.sort(key=sk)
    return retrieved

def format_context(chunks):
    pieces = []
    for c in chunks:
        _, body = parse_frontmatter(c["document"])
        pieces.append(body.strip())
    return "\n\n---\n\n".join(pieces)

def load_system_prompt():
    return (BASE / "system_prompt.txt").read_text(encoding="utf-8").strip()
