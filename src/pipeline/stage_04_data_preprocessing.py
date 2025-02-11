from src.config import logger
from src.components import DataPreprocessing
from src.utils import ConfigControl

STAGE = "Data Preprocessing"


class DataPreprocessingPipeline:
    def __init__(self) -> None:
        """
        Initializing DataPreprocessingPipeline class.
        """
        self.config = ConfigControl.data_preprocessing_config()
        self.pipeline = DataPreprocessing(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.preprocessing()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    data_validation_pipeline = DataPreprocessingPipeline()
    data_validation_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
