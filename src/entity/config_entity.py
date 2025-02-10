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
    x_train_output_path: Path
    x_test_output_path: Path
    y_train_output_path: Path
    y_test_output_path: Path
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


@dataclass
class ModelTrainingConfig:
    x_train_inutput_path: Path
    y_train_inutput_path: Path
    encodings: dict[str, list]
