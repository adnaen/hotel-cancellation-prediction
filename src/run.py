from typing import Any
from src.pipeline import DataIngestionPipeline, DataTransformPipeline


def run_pipeline(pipeline: Any) -> None:
    """
    run pipeline

    Args:
        pipeline (Any) : Instance of Pipeline.

    Returns:
        None
    """
    pipeline.run()


if __name__ == "__main__":
    run_pipeline(DataIngestionPipeline())
    run_pipeline(DataTransformPipeline())
