/title: Bootstrap Memory Bank and Qdrant
/description: Build JSONL from /memory_bank and ingest into Qdrant collection code_docs.
/steps:
- run: python scripts/build_kb_jsonl.py
- run: export QDRANT_URL=http://localhost:6333 && python scripts/ingest_qdrant.py memory_packs/kb.documents.jsonl
- note: Expect "[Memory Bank: Indexed]" on next task start if ingestion succeeded.
