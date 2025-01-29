from src.config import BasePaths
from src.entity import DataIngestionConfig
from src.components import DataIngestion, DataCleaning
from src.entity.config_entity import DataCleaningConfig
from src.utils import get_config


config_path = BasePaths.resolve("config/stages.yml")
data_ingestion_config = get_config(
    yaml_path=config_path, keys=["stages", "data_ingestion"]
)

data_cleaning_config = get_config(
    yaml_path=config_path, keys=["stages", "data_cleaning"]
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


data_ing = DataIngestion(config=ingestion_config)
stage1 = data_ing.run()
if stage1:
    data_clean = DataCleaning(config=cleaning_config)
    data_clean.run()
