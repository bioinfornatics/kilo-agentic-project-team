import sys, json
from pathlib import Path
import argparse

REQUIRED_PREFIXES = {
    "roleDefinition": "You are Kilo Code",
    "whenToUse": "Use this mode when",
    "customInstructions": "Your role is to"
}

FOOTGUN_PROMPTS = [
    ("system-prompt-code","Code"),
    ("system-prompt-architect","Architect"),
    ("system-prompt-orchestrator","Orchestrator"),
]

def check_modes(kilocodemodes: Path):
    data = json.loads(kilocodemodes.read_text(encoding="utf-8", errors="replace"))
    modes = data["modes"] if isinstance(data, dict) and "modes" in data else (data if isinstance(data, list) else [data])
    failures = []
    for m in modes:
        slug = m.get("slug","")
        for key, pref in REQUIRED_PREFIXES.items():
            val = (m.get(key,"") or "").strip()
            if not val.startswith(pref):
                failures.append(("mode", slug, key, pref, val[:60]))
    return failures

def head3_ok(lines):
    head = [lines[i].strip() if i < len(lines) else "" for i in range(3)]
    return (
        head[0].startswith(REQUIRED_PREFIXES["roleDefinition"]) and
        head[1].startswith(REQUIRED_PREFIXES["whenToUse"]) and
        head[2].startswith(REQUIRED_PREFIXES["customInstructions"])
    ), head

def check_footgun(kilo_dir: Path):
    failures = []
    for fname, label in FOOTGUN_PROMPTS:
        p = kilo_dir / fname
        if not p.exists():
            failures.append(("prompt_missing", label, fname, "", ""))
            continue
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        ok, head = head3_ok(lines)
        if not ok:
            failures.append(("prompt_prefix", label, fname, "", " | ".join(head[:3])))
    return failures

def main(argv=None):
    parser = argparse.ArgumentParser(description="Kilo Code verifier: prefix-rule and Footgun prompt checks")
    parser.add_argument("--root", default=".", help="Project root (where .kilocodemodes and .kilo live)")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    km = root / ".kilocodemodes"
    kd = root / ".kilo"

    errors = []
    if not km.exists():
        errors.append(("missing", ".kilocodemodes", str(km), "", ""))
    if not kd.exists():
        errors.append(("missing", ".kilo", str(kd), "", ""))

    if not errors:
        errors.extend(check_modes(km))
        errors.extend(check_footgun(kd))

    if errors:
        print("❌ kilo-verify: FAIL")
        for e in errors:
            print(" -", e)
        return 1

    print("✅ kilo-verify: PASS — Prefix rules and Footgun prompts are valid")
    return 0

