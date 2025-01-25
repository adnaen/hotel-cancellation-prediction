import gdown
import yaml
from pathlib import Path
import os
from src.config import logger


def from_gdrive(url: str, filename: Path) -> bool:
    if not os.path.exists(filename):
        create_path(filename)
        gdown.download(url=url, output=filename, quiet=False)
        logger.info(f"dataset downloaded at: {filename}")
        return True
    logger.info(f"dataset already exist at {filename}")
    return False


def load_yaml(absolute_path: Path) -> dict:
    """read .yml file and return its content"""
    with open(absolute_path, "r") as file:
        content = yaml.safe_load(file)
    logger.info(f"load yaml file from {absolute_path}")
    return content


def create_path(absolute_path: Path) -> bool:
    if not isinstance(absolute_path, Path):
        absolute_path = Path(absolute_path)
    if absolute_path.suffix:
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        absolute_path.touch()
        logger.info(f"file has been created at: {absolute_path}")
        return True
    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"folder has been created at: {absolute_path}")
    return True
