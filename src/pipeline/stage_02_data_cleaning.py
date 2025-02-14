from src.config import logger
from src.components import DataCleaning
from src.config import ConfigControl

STAGE = "DataCleaning"


class DataCleaningPipeline:
    def __init__(self) -> None:
        """
        Initializing DataIngestionPipeline class.
        """
        self.config = ConfigControl.data_cleaning_config()
        self.pipeline = DataCleaning(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.clean()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    data_transform_pipeline = DataCleaningPipeline()
    data_transform_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
