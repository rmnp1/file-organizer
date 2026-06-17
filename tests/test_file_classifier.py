import pytest

from application.services.file_classifier import FileClassifier


@pytest.fixture
def file_classifier():
    return FileClassifier()


@pytest.mark.parametrize("extension, expected_category", [
    ("txT", "Documents"),
    ("", "Other"),
    ("   ", "Other"),
    ("jPg", "Images"),
    ("png", "Images"),
    ("mp3", "Audio"),
    ("mp4", "Video"),
    ("EXE", "Applications"),
    ("zip", "Archives"),
    ("doc", "Documents"),
    ("ppt", "Documents"),
    ("xls", "Documents"),
    ("unknown", "Other"),
])
def test_classify_file(file_classifier, extension, expected_category):
    assert file_classifier.classify(extension) == expected_category