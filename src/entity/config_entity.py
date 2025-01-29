from pathlib import Path
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    source_url: str
    download_path: Path


@dataclass
class DataCleaningConfig:
    input_path: Path
    output_path: Path
    columns_to_drop: list[str]
    dtype_convertion: dict[str, str]
    missing_values: dict[str, str | list[str]]
    outlier_columns: list[str]
