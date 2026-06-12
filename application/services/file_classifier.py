from domain.rules.extension_mapping import EXTENSION_MAPPING


class FileClassifier:
    """Classifies files into categories based on their extensions."""

    def __init__(self):
        self.extensions = EXTENSION_MAPPING

    def classify(self, extension: str) -> str:
        return self.extensions.get(extension.lower(), "Other")
