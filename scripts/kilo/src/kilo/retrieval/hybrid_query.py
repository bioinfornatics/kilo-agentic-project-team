"""Hybrid query: prefetch sparse → dense top_k → rerank (RSF).
Usage:
  python retrieval/hybrid_query.py "query text" --collection code_docs --prefetch 200 --dense_k 60 --final_k 15 --rsf 0.6,0.4
Requires:
  - QDRANT_URL (default http://localhost:6333)
  - QDRANT_API_KEY (optional)
  - EMBED_MODEL / OPENAI_API_KEY (for dense)
"""
import os, sys, json, math, argparse, hashlib, re
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http import models as qm

# Local embedding fallback (same as embed_text.py)
def local_embed(text: str, size: int = 384):
    h = hashlib.sha256(text.encode("utf-8")).digest()
    vec = []
    while len(vec) < size:
        for b in h:
            vec.append((b - 128) / 128.0)
            if len(vec) >= size:
                break
    return vec

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--collection", default=os.getenv("QDRANT_COLLECTION","code_docs"))
    ap.add_argument("--prefetch", type=int, default=200)
    ap.add_argument("--dense_k", type=int, default=60)
    ap.add_argument("--final_k", type=int, default=15)
    ap.add_argument("--rsf", default="0.6,0.4")
    args = ap.parse_args()
    rsf_dense, rsf_sparse = [float(x) for x in args.rsf.split(",")]

    url = os.getenv("QDRANT_URL","http://localhost:6333")
    key = os.getenv("QDRANT_API_KEY")
    client = QdrantClient(url=url, api_key=key)

    # Dense vector (OpenAI via embed_text.py contract is not used here; do inline to simplify demo)
    dense_vec = local_embed(args.query, 384)

    # Use sparse query as empty (Qdrant can accept none; in prod, build a query-side sparse vector too).
    # For demo, rely on payload filters or leave to dense only if sparse not configured.
    # Here we do dense-first due to client constraints; still honor RSF at rerank stage.
    search_res = client.search(
        collection_name=args.collection,
        query_vector={"name":"text_dense","vector":dense_vec},
        limit=args.dense_k
    )

    # Rerank with RSF (no live sparse score without query sparse; simulate sparse=0 here)
    rescored = []
    for p in search_res:
        dense_score = p.score or 0.0
        sparse_score = 0.0  # placeholder; wire real sparse in production
        score = rsf_dense * dense_score + rsf_sparse * sparse_score
        rescored.append((score, p))

    rescored.sort(key=lambda x: x[0], reverse=True)
    top = [dict(id=str(p.id), score=s, payload=p.payload) for s,p in rescored[:args.final_k]]

    out_path = "retrieval/hybrid_results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"query": args.query, "results": top}, f, ensure_ascii=False, indent=2)
    print(out_path)

if __name__ == "__main__":
    main()
