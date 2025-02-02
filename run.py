from src.config import BasePaths
from src.entity import (
    DataIngestionConfig,
    DataTransformationConfig,
)
from src.components import (
    DataIngestion,
    DataTransform,
)
from src.utils import get_config


config_path = BasePaths.resolve("config/stages.yml")
schema_path = BasePaths.resolve("config/schema.yml")
data_shcema = get_config(yaml_path=schema_path)
data_ingestion_config = get_config(yaml_path=config_path, keys=["data_ingestion"])

data_transform_config = get_config(yaml_path=config_path, keys=["data_transform"])

# data_validation_config = get_config(yaml_path=config_path, keys=["data_validation"])


ingestion_config = DataIngestionConfig(
    source_url=data_ingestion_config["source_url"],
    download_path=BasePaths.resolve(data_ingestion_config["download_path"]),
)


transform_config = DataTransformationConfig(
    input_path=BasePaths.resolve(data_transform_config["input_path"]),
    x_output_path=BasePaths.resolve(data_transform_config["x_output_path"]),
    y_output_path=BasePaths.resolve(data_transform_config["y_output_path"]),
    columns_to_drop=data_transform_config["columns_to_drop"],
    dtype_convertion=data_transform_config["dtype_convertion"],
    missing_values=data_transform_config["missing_values"],
    outlier_columns=data_transform_config["outlier_columns"],
    encodings=data_transform_config["encodings"],
    target_variable=data_shcema["target_variable"],
    numerical_cols=data_shcema["numerical_columns"],
    categorical_cols=data_shcema["categorical_columns"],
)

# validation_config = DataValidationConfig(
#     input_path=BasePaths.resolve(data_validation_config["input_path"]),
#     no_of_columns=data_validation_config["no_of_columns"],
#     dtype_counts=data_validation_config["dtype_counts"],
# )

data_ing = DataIngestion(config=ingestion_config)
data_ing.run()
#
# data_valid = DataValidation(config=validation_config)
# data_valid.run()

data_prepro = DataTransform(config=transform_config)
data_prepro.run()
