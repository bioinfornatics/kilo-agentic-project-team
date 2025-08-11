"""Simple eval harness for LITM, Needle, Drift (dummy adapters supported)."""
import argparse, json, random, statistics, os, pathlib

def litm_probe(n=12):
    # Simulate edge advantage (lost-in-the-middle)
    # Scores for positions from start->end (1.0 best)
    start = 1.0
    middle = 0.82
    end = 1.0
    pbi = (start + end)/2 - middle
    return {"start": start, "middle": middle, "end": end, "pbi": round(pbi, 2)}

def needle_probe(n=20):
    acc = 0.82
    return {"acc": acc}

def drift_probe(n=10):
    drift = 0.27
    return {"drift": drift}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", choices=["litm","needle","drift","all"], default="all")
    ap.add_argument("-n", type=int, default=10)
    args = ap.parse_args()

    out = {}
    if args.suite in ("litm","all"):
        out["litm"] = litm_probe(args.n)
    if args.suite in ("needle","all"):
        out["needle"] = needle_probe(args.n)
    if args.suite in ("drift","all"):
        out["drift"] = drift_probe(args.n)

    path = pathlib.Path("eval/outputs")
    path.mkdir(parents=True, exist_ok=True)
    with open(path/"summary.json", "w") as f:
        json.dump(out, f, indent=2)
    print(str(path/"summary.json"))

if __name__ == "__main__":
    main()
