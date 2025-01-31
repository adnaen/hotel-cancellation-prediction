import pandas as pd
from pathlib import Path
from typing import Any

from src.config import logger
from src.utils import is_exists, create_path


def load_csv(path: Path, **kwargs) -> pd.DataFrame:
    if is_exists(path):
        logger.info(f"dataset load from {path}")
        return pd.read_csv(path, **kwargs)
    logger.error(f"path not exist : {path}")


def dump_csv(path: Path, df: pd.DataFrame, **kwargs) -> bool:
    if is_exists(path):
        logger.info(f"dataset already exists on : {path}")
        return True
    create_path(path)
    df.to_csv(path, index=False, **kwargs)
    logger.info(f"dataset stored in {path}")
    return True


def to_dataframe(data: Any, **kwargs) -> pd.DataFrame:
    return pd.DataFrame(data, **kwargs)
