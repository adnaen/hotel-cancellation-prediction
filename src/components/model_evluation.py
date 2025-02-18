import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, recall_score, confusion_matrix

from src.entity import ModelEvaluationConfig
from src.utils.joblib_utils import load_joblib
from src.utils.common import create_path
from src.utils.json_utils import dump_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        """
        Initializing ModelEvaluation class.
        """
        self.config = config
        self.pipeline = load_joblib(self.config.pipeline_path)
        self.test_df = pd.read_csv(self.config.test_data_path)
        self.metrics = {}

    def evaluation_metrics(self) -> None:
        """
        Calculate classification metrics such as, accuracy, f1, recall and confusion metrics

        Args:
            None

        Returns:
            None
        """
        x_test = self.test_df.drop(columns=["is_canceled"])
        y_test = self.test_df["is_canceled"]

        y_pred = self.pipeline.predict(x_test)

        tn, fp, fn, tp = confusion_matrix(y_true=y_test, y_pred=y_pred).ravel()
        self.metrics = {
            "accuracy_score": accuracy_score(y_true=y_test, y_pred=y_pred),
            "f1_score": f1_score(y_true=y_test, y_pred=y_pred),
            "recall_score": recall_score(y_true=y_test, y_pred=y_pred),
            "confusion_metrics": {
                "TN": int(tn),
                "FP": int(fp),
                "FN": int(fn),
                "TP": int(tp),
            },
        }

    def save_metrics(self) -> None:
        """
        Save the calculated metrics into json.

        Args:
            None

        Returns:
            None
        """
        create_path(self.config.output_path)
        dump_json(path=self.config.output_path, data=self.metrics, indent=1)
