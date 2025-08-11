"""Enforce THIRD_PARTY_NOTICES.md updates when dependencies change (package.json/yarn.lock/pnpm-lock)."""
import os, subprocess, sys, json

NOTICE = "THIRD_PARTY_NOTICES.md"
DEPS = ["package.json","yarn.lock","pnpm-lock.yaml","package-lock.json"]

def main():
    try:
        diff = subprocess.check_output(["git","diff","--name-only","--staged"], text=True)
    except Exception:
        diff = ""
    changed = [f for f in diff.splitlines() if any(f.endswith(x) for x in DEPS)]
    if changed and NOTICE not in diff:
        print(f"Dependencies changed: {changed}. Update {NOTICE} before commit.")
        sys.exit(2)
    print("Dependency notices OK.")

if __name__ == "__main__":
    main()
