import joblib
from typing import Any
from pathlib import Path

from src.config import logger, BasePaths
from src.utils import is_exists


def dump_joblib(path: str | Path, data: Any) -> bool:
    """
    save joblib file to specific path.

    Args:
        path (Path) : path to be stored.
        data (Any) : data to be serialized.

    Returns:
        bool : status
    """
    try:
        abs_path: Path = BasePaths.resolve(path)
        if is_exists(path):
            logger.info(f"{abs_path.name} joblic file already exist on {abs_path}!")
        joblib.dump(filename=path, value=data)
        logger.info(
            f"{abs_path.name} Joblib file has been saved on {abs_path} successfully!"
        )
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
