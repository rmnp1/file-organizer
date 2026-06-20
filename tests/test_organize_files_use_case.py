import pytest

from application.organize_files_use_case import OrganizeFilesUseCase
from application.services.file_classifier import FileClassifier
from infrastructure.file_system.file_mover import FileMover
from infrastructure.file_system.file_scanner import FileScanner


@pytest.fixture
def organize_files_use_case():
    return OrganizeFilesUseCase(
        mover=FileMover(),
        classifier=FileClassifier(),
        scanner=FileScanner()
    )

def test_execute(organize_files_use_case, tmp_path):
    photo = tmp_path / "photo.jpg"
    document = tmp_path / "report.pdf"

    photo.touch()
    document.touch()

    organize_files_use_case.execute(tmp_path)

    assert (tmp_path / "Images" / "photo.jpg").exists()

    assert (tmp_path / "Documents" / "report.pdf").exists()

    assert not photo.exists()

    assert not document.exists()