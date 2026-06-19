import pytest
from infrastructure.file_system.file_mover import FileMover


@pytest.fixture
def file_mover():
    return FileMover()


def test_move_file_success(file_mover, tmp_path):
    source_file = tmp_path / "document.txt"
    source_file.write_text("hello")
    dest_dir = tmp_path / "target_folder"

    result = file_mover.move(source_file, dest_dir)

    expected_path = dest_dir / "document.txt"
    assert result == expected_path
    assert expected_path.exists()
    assert not source_file.exists()


def test_move_file_handles_duplicate_names(file_mover, tmp_path):
    source_file = tmp_path / "photo.jpg"
    source_file.write_text("data")

    dest_dir = tmp_path / "gallery"
    dest_dir.mkdir()

    (dest_dir / "photo.jpg").write_text("old_data")

    result = file_mover.move(source_file, dest_dir)
    expected_copy_path = dest_dir / "photo_copy1.jpg"
    assert result == expected_copy_path
    assert expected_copy_path.exists()
    assert (dest_dir / "photo.jpg").exists()


def test_move_non_existent_file_raises_error(file_mover, tmp_path):
    non_existent = tmp_path / "ghost.txt"
    dest_dir = tmp_path / "output"

    with pytest.raises(FileNotFoundError) as exc_info:
        file_mover.move(non_existent, dest_dir)

    assert f"File '{non_existent}' does not exist." in str(exc_info.value)

