from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from .schema import AssemblerConfig
from .assembler import assemble


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="kilo prompt-assemble", description="Assemble prompts from project files (.kilocodemodes, .kilo, .kilocode)")
    parser.add_argument("--root", default=".", help="Project root (contains .kilocodemodes, .kilo, .kilocode)")
    parser.add_argument("--mode", default=None, help="Optional mode slug to assemble only that mode (e.g., code-nextjs)")
    parser.add_argument("--no-rules", action="store_true", help="Do not include .kilocode/rules snippets")
    parser.add_argument("--no-footgun", action="store_true", help="Do not include .kilo/system-prompt-* overview")
    parser.add_argument("--out", default=None, help="Output file path (markdown). If omitted, prints to stdout.")
    args = parser.parse_args(argv)

    cfg = AssemblerConfig(
        root=Path(args.root).resolve(),
        mode=args.mode,
        include_rules=not args.no_rules,
        include_footgun=not args.no_footgun,
    )
    out = assemble(cfg)
    if args.out:
        Path(args.out).write_text(out.content, encoding="utf-8")
    else:
        print(out.content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
