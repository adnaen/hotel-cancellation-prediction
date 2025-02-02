import joblib
from typing import Any
from pathlib import Path

from src.config import logger
from src.utils import is_exists


def dump_joblib(path: Path, data: Any) -> bool:
    """
    save joblib file to specific path.

    Args:
        path (Path) : path to be stored.
        data (Any) : data to be serialized.

    Returns:
        bool : status
    """
    try:
        if is_exists(path):
            logger.info(f"{path.name} joblic file already exist on {path}!")
        joblib.dump(filename=path, value=data)
        logger.info(f"{path.name} Joblib file has been saved on {path} successfully!")
        return True
    except Exception as e:
        logger.error("error occured in dump joblib function", e)
        return False


def load_joblib(path: Path) -> Any:
    """
    load joblib file and return.

    Args:
        path (Path) : path to be load joblib file.

    Returns:
        Any : joblib file data

    Raises:
        FileNotFoundError : when the file not exists.
    """
    try:
        if not is_exists(path):
            logger.error(f"{path} file not exists!")
            raise FileNotFoundError
        logger.info(f"{path} successfully loaded!")
        return joblib.load(filename=path)
    except Exception as e:
        logger.error(f"error while load {path} joblib file! : {e}")
        raise e
