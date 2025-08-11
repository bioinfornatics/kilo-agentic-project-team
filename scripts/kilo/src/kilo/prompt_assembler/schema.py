from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict

@dataclass(slots=True)
class ModeBlock:
    slug: str
    name: str
    roleDefinition: str
    whenToUse: str
    customInstructions: str
    source_path: Optional[Path] = None

@dataclass(slots=True)
class AssemblerConfig:
    root: Path
    mode: Optional[str] = None
    include_rules: bool = True
    include_footgun: bool = True
    k_cap: int = 12
    edge_anchor: bool = True

@dataclass(slots=True)
class AssemblerOutput:
    content: str
    modes_processed: List[str]
    citations: Dict[str, str]
