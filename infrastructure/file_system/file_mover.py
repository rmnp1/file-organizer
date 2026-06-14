import shutil
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class FileMover:
    def move(self, source: Path, destination_dir: Path):
        """Moves files into destination directories."""

        if not source.is_file():
            logger.warning(f"File '{source}' does not exist.")
            raise FileNotFoundError(f"File '{source}' does not exist.")

        destination_dir.mkdir(parents=True, exist_ok=True)

        destination_path = destination_dir / source.name

        count = 1
        while destination_path.exists():
            destination_path = destination_dir / f"{source.stem}_copy{count}{source.suffix}"
            count += 1

        result_path = shutil.move(str(source), str(destination_path))
        logger.info(f"File '{source}' moved to '{result_path}'.")
        return Path(result_path)




