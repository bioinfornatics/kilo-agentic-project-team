"""Embed text lines using OpenAI (if OPENAI_API_KEY set) or a local fallback.
Outputs newline-delimited JSON: {"id": "...", "vector": [..]}.
"""
import os, sys, json, hashlib
from typing import List
try:
    from openai import OpenAI
except Exception:
    OpenAI = None

MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")

def local_embed(text: str, size: int = 384):
    # Very rough deterministic fallback: SHA256 → bucket into floats
    h = hashlib.sha256(text.encode("utf-8")).digest()
    # stretch digest to desired size
    vec = []
    while len(vec) < size:
        for b in h:
            vec.append((b - 128) / 128.0)
            if len(vec) >= size:
                break
    return vec

def openai_embed_batch(texts: List[str]):
    client = OpenAI()
    resp = client.embeddings.create(model=MODEL, input=texts)
    return [d.embedding for d in resp.data]

def main(path: str):
    lines = [json.loads(l) for l in open(path, "r", encoding="utf-8") if l.strip()]
    api_key = os.getenv("OPENAI_API_KEY")
    use_openai = OpenAI is not None and api_key
    texts = [l["text"] for l in lines]
    if use_openai:
        try:
            vecs = openai_embed_batch(texts)
        except Exception:
            vecs = [local_embed(t, 384) for t in texts]
            print("WARN: OpenAI embed failed; using local fallback", file=sys.stderr)
    else:
        vecs = [local_embed(t, 384) for t in texts]
    for rec, v in zip(lines, vecs):
        out = {"id": rec.get("id"), "vector": v}
        print(json.dumps(out, ensure_ascii=False))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/embed_text.py memory_packs/kb.documents.jsonl"); sys.exit(2)
    main(sys.argv[1])
