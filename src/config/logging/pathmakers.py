import os
from pathlib import Path
from typing import Union


def make_base_log_directory(path: Union[Path, str]) -> Path:
    """Method for creating the root log folder."""

    if isinstance(path, str):
        path = Path(path).resolve()

    path /= "logs"

    path.mkdir(parents=True, exist_ok=True)
    return path


def make_log_path(base_log_dir: Union[Path, str], module_name: str) -> str:
    log_path: str = os.path.join(
        str(base_log_dir),
        module_name,
        "{time:YYYY-MM-DD}",
        "{time:YYYY-MM-DD_HH}.log",
    )
    return log_path
