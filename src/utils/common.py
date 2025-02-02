import gdown
import os
from pathlib import Path
from src.config import logger


def from_gdrive(url: str, filename: Path) -> bool:
    if not filename.exists():
        create_path(filename)
        status = gdown.download(url=url, output=str(filename), quiet=True)
        if status:
            logger.info(f"dataset downloaded at: {filename}")
            return True
        else:
            logger.error("failed to download dataset!!!")
            return True

    logger.info(f"dataset already exist at {filename}")
    return False


def is_exists(path: str | Path, else_create: bool = False) -> bool:
    if else_create:
        return create_path(path)
    return os.path.exists(path)


def create_path(absolute_path: Path | str) -> bool:
    """create all folders/files witht the path if it not exist"""

    if not isinstance(absolute_path, Path):
        absolute_path = Path(absolute_path)

    if absolute_path.suffix:
        absolute_path = absolute_path.parent

    absolute_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"folder has been created at: {absolute_path}")
    return True
