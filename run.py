from src.config import BasePaths
from src.entity import (
    DataIngestionConfig,
    DataCleaningConfig,
    DataValidationConfig,
    DataPreprocessingConfig,
)
from src.components import (
    DataIngestion,
    DataValidation,
    DataTransform,
)
from src.utils import get_config


config_path = BasePaths.resolve("config/stages.yml")
data_ingestion_config = get_config(
    yaml_path=config_path, keys=["stages", "data_ingestion"]
)

data_cleaning_config = get_config(
    yaml_path=config_path, keys=["stages", "data_cleaning"]
)

data_validation_config = get_config(
    yaml_path=config_path, keys=["stages", "data_validation"]
)

data_preprocessing_config = get_config(
    yaml_path=config_path, keys=["stages", "data_preprocessing"]
)

ingestion_config = DataIngestionConfig(
    source_url=data_ingestion_config["source_url"],
    download_path=BasePaths.resolve(data_ingestion_config["download_path"]),
)


cleaning_config = DataCleaningConfig(
    input_path=BasePaths.resolve(data_cleaning_config["input_path"]),
    output_path=BasePaths.resolve(data_cleaning_config["output_path"]),
    columns_to_drop=data_cleaning_config["columns_to_drop"],
    dtype_convertion=data_cleaning_config["dtype_convertion"],
    missing_values=data_cleaning_config["missing_values"],
    outlier_columns=data_cleaning_config["outlier_columns"],
)

validation_config = DataValidationConfig(
    input_path=BasePaths.resolve(data_validation_config["input_path"]),
    no_of_columns=data_validation_config["no_of_columns"],
    dtype_counts=data_validation_config["dtype_counts"],
)

preprocessing_config = DataPreprocessingConfig(
    input_path=BasePaths.resolve(data_preprocessing_config["input_path"]),
    output_path=BasePaths.resolve(data_preprocessing_config["output_path"]),
    encodings=data_preprocessing_config["encodings"],
)

# data_ing = DataIngestion(config=ingestion_config)
# data_ing.run()
#
# data_clean = DataCleaning(config=cleaning_config)
# data_clean.run()
#
# data_valid = DataValidation(config=validation_config)
# data_valid.run()

data_prepro = DataPreprocessing(config=preprocessing_config)
data_prepro.run()
