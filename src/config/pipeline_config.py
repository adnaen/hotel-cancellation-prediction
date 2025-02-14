from src.entity import (
    DataIngestionConfig,
    DataCleaningConfig,
    DataValidationConfig,
    DataPreprocessingConfig,
    ModelSelectionConfig,
    ModelTrainingConfig,
)
from src.utils import get_config, load_json
from src.config import BasePaths


class ConfigControl:
    config = get_config(yaml_path=BasePaths.resolve("config/stages.yml"))
    schema = get_config(yaml_path=BasePaths.resolve("config/schema.yml"))
    params = get_config(yaml_path=BasePaths.resolve("config/params.yml"))

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
            df_output_path=data_transform["df_output_path"],
            columns_to_drop=data_transform["columns_to_drop"],
            dtype_convertion=data_transform["dtype_convertion"],
            missing_values=data_transform["missing_values"],
            outlier_columns=data_transform["outlier_columns"],
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
            df_input_path=data_preprocessing["df_input_path"],
            encodings=data_preprocessing["encodings"],
            numerical_features=cls.schema["numerical_columns"],
            train_output_path=data_preprocessing["train_output_path"],
            test_output_path=data_preprocessing["test_output_path"],
            pipeline_path=data_preprocessing["pipeline_path"],
        )
        return config

    @classmethod
    def model_selection_config(cls) -> ModelSelectionConfig:
        model_selection = cls.config["model_selection"]
        config = ModelSelectionConfig(
            train_input_path=model_selection["train_input_path"],
            params=cls.params,
            best_model_info_path=model_selection["best_model_info_path"],
        )
        return config

    @classmethod
    def model_training_config(cls) -> ModelTrainingConfig:
        model_training = cls.config["model_training"]
        best_model_info = load_json(model_training["best_model_info_path"])

        config = ModelTrainingConfig(
            train_input_path=model_training["train_input_path"],
            preprocessor_path=model_training["preprocessor_path"],
            best_model=str(best_model_info.get("best_model")),
            best_params=best_model_info.get("best_params", {}),
            pipeline_path=model_training["pipeline_path"],
        )
        return config
