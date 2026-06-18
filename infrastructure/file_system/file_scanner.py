from domain.entities.file_info import FileInfo
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class FileScanner:
    """Scans a directory for files and returns a list of FileInfo objects."""
    
    def scan(self, directory: Path) -> list[FileInfo]:
        dir_path = Path(directory)
        results = []

        if not dir_path.is_dir():
            logger.warning(f"Directory '{directory}' does not exist.")
            return []

        try:
            for path in dir_path.iterdir():
                if path.is_file():
                    results.append(FileInfo.from_path(path))
        except OSError as e:
            logger.error(f"Error scanning directory '{directory}': {e}")

        return results

