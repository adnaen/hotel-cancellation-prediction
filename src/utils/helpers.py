import gdown
import yaml
from pathlib import Path
import os


def from_gdrive(url: str, filename: Path) -> bool:
    if not os.path.exists(filename):
        gdown.download(url=url, output=filename, quiet=False)
        return True
    return False


def load_yaml(absolute_path: Path) -> dict:
    """read .yml file and return its content"""
    with open(absolute_path, "r") as file:
        content = yaml.safe_load(file)
    return content
