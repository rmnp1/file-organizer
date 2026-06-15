from pathlib import Path

from application.organize_files_use_case import OrganizeFilesUseCase
from application.services.file_classifier import FileClassifier
from infrastructure.file_system.file_scanner import FileScanner
from infrastructure.file_system.file_mover import FileMover
from infrastructure.logging.logging_configuration import LoggingConfiguration

def get_directory() -> Path:
    directory = Path(input("Enter the directory to organize: ").strip())
    return directory

def main() -> None:
    LoggingConfiguration.setup()

    directory = get_directory()

    mover = FileMover()
    classifier = FileClassifier()
    scanner = FileScanner()

    use_case = OrganizeFilesUseCase(mover, classifier, scanner)
    use_case.execute(directory)


if __name__ == '__main__':
    main()