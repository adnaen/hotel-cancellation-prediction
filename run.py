from src import DataIngestionConfig
from src.paths import BasePaths
from src.stages import DataIngestion
from src.utils import load_yaml


configs = load_yaml(BasePaths.resolve("config/config.yml"))

data_ingestion_config = configs["pipeline"]["stages"]["data_ingestion"]

ingestion_config = DataIngestionConfig(
    gdrive_url=data_ingestion_config["gdrive_url"],
    output_path=data_ingestion_config["output_path"],
)

data_ing = DataIngestion(config=ingestion_config)
data_ing.run()
