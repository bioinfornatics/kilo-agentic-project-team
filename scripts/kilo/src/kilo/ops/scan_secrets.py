"""Scan staged diffs for secrets (simple patterns + entropy heuristic)."""
import re, sys, json, math
import subprocess

PATTERNS = [
    r"AKIA[0-9A-Z]{16}",
    r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}",
    r"-----BEGIN (RSA|EC|DSA) PRIVATE KEY-----",
]

def entropy(s: str):
    import math
    counts = {c:s.count(c) for c in set(s)}
    probs = [c/len(s) for c in counts.values()]
    return -sum(p*math.log2(p) for p in probs)

def main():
    try:
        diff = subprocess.check_output(["git","diff","--staged"], text=True, stderr=subprocess.DEVNULL)
    except Exception:
        diff = ""
    findings = []
    for i, line in enumerate(diff.splitlines(), 1):
        for pat in PATTERNS:
            if re.search(pat, line):
                findings.append({"line": i, "pattern": pat, "text": line.strip()})
        tokens = re.findall(r"[A-Za-z0-9+/]{24,}={0,2}", line)
        for t in tokens:
            if entropy(t) > 3.5:
                findings.append({"line": i, "pattern": "entropy", "text": t[:8]+"..."})
    if findings:
        print(json.dumps({"findings": findings}, indent=2))
        sys.exit(2)
    print("No secrets found.")

if __name__ == "__main__":
    main()
