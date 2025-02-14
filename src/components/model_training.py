import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator

from src.entity import ModelTrainingConfig
from src.utils import dump_joblib, load_joblib


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig) -> None:
        self.config = config
        self.train = pd.read_csv(self.config.train_input_path)
        self.model: BaseEstimator | None = None
        self.pipeline = None

    def fit_model(self) -> None:
        estimators = {
            "DecisionTreeClassifier": DecisionTreeClassifier(),
            "RandomForestClassifier": RandomForestClassifier(),
            "XGBClassifier": XGBClassifier(),
        }

        self.model = estimators[self.config.best_model]
        self.model.set_params(**self.config.best_params)

    def train_model(self) -> None:
        x_train = self.train.drop(columns=["is_canceled"])
        y_train = self.train["is_canceled"]

        self.model.fit(x_train, y_train)

        preprocessor = load_joblib(self.config.preprocessor_path)

        self.pipeline = Pipeline(
            steps=[("preprocessor", preprocessor), ("model", self.model)]
        )

    def save_model(self) -> None:
        dump_joblib(path=self.config.pipeline_path, data=self.pipeline)
