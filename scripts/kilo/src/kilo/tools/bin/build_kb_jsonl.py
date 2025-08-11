"""Convert memory_bank/*.md to JSONL for Qdrant ingest (writes memory_packs/kb.documents.jsonl)."""
import json, sys, datetime, pathlib, re
root = pathlib.Path(__file__).resolve().parents[1]
src = root / "memory_bank"
outp = root / "memory_packs" / "kb.documents.jsonl"
outp.parent.mkdir(parents=True, exist_ok=True)

def md_to_rec(p: pathlib.Path):
    text = p.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip() if text.startswith("#") else p.stem
    body = "\n".join(text.splitlines()[1:]).strip()
    payload = {
        "repo":"project",
        "path": f"memory_bank/{p.name}",
        "lang":"md",
        "title": title,
        "tags": [],
        "persona": ["datallm","fullstack","uiux","qa","devops","product"],
        "artifact_type":"kb",
        "updated_at": datetime.datetime.utcnow().isoformat()+"Z"
    }
    return {"id": f"kb::{p.stem}","text": body, "payload": payload}

with outp.open("w", encoding="utf-8") as f:
    for p in sorted(src.glob("*.md")):
        f.write(json.dumps(md_to_rec(p), ensure_ascii=False) + "\n")

print(str(outp))
