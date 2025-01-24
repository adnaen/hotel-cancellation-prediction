from src.utils import from_gdrive
from src import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_raw_data(self) -> bool:
        try:
            from_gdrive(url=self.config.gdrive_url, filename=self.config.output_path)
            return True
        except Exception:
            print("something went wrong")
            return False

    def run(self) -> bool:
        download_status = self.download_raw_data()
        if download_status:
            return True
        else:
            return False
