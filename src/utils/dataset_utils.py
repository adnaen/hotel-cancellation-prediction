import pandas as pd
from pathlib import Path


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def save_csv(path: Path, df: pd.DataFrame) -> None:
    df.to_csv(path)
