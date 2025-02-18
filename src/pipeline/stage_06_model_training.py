from src.config import logger
from src.components import ModelTraining
from src.config import ConfigControl

STAGE = "Model Training"


class ModelTrainingPipeline:
    def __init__(self) -> None:
        """
        Initializing ModelTrainingPipeline class.
        """
        self.config = ConfigControl.model_training_config()
        self.pipeline = ModelTraining(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.choose_model()
        status = self.pipeline.train_model()
        status = self.pipeline.save_model()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
