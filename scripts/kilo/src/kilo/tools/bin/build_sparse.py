"""Build TF-IDF sparse vectors for memory_bank/*.md and emit JSONL with indices/values arrays."""
import pathlib, json, re, math, collections, datetime
from typing import List, Dict

root = pathlib.Path(__file__).resolve().parents[1]
src = root / "memory_bank"
outp = root / "memory_packs" / "kb.sparse.jsonl"
outp.parent.mkdir(parents=True, exist_ok=True)

def tokenize(text: str):
    return [t.lower() for t in re.findall(r"[a-zA-Z0-9_]+", text)]

docs = []
vocab = collections.Counter()
for p in sorted(src.glob("*.md")):
    text = p.read_text(encoding="utf-8")
    toks = tokenize(text)
    docs.append((p, toks))
    vocab.update(set(toks))

idf = {}
N = len(docs) or 1
for term, df in vocab.items():
    idf[term] = math.log((N + 1) / (df + 1)) + 1.0

term_index = {t:i for i,(t,_) in enumerate(sorted(idf.items(), key=lambda x: x[0]))}

with outp.open("w", encoding="utf-8") as f:
    for p, toks in docs:
        tf = collections.Counter(toks)
        indices = []
        values = []
        for term, cnt in tf.items():
            if term in term_index:
                indices.append(term_index[term])
                values.append((cnt / len(toks)) * idf[term])
        rec = {
            "id": f"kb::{p.stem}",
            "sparse": {"indices": indices, "values": values}
        }
        f.write(json.dumps(rec) + "\n")

print(str(outp))
