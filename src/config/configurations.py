from src.entity import DataIngestionConfig, DataTransformationConfig
from src.utils import get_config
from .paths import BasePaths


class ConfigControl:
    def __init__(self) -> None:
        self.config = get_config(yaml_path=BasePaths.resolve("config/config.yml"))
        self.schema = get_config(yaml_path=BasePaths.resolve("config/schema.yml"))

    def data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion = self.config["data_ingestion"]
        config = DataIngestionConfig(
            source_url=data_ingestion["source_utl"],
            download_path=data_ingestion["download_path"],
        )
        return config

    def data_transform_config(self) -> DataTransformationConfig:
        data_transform = self.config["data_transform"]
        config = DataTransformationConfig(
            input_path=data_transform["input_path"],
            x_output_path=data_transform["x_output_path"],
            y_output_path=data_transform["y_output_path"],
            columns_to_drop=data_transform["columns_to_drop"],
            dtype_convertion=data_transform["dtype_convertion"],
            missing_values=data_transform["missing_values"],
            outlier_columns=data_transform["outlier_columns"],
            encodings=data_transform["encodings"],
            target_variable=self.schema["target_variable"],
            numerical_cols=self.schema["numerical_columns"],
            categorical_cols=self.schema["categorical_columns"],
        )
        return config
