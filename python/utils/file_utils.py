from pathlib import Path


def get_file_path(filename: str, module_file_path: str) -> Path:
    """Return the absolute path to the file located next to the problem module file"""
    return Path(module_file_path).resolve().with_name(filename)
