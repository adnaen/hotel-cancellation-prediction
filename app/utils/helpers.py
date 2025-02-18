from typing import Any
import pandas as pd
from src.utils.json_utils import load_json
from src.utils.joblib_utils import load_joblib
from src.config import BasePaths


async def get_metrics() -> dict:
    FILE_PATH = "artifacts/model_evaluation/metrics.json"
    metrics = load_json(path=FILE_PATH)
    return metrics


async def get_about_model() -> dict:
    FILE_PATH = "artifacts/model_selection/best_model.json"
    model_info = load_json(path=FILE_PATH)
    return model_info


def get_prediction(df: pd.DataFrame) -> list[int]:
    MODEL_PATH = BasePaths.MODEL_DIR / "trained/pipeline.joblib"
    pipeline = load_joblib(path=MODEL_PATH)
    y_pred = pipeline.predict(df)
    print("y predict is : ", y_pred)
    return y_pred
