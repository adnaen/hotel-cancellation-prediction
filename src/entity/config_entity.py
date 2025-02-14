from pathlib import Path
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    source_url: str
    download_path: Path


@dataclass
class DataCleaningConfig:
    input_path: Path
    df_output_path: Path
    columns_to_drop: list[str]
    dtype_convertion: dict[str, str]
    missing_values: dict[str, str | list[str]]
    outlier_columns: dict[str, str | list[str]]


@dataclass
class DataValidationConfig:
    input_path: Path
    dtypes: dict[str, int]
    shape: dict[str, int]


@dataclass
class DataPreprocessingConfig:
    df_input_path: Path
    encodings: dict[str, list]
    numerical_features: list[str]
    test_output_path: Path
    train_output_path: Path
    pipeline_path: Path


@dataclass
class ModelSelectionConfig:
    train_input_path: Path
    params: dict
    best_model_info_path: Path


@dataclass
class ModelTrainingConfig:
    train_input_path: Path
    preprocessor_path: Path
    best_model: str
    best_params: dict
    pipeline_path: Path
