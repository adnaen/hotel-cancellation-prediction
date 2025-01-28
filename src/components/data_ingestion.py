from src.utils import from_gdrive
from src.entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_raw_data(self) -> bool:
        from_gdrive(url=self.config.source_url, filename=self.config.download_path)
        return True

    def run(self) -> bool:
        download_status = self.download_raw_data()
        if download_status:
            return True
        else:
            return False
