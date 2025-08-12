import sys
import argparse
import runpy
from pathlib import Path

# Reuse the verifier if available
try:
    from .cli import main as verify_main
except Exception:
    verify_main = None

BIN_PREFIX = "kilo.tools.bin."

def _run_bin(mod_basename: str):
    """Run a packaged script module under kilo_tools.bin as __main__."""
    return runpy.run_module(BIN_PREFIX + mod_basename, run_name="__main__")


def cmd_build_kb(args):        return _run_bin("build_kb_jsonl")
def cmd_build_sparse(args):    return _run_bin("build_sparse")
def cmd_embed_text(args):      return _run_bin("embed_text")
def cmd_ingest_qdrant(args):   return _run_bin("ingest_qdrant")
def cmd_check_mb_tokens(args): return _run_bin("check_mb_tokens")
def cmd_test_mode_pins(args):  return _run_bin("test_mode_pins")
def cmd_prompt_assemble(args):
    # Invoke Python wrapper which delegates to Node/TS
    from kilo.prompt_assembler.runner import main as pa_main
    return pa_main([])


def main(argv=None):
    parser = argparse.ArgumentParser(prog="kilo", description="Kilo Code unified CLI")
    sub = parser.add_subparsers(dest="command", metavar="<command>")
    sub.required = True


    sub.add_parser("build-kb", help="Build KB JSONL from memory_bank").set_defaults(func=cmd_build_kb)
    sub.add_parser("build-sparse", help="Build sparse embeddings / index").set_defaults(func=cmd_build_sparse)
    sub.add_parser("embed-text", help="Embed text via OpenAI").set_defaults(func=cmd_embed_text)
    sub.add_parser("ingest-qdrant", help="Ingest data into Qdrant").set_defaults(func=cmd_ingest_qdrant)
    sub.add_parser("check-mb-tokens", help="Check Memory Bank token counts").set_defaults(func=cmd_check_mb_tokens)
    sub.add_parser("test-mode-pins", help="Test mode knowledge pins").set_defaults(func=cmd_test_mode_pins)
    sub.add_parser("prompt-assemble", help="Run the TypeScript prompt_assembler via Python wrapper").set_defaults(func=cmd_prompt_assemble)

    args = parser.parse_args(argv)
    res = args.func(args)
    # Normalize return to exit code
    if isinstance(res, int):
        return res
    return 0

if __name__ == "__main__":
    sys.exit(main())
