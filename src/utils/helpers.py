import gdown
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


def create_path(absolute_path: Path) -> bool:
    """create all folders/files witht the path if it not exist"""

    if not isinstance(absolute_path, Path):
        absolute_path = Path(absolute_path)
    if absolute_path.suffix:
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"parent folder has been created at: {absolute_path}")
        return True
    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"folder has been created at: {absolute_path}")
    return True
