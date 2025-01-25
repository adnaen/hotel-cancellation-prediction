from src.utils import from_gdrive
from src.config import DataIngestionConfig, logger


class DataIngestion:

    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_raw_data(self) -> bool:
        logger.info("DATA INGESTION START")
        try:
            from_gdrive(url=self.config.gdrive_url, filename=self.config.output_path)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def run(self) -> bool:
        download_status = self.download_raw_data()
        if download_status:
            logger.info("DATA INGESTION START")
            return True
        else:
            logger.info("DATA INGESTION FAILED SOMEWHERE")
            return False
