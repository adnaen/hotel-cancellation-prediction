from src.components import (
    DataIngestion,
    DataTransform,
)
from src.config import ConfigControl

config_control = ConfigControl()

data_ing = DataIngestion(config=config_control.data_ingestion_config())

data_prepro = DataTransform(config=config_control.data_transform_config())
