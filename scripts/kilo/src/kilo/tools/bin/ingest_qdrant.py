"""Upsert JSONL docs into Qdrant (dense only placeholder vectors; plug real embeddings via your pipeline)."""
import os, json, sys
from qdrant_client import QdrantClient
from qdrant_client.http import models as qm

COLL = os.getenv("QDRANT_COLLECTION","code_docs")
URL = os.getenv("QDRANT_URL","http://localhost:6333")
KEY = os.getenv("QDRANT_API_KEY")

def load_jsonl(path: str):
    for line in open(path, "r", encoding="utf-8"):
        if line.strip():
            yield json.loads(line)

def main(jsonl_path: str):
    client = QdrantClient(url=URL, api_key=KEY)
    # Ensure collection
    try:
        client.get_collection(COLL)
    except Exception:
        client.recreate_collection(
            collection_name=COLL,
            vectors_config={"text_dense": qm.VectorParams(size=1536, distance=qm.Distance.COSINE)}
        )
    points = []
    for rec in load_jsonl(jsonl_path):
        pid = rec.get("id")
        payload = rec.get("payload", {})
        vec = [0.0]*1536  # placeholder vector
        points.append(qm.PointStruct(id=pid, vector={"text_dense": vec}, payload=payload))
    if points:
        client.upsert(collection_name=COLL, points=points)
    print(f"Upserted {len(points)} points into {COLL} @ {URL}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/ingest_qdrant.py memory_packs/kb.documents.jsonl"); sys.exit(2)
    main(sys.argv[1])
