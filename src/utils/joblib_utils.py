import joblib
from typing import Any
from pathlib import Path

from src.config import logger
from src.utils import is_exists


def dump_joblib(path: Path, data: Any) -> bool:
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
    try:
        if not is_exists(path):
            logger.error(f"{path} file not exists!")
            return
        logger.info(f"{path} successfully loaded!")
        return joblib.load(filename=path)
    except Exception as e:
        logger.error(f"error while load {path} joblib file! : {e}")
