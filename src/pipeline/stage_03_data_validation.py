from src.config import logger
from src.components import DataValidation
from src.config import ConfigControl

STAGE = "Data Validation"


class DataValidationPipeline:
    def __init__(self) -> None:
        """
        Initializing DataValidationPipeline class.
        """
        self.config = ConfigControl.data_validation_config()
        self.pipeline = DataValidation(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.structural_validation()
        status = self.pipeline.integrity_validation()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
