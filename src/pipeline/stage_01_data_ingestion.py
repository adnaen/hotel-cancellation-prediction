from src.config import logger
from src.components import DataIngestion
from src.utils import ConfigControl

STAGE = "Data Ingestion"


class DataIngestionPipeline:
    def __init__(self) -> None:
        """
        Initializing DataIngestionPipeline class.
        """
        self.config = ConfigControl.data_ingestion_config()
        self.pipeline = DataIngestion(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.download_raw_data()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
