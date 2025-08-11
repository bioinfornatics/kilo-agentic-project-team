from __future__ import annotations
from pathlib import Path
from typing import List, Dict
from .schema import AssemblerConfig, AssemblerOutput, ModeBlock
from .validators import validate_prefixes
from .loader import load_all_modes, load_footgun_prompts, load_rule_snippets

def _assemble_for_mode(m: ModeBlock, citations: Dict[str, str]) -> str:
    parts: List[str] = []
    parts.append(f"## Mode: {m.name} (`{m.slug}`)")
    parts.append("### Role Definition")
    parts.append(m.roleDefinition)
    parts.append("### When To Use")
    parts.append(m.whenToUse)
    parts.append("### Custom Instructions")
    parts.append(m.customInstructions)
    if m.source_path:
        key = f"mode:{m.slug}"
        citations[key] = str(m.source_path)
        parts.append(f"\n*Source:* [{key}]")
    return "\n".join(parts)

def assemble(cfg: AssemblerConfig) -> AssemblerOutput:
    root = cfg.root
    citations: Dict[str, str] = {}
    modes = load_all_modes(root)
    if cfg.mode:
        modes = [m for m in modes if m.slug == cfg.mode]
        if not modes:
            raise ValueError(f"Mode '{cfg.mode}' not found in .kilocodemodes")
    failures = validate_prefixes(modes)
    if failures:
        lines = "\n".join([f"- {slug}: {reason}" for slug, reason in failures])
        raise ValueError("Prefix rule violations:\n" + lines)
    out_parts: List[str] = []
    out_parts.append("# Assembled Prompts")
    out_parts.append(f"_Root: {root}_")
    if cfg.mode:
        out_parts.append(f"_Mode filter: `{cfg.mode}`_")
    out_parts.append("")
    if cfg.include_footgun:
        fgs = load_footgun_prompts(root)
        if fgs:
            out_parts.append("## Footgun Overrides (overview)")
            for label, path, _txt in fgs:
                key = f"footgun:{label}"
                citations[key] = str(path)
                out_parts.append(f"- {label} → [{key}]")
            out_parts.append("")
    if cfg.include_rules:
        rules = load_rule_snippets(root, max_chars=500)
        if rules:
            out_parts.append("## Project Rules (snippets)")
            for p, snippet in rules[: cfg.k_cap]:
                key = f"rule:{p.name}"
                citations[key] = str(p)
                out_parts.append(f"### {p.name}")
                out_parts.append(snippet.strip())
                out_parts.append("")
    out_parts.append("## Modes")
    for m in modes[: cfg.k_cap]:
        out_parts.append(_assemble_for_mode(m, citations))
        out_parts.append("")
    out_parts.append("---")
    out_parts.append("## Citations (path map)")
    for k, v in citations.items():
        out_parts.append(f"- {k} → {v}")
    content = "\n".join(out_parts).strip() + "\n"
    return AssemblerOutput(content=content, modes_processed=[m.slug for m in modes], citations=citations)
