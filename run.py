from src.config import DataIngestionConfig
from src.config import BasePaths
from src.stages import DataIngestion
from src.utils import load_yaml


print(f"PROJECT_PATH : {BasePaths.PROJECT_DIR}")
configs = load_yaml(BasePaths.resolve("config/config.yml"))

data_ingestion_config = configs["pipeline"]["stages"]["data_ingestion"]

ingestion_config = DataIngestionConfig(
    gdrive_url=data_ingestion_config["gdrive_url"],
    output_path=data_ingestion_config["output_path"],
)

data_ing = DataIngestion(config=ingestion_config)
data_ing.run()
