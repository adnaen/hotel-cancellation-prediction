from src.utils.common import from_gdrive
from src.entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig) -> None:
        """
        Initialize the DataIngestion class.

        Args:
            config (DataIngestionConfig) : DataIngestion configuration
        """
        self.config = config

    def download_raw_data(self) -> bool:
        """
        download raw dataset from google drive.

        Returns:
            bool: status
        """
        from_gdrive(url=self.config.source_url, filename=self.config.download_path)
        return True
