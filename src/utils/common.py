import gdown
import os
from pathlib import Path
from src.config import logger


def from_gdrive(url: str, filename: Path) -> bool:
    """
    Download content with it url from google drive.

    Args:
        url (str) : google drive file url <warn: must be accessble>
        filename (Path) : path to store the file

    Returns:
        bool : status
    """
    if not is_exists(filename):
        create_path(filename)
        status = gdown.download(url=url, output=str(filename), quiet=False)
        if status:
            logger.info(f"dataset downloaded at: {filename}")
            return True
        else:
            logger.error("failed to download dataset!!!")
            return True

    logger.info(f"dataset already exist at {filename}")
    return False


def create_path(absolute_path: Path | str) -> bool:
    """
    create all folders/files with the path if it not exist

    Args:
        absolute_path (Path | str) : absolute path to be created.

    Returns:
        bool : status
    """
    if not isinstance(absolute_path, Path):
        absolute_path = Path(absolute_path)

    if absolute_path.suffix:
        absolute_path = absolute_path.parent

    if is_exists(absolute_path):
        logger.info(f"folder has already exist at: {absolute_path}")
        return False
    absolute_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"folder has been created at: {absolute_path}")
    return True


def is_exists(path: str | Path) -> bool:
    """
    Check if the path does exists.

    Args:
        path (str | Path) : path to check

    Returns:
        bool : status
    """
    return os.path.exists(path)
