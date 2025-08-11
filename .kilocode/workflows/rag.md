# Workflow — RAG Pipeline
**steps:** schema → ingest → hybrid query → assemble → eval → gate

## Steps
1. **Schema:** define Qdrant collection (named vectors, payload indexes)
2. **Ingest:** `python scripts/build_kb_jsonl.py && python scripts/ingest_qdrant.py memory_packs/kb.documents.jsonl`
3. **Query:** `python retrieval/hybrid_query.py "task" --collection code_docs --rsf 0.6,0.4`
4. **Assemble:** `ts-node prompt_assembler/bridge.ts` (edge‑anchored with citations)
5. **Eval:** `python eval/harness.py --suite litm --adapter dummy -n 12`

## Gates
- **LITM PBI ≤ 0.20**, **Needle acc ≥ 0.70**, **Drift ≤ 0.30**

## Concrete commands (demo)
```bash
# 1) Build JSONL from memory_bank
python scripts/build_kb_jsonl.py

# 2) (Optional) Build sparse indices
python scripts/build_sparse.py

# 3) Upsert to Qdrant (set QDRANT_URL / API key env)
python scripts/ingest_qdrant.py memory_packs/kb.documents.jsonl

# 4) Hybrid query (dense fallback; wire sparse in prod)
python retrieval/hybrid_query.py "How to assemble prompts?" --collection code_docs

# 5) Assemble prompt (edge‑anchored + citations)
node prompt_assembler/bridge.ts

# 6) Eval gates
python eval/harness.py --suite all
```
