from typing import Any
from src.pipeline import (
    DataIngestionPipeline,
    DataCleaningPipeline,
    DataValidationPipeline,
    DataPreprocessingPipeline,
    ModelSelectionPipeline,
)
from src.config import logger


def run_pipeline(pipeline: Any, stage: str) -> None:
    """
    run pipeline

    Args:
        pipeline (Any) : Instance of Pipeline.

    Returns:
        None
    """
    logger.info(
        f"\n{'*' * 100}\n{' ' * 40}STAGE {stage} STARTED{' ' * 40}\n{'*' * 100}"
    )
    pipeline.run()

    logger.info(f"\n{'*' * 100}\n{' ' * 40}STAGE {stage} END{' ' * 40}\n{'*' * 100}")


if __name__ == "__main__":
    run_pipeline(DataIngestionPipeline(), stage="Data Ingestion")
    run_pipeline(DataCleaningPipeline(), stage="Data Cleaning")
    run_pipeline(DataValidationPipeline(), stage="Data Validation")
    run_pipeline(DataPreprocessingPipeline(), stage="Data Preprocessing")
    run_pipeline(ModelSelectionPipeline(), stage="Model Selection")
