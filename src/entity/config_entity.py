from pathlib import Path
from dataclasses import dataclass

#
# Data schema for Pipeline Configuration
#


@dataclass
class DataIngestionConfig:
    source_url: str
    download_path: Path


@dataclass
class DataTransformationConfig:
    input_path: Path
    x_output_path: Path
    y_output_path: Path
    columns_to_drop: list[str]
    dtype_convertion: dict[str, str]
    missing_values: dict[str, str | list[str]]
    outlier_columns: dict[str, str | list[str]]
    encodings: dict[str, list[str]]
    target_variable: str
    numerical_cols: list[str]
    categorical_cols: list[str]


@dataclass
class DataValidationConfig:
    input_path: Path
    dtypes: dict[str, int]
    shape: dict[str, int]
