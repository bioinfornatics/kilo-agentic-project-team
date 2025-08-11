import runpy

def _run(mod_name: str):
    # Execute the module as if run with `python -m <module>`
    return runpy.run_module(mod_name, run_name="__main__")

def build_kb_jsonl():
    return _run("kilo_tools.bin.build_kb_jsonl")

def build_sparse():
    return _run("kilo_tools.bin.build_sparse")

def check_mb_tokens():
    return _run("kilo_tools.bin.check_mb_tokens")

def embed_text():
    return _run("kilo_tools.bin.embed_text")

def ingest_qdrant():
    return _run("kilo_tools.bin.ingest_qdrant")

def test_mode_pins():
    return _run("kilo_tools.bin.test_mode_pins")
