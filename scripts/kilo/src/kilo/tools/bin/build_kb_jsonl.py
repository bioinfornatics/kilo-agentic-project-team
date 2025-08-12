"""Convert memory_bank/*.md to JSONL for Qdrant ingest (writes memory_packs/kb.documents.jsonl)."""
import json, sys, datetime, pathlib, re
import argparse
# `root` et `src` seront déterminés à partir de l’argument CLI `--root` après l’analyse des arguments.
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-d", "--directory", action="append", help="Dossier(s) à scanner")
parser.add_argument("--root", type=str, help="Racine du projet (par défaut, le dossier courant)")
args = parser.parse_args()
# Définition de `root` et `src` selon l'argument CLI `--root`
root = pathlib.Path(args.root).resolve() if args.root else pathlib.Path.cwd()
src = root / "memory_bank"
dirs = [pathlib.Path(d) for d in args.directory] if args.directory else [src]
all_files = []
for d in dirs:
    all_files.extend(d.rglob("*.md"))
# Avertissement si aucun fichier .md n’est trouvé dans les dossiers spécifiés
if not all_files:
    print("Avertissement: aucun fichier .md n’est trouvé dans les dossiers spécifiés")
outp = pathlib.Path.cwd() / "kb.documents.jsonl"
outp.parent.mkdir(parents=True, exist_ok=True)


def md_to_rec(p: pathlib.Path):
    text = p.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip() if text.startswith("#") else p.stem
    body = "\n".join(text.splitlines()[1:]).strip()
    payload = {
        "repo":"project",
        "path": p.relative_to(root).as_posix(),
        "lang":"md",
        "title": title,
        "tags": [],
        "persona": ["datallm","fullstack","uiux","qa","devops","product"],
        "artifact_type":"kb",
        "updated_at": datetime.datetime.utcnow().isoformat()+"Z"
    }
    return {"id": f"kb::{p.stem}","text": body, "payload": payload}

with outp.open("w", encoding="utf-8") as f:
    for p in sorted(all_files):
        f.write(json.dumps(md_to_rec(p), ensure_ascii=False) + "\n")

print(str(outp))
