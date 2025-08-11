from __future__ import annotations
from typing import List, Tuple
from .schema import ModeBlock

REQUIRED_PREFIXES = {
    "roleDefinition": "You are Kilo Code",
    "whenToUse": "Use this mode when",
    "customInstructions": "Your role is to",
}

def validate_prefixes(modes: List[ModeBlock]) -> List[Tuple[str, str]]:
    failures: List[Tuple[str, str]] = []
    for m in modes:
        if not m.roleDefinition.startswith(REQUIRED_PREFIXES["roleDefinition"]):
            failures.append((m.slug, "roleDefinition must start with 'You are Kilo Code'"))
        if not m.whenToUse.startswith(REQUIRED_PREFIXES["whenToUse"]):
            failures.append((m.slug, "whenToUse must start with 'Use this mode when'"))
        if not m.customInstructions.startswith(REQUIRED_PREFIXES["customInstructions"]):
            failures.append((m.slug, "customInstructions must start with 'Your role is to'"))
    return failures
