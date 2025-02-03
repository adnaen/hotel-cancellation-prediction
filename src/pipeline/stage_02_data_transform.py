from src.config import logger
from src.components import DataTransform
from src.utils import ConfigControl

STAGE = "DataTransform"


class DataTransformPipeline:
    def __init__(self) -> None:
        """
        Initializing DataIngestionPipeline class.
        """
        self.config = ConfigControl.data_transform_config()
        self.pipeline = DataTransform(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.transform()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    data_transform_pipeline = DataTransformPipeline()
    data_transform_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
