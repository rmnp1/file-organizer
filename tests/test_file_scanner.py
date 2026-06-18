from pathlib import Path

import pytest

from infrastructure.file_system.file_scanner import FileScanner


@pytest.fixture
def file_scanner():
    return FileScanner()

def test_scan_directory(file_scanner):
    directory = "tests"
    files = file_scanner.scan(directory)
    assert len(files) > 0

def test_scan_non_existent_directory(file_scanner):
    directory = "non_existent_directory"
    files = file_scanner.scan(directory)
    assert len(files) == 0

