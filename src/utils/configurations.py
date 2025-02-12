from src.entity import (
    DataIngestionConfig,
    DataCleaningConfig,
    DataValidationConfig,
    DataPreprocessingConfig,
)
from src.utils import get_config
from src.config import BasePaths


class ConfigControl:
    config = get_config(yaml_path=BasePaths.resolve("config/stages.yml"))
    schema = get_config(yaml_path=BasePaths.resolve("config/schema.yml"))

    @classmethod
    def data_ingestion_config(cls) -> DataIngestionConfig:
        data_ingestion = cls.config["data_ingestion"]
        config = DataIngestionConfig(
            source_url=data_ingestion["source_url"],
            download_path=data_ingestion["download_path"],
        )
        return config

    @classmethod
    def data_cleaning_config(cls) -> DataCleaningConfig:
        data_transform = cls.config["data_cleaning"]
        config = DataCleaningConfig(
            input_path=data_transform["input_path"],
            x_output_path=data_transform["x_output_path"],
            y_output_path=data_transform["y_output_path"],
            columns_to_drop=data_transform["columns_to_drop"],
            dtype_convertion=data_transform["dtype_convertion"],
            missing_values=data_transform["missing_values"],
            outlier_columns=data_transform["outlier_columns"],
            target_variable=cls.schema["target_variable"],
        )
        return config

    @classmethod
    def data_validation_config(cls) -> DataValidationConfig:
        data_validation = cls.config["data_validation"]
        config = DataValidationConfig(
            input_path=data_validation["input_path"],
            dtypes=data_validation["dtypes"],
            shape=data_validation["shape"],
        )
        return config

    @classmethod
    def data_preprocessing_config(cls) -> DataPreprocessingConfig:
        data_preprocessing = cls.config["data_preprocessing"]
        config = DataPreprocessingConfig(
            x_input_path=data_preprocessing["x_input_path"],
            y_input_path=data_preprocessing["y_input_path"],
            encodings=data_preprocessing["encodings"],
            numerical_features=cls.schema["numerical_columns"],
            x_output_path=data_preprocessing["x_output_path"],
            pipeline_path=data_preprocessing["pipeline_path"],
        )
        return config
