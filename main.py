import os
from pathlib import Path
import logging

from application.organize_files_use_case import OrganizeFilesUseCase
from application.services.file_classifier import FileClassifier
from infrastructure.file_system.file_scanner import FileScanner
from infrastructure.file_system.file_mover import FileMover
from infrastructure.logging.logging_configuration import LoggingConfiguration

logger = logging.getLogger(__name__)

def get_directory() -> Path:
    directory_env = os.getenv("TARGET_DIR")

    directory_raw = directory_env if directory_env else input("Enter the directory to organize: ")
    return Path(directory_raw.strip()).expanduser().resolve()

def main() -> None:
    """
    Initializes application components
    and starts the file organization process.
    """

    LoggingConfiguration.setup()

    directory = get_directory()

    logger.info("Organizing files started.")

    mover = FileMover()
    classifier = FileClassifier()
    scanner = FileScanner()

    use_case = OrganizeFilesUseCase(mover, classifier, scanner)
    use_case.execute(directory)


if __name__ == '__main__':
    main()