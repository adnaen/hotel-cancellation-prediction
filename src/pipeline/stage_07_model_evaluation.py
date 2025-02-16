from src.config import logger
from src.components import ModelEvaluation
from src.config import ConfigControl

STAGE = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        """
        Initializing ModelEvaluationPipeline class.
        """
        self.config = ConfigControl.model_evaluation_config()
        self.pipeline = ModelEvaluation(config=self.config)

    def run(self) -> bool:
        status = self.pipeline.evaluation_metrics()
        status = self.pipeline.save_metrics()
        return True if status else False


if __name__ == "__main__":
    logger.info(f">>> STAGE {STAGE} STARGED <<<<")
    model_Evaluation_pipeline = ModelEvaluationPipeline()
    model_Evaluation_pipeline.run()
    logger.info(f">>> STAGE {STAGE} END <<<<")
