from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class OrganizeFilesUseCase:
    def __init__(
            self,
            mover: "FileMover",
            classifier: "FileClassifier",
            scanner: "FileScanner"
    ):
        self._mover = mover
        self._classifier = classifier
        self._scanner = scanner

    def execute(self, directory: Path):
        """Organizes files in the specified directory."""

        logger.info(f"Organizing files in directory: {directory}")

        files = self._scanner.scan(directory)

        if not files:
            logger.warning("No files found in the specified directory.")
            return

        logger.info(f"Found {len(files)} files to organize.")

        for file in files:
            try:
                category = self._classifier.classify(file.extension)
                destination_dir = directory / category

                self._mover.move(
                    file.path,
                    destination_dir
                )
            except Exception as e:
                logger.error(f"Error processing file '{file.path}': {e}")

        logger.info("Files organized successfully.")