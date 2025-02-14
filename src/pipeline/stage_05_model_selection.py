from src.config import logger
from src.components import ModelSelection
from src.config import ConfigControl

STAGE = "Model Selection"


class ModelSelectionPipeline:
    def __init__(self) -> None:
        """
        Initializing ModelSelectionPipeline class.
        """
        self.config = ConfigControl.model_selection_config()
        self.pipeline = ModelSelection(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.split_data()
        status = self.pipeline.select_model()
        status = self.pipeline.tune_model()
        status = self.pipeline.save_model_info()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    model_selection_pipeline = ModelSelectionPipeline()
    model_selection_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
