"""Validate .kilocodemodes:
 - Each mode's customInstructions begins with:
     1) "Your role is to ..."
     2) "Use this mode when ..."
 - All @memory_bank/<file>.md pins exist.
Exit non‑zero on failure. Prints a JSON summary.
"""
import json, sys, re, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
modes_path = root / ".kilocodemodes"
mem_dir = root / "memory_bank"

def main():
    if not modes_path.exists():
        print(json.dumps({"error": ".kilocodemodes not found"})); sys.exit(2)
    data = json.loads(modes_path.read_text(encoding="utf-8"))
    failures = []
    summary = {}
    for m in data.get("customModes", []):
        slug = m.get("slug")
        ci = (m.get("customInstructions") or "").strip().splitlines()
        role_ok = len(ci) >= 1 and ci[0].lower().startswith("your role is to")
        when_ok = len(ci) >= 2 and ci[1].lower().startswith("use this mode when")
        pins = [ln.strip()[2:].strip() for ln in ci if ln.strip().startswith("- @")]
        pins_ok = True
        missing = []
        for p in pins:
            if p.startswith("memory_bank/"):
                if not (mem_dir / p.split("memory_bank/")[1]).exists():
                    pins_ok = False
                    missing.append(p)
        summary[slug] = {"role_ok": role_ok, "when_ok": when_ok, "pins": pins, "pins_ok": pins_ok, "missing": missing}
        if not (role_ok and when_ok and pins_ok):
            failures.append(slug)
    print(json.dumps({"summary": summary, "failures": failures}, indent=2))
    sys.exit(0 if not failures else 3)

if __name__ == "__main__":
    main()
