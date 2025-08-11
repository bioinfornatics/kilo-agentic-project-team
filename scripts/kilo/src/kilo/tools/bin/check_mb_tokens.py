"""Estimate token budgets for memory_bank/*.md and fail if any doc exceeds threshold.
Heuristic: tokens ≈ ceil(words / 0.75). Default threshold: 800 tokens.
Usage: python scripts/check_mb_tokens.py [--max 800]
"""
import argparse, math, pathlib, re, sys, json
root = pathlib.Path(__file__).resolve().parents[1]
mem = root / "memory_bank"

def estimate_tokens(text: str) -> int:
    words = re.findall(r"\w+", text)
    return math.ceil(len(words) / 0.75)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=800)
    args = ap.parse_args()
    too_big = []
    report = {}
    for p in sorted(mem.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        tk = estimate_tokens(t)
        report[p.name] = tk
        if tk > args.max:
            too_big.append({"file": p.name, "tokens": tk, "max": args.max})
    print(json.dumps({"token_estimate": report, "violations": too_big}, indent=2))
    sys.exit(0 if not too_big else 4)

if __name__ == "__main__":
    main()
