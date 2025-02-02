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
    """
    Check if the path does exists.

    Args:
        path (str | Path) : path to check
        else_create (bool) : create the path if is not exists.

    Returns:
        bool : status
    """
    if else_create:
        return create_path(path)
    return os.path.exists(path)


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

    absolute_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"folder has been created at: {absolute_path}")
    return True
