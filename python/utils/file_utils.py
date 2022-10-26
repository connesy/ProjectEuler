from pathlib import Path


def get_file_path(filename: str, module_file_path: str) -> Path:
    """Return the absolute path to a filename located next to the problem module file"""
    return Path(module_file_path).resolve().with_name(filename)


def read_data_file(*, module_file_path: str) -> list[str]:
    """Return the contents of the data file located next to the problem module file"""
    data_filepath = get_file_path("data.txt", module_file_path)
    with data_filepath.open() as file:
        return file.read().splitlines()
