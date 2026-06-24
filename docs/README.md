# File Organizer

A Python application that automatically organizes files inside a directory by categorizing them into dedicated folders based on their file extensions.

The application scans a directory, classifies files (images, documents, videos, archives, audio files, and more), and moves them into corresponding folders to maintain a clean and structured filesystem.

![Python](https://img.shields.io/badge/Python-3.14+-blue)
![Architecture](https://img.shields.io/badge/Architecture-Layered-orange)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)
![Package Manager](https://img.shields.io/badge/Package_Manager-uv-purple)

---

## Features

- Automatically organizes files by category
- Supports multiple file types and extensions
- Creates destination folders automatically
- Prevents file overwriting by generating unique filenames
- Handles invalid directories and unexpected errors gracefully
- Provides centralized JSON logging
- Includes unit and integration tests
- Supports Windows, macOS, and Linux

---

## Architecture

The project follows a layered architecture that separates business logic, domain rules, and infrastructure concerns into independent layers.

### Project Structure

```text
file_organizer/
│
├── application/
│   ├── organize_files_use_case.py
│   └── services/
│       └── file_classifier.py
│
├── domain/
│   ├── entities/
│   │   └── file_info.py
│   └── rules/
│       └── extension_mapping.py
│
├── infrastructure/
│   ├── file_system/
│   │   ├── file_scanner.py
│   │   └── file_mover.py
│   │
│   └── logging/
│       └── logging_configuration.py
│
├── tests/
│
└── main.py
```

### Domain Layer

Contains the core entities and business rules.

| Component | Responsibility |
|-----------|----------------|
| `FileInfo` | Represents file metadata |
| `EXTENSION_MAPPING` | Defines file categorization rules |

### Application Layer

Contains the application's business logic.

| Component | Responsibility |
|-----------|----------------|
| `OrganizeFilesUseCase` | Coordinates the file organization workflow |
| `FileClassifier` | Maps file extensions to categories |

### Infrastructure Layer

Handles communication with the operating system and external libraries.

| Component | Responsibility |
|-----------|----------------|
| `FileScanner` | Scans directories and retrieves files |
| `FileMover` | Moves files to destination folders |
| `LoggingConfiguration` | Configures centralized logging |

### Entry Point

`main.py` is responsible for:

- collecting user input
- initializing application dependencies
- executing the file organization workflow

---

## Supported Categories

| Category | Extensions |
|----------|------------|
| Images | jpg, jpeg, png, gif, bmp, svg, webp, tiff, ico, heic |
| Documents | pdf, doc, docx, txt, md, csv, xls, xlsx, ppt, pptx, odt, ods |
| Audio | mp3, wav, flac, m4a, aac, ogg, wma |
| Video | mp4, mkv, avi, mov, wmv, flv, webm, mpeg |
| Archives | zip, rar, 7z, tar, gz |
| Applications | exe, msi, dmg, pkg, deb, rpm, apk |
| Development | py, js, ts, html, css, json, xml, yaml, yml, sh, bat, c, cpp, java, go |
| Books | epub, mobi, fb2, djvu |
| Design | psd, ai, fig, blend, dwg, stl |
| Other | Unsupported file types |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rmnp1/file-organizer.git

cd file-organizer
```

Install dependencies:

```bash
uv sync
```

---

## Usage

Run the application:

```bash
uv run main.py
```

The application will prompt for a directory path:

```text
Enter the directory to organize:
```

Examples:

```text
~/Desktop/Downloads
```

```text
C:\Users\Username\Downloads
```

---

## Running Tests

Run all tests:

```bash
uv run pytest
```

## Logging

The application uses centralized JSON logging to provide visibility into the execution flow.

Example:

```json
{
  "time": "2026-06-22 20:41:23",
  "level": "INFO",
  "msg": "File 'photo.jpg' moved to 'Images/photo.jpg'"
}
```

---

## Technologies

- Python
- uv
- pathlib
- shutil
- logging
- dataclasses
- pytest
- python-json-logger

---

## Learning Objectives

This project was built to practice:

- Layered Architecture
- Object-Oriented Programming (OOP)
- Dependency Injection
- Filesystem operations
- Error handling
- Centralized logging
- Automated testing with Pytest
- Writing maintainable and modular Python code

---

## License

This project was created for educational and portfolio purposes.