from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable, List, Tuple
from .schema import ModeBlock

def _iter_modes_from_kilocodemodes(path: Path) -> Iterable[ModeBlock]:
    raw = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    arr = raw["modes"] if isinstance(raw, dict) and "modes" in raw else (raw if isinstance(raw, list) else [raw])
    for m in arr:
        slug = (m.get("slug") or "").strip()
        name = (m.get("name") or "").strip()
        rd = (m.get("roleDefinition") or "").strip()
        wtu = (m.get("whenToUse") or "").strip()
        ci = (m.get("customInstructions") or "").strip()
        if slug:
            yield ModeBlock(slug=slug, name=name, roleDefinition=rd, whenToUse=wtu, customInstructions=ci, source_path=path)

def load_all_modes(root: Path) -> List[ModeBlock]:
    km = root / ".kilocodemodes"
    if not km.exists():
        raise FileNotFoundError(f".kilocodemodes not found at {km}")
    return list(_iter_modes_from_kilocodemodes(km))

def load_footgun_prompts(root: Path) -> List[Tuple[str, Path, str]]:
    kilo = root / ".kilo"
    out: List[Tuple[str, Path, str]] = []
    if not kilo.exists():
        return out
    for name in ["system-prompt-code", "system-prompt-architect", "system-prompt-orchestrator"]:
        p = kilo / name
        if p.exists():
            out.append((name.replace("system-prompt-", ""), p, p.read_text(encoding="utf-8", errors="replace")))
    return out

def load_rule_snippets(root: Path, max_chars: int = 1000) -> List[Tuple[Path, str]]:
    base = root / ".kilocode"
    acc: List[Tuple[Path, str]] = []
    if not base.exists():
        return acc
    for p in base.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")[:max_chars]
            acc.append((p, txt))
        except Exception:
            continue
    return acc
