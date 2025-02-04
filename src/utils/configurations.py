from src.entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
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
    def data_transform_config(cls) -> DataTransformationConfig:
        data_transform = cls.config["data_transform"]
        config = DataTransformationConfig(
            input_path=data_transform["input_path"],
            x_output_path=data_transform["x_output_path"],
            y_output_path=data_transform["y_output_path"],
            columns_to_drop=data_transform["columns_to_drop"],
            dtype_convertion=data_transform["dtype_convertion"],
            missing_values=data_transform["missing_values"],
            outlier_columns=data_transform["outlier_columns"],
            encodings=data_transform["encodings"],
            target_variable=cls.schema["target_variable"],
            numerical_cols=cls.schema["numerical_columns"],
            categorical_cols=cls.schema["categorical_columns"],
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
