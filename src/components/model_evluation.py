import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, recall_score, confusion_matrix

from src.entity import ModelEvaluationConfig
from src.utils import load_joblib, dump_json, create_path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
        self.pipeline = load_joblib(self.config.pipeline_path)
        self.test_df = pd.read_csv(self.config.test_data_path)
        self.metrics = {}

    def evaluation_metrics(self) -> None:
        x_test = self.test_df.drop(columns=["is_canceled"])
        y_test = self.test_df["is_canceled"]

        y_pred = self.pipeline.predict(x_test)

        tn, fp, fn, tp = confusion_matrix(y_true=y_test, y_pred=y_pred).ravel()
        self.metrics = {
            "accuracy_score": accuracy_score(y_true=y_test, y_pred=y_pred),
            "f1_score": f1_score(y_true=y_test, y_pred=y_pred),
            "recall_score": recall_score(y_true=y_test, y_pred=y_pred),
            "confustion_metrics": {
                "TN": int(tn),
                "FP": int(fp),
                "FN": int(fn),
                "TP": int(tp),
            },
        }

    def save_metrics(self) -> None:
        create_path(self.config.output_path)
        dump_json(path=self.config.output_path, data=self.metrics, indent=1)
