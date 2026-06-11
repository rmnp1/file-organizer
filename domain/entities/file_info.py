from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Fileinfo:
    path: Path
    filename: str
    extension: str
