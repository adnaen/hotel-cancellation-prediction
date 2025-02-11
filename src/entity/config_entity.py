from pathlib import Path
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    source_url: str
    download_path: Path


@dataclass
class DataCleaningConfig:
    input_path: Path
    x_output_path: Path
    y_output_path: Path
    columns_to_drop: list[str]
    dtype_convertion: dict[str, str]
    missing_values: dict[str, str | list[str]]
    outlier_columns: dict[str, str | list[str]]
    target_variable: str


@dataclass
class DataValidationConfig:
    input_path: Path
    dtypes: dict[str, int]
    shape: dict[str, int]


@dataclass
class DataPreprocessingConfig:
    x_input_path: Path
    y_input_path: Path
    encodings: dict[str, list]
    numerical_features: list[str]
    x_output_path: Path
    pipeline_path: Path
