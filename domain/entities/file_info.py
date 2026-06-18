from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FileInfo:
    path: Path
    filename: str
    extension: str

    @classmethod
    def from_path(cls, path: Path):
        return cls(path, path.name, path.suffix)
