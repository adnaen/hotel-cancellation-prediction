from typing import Any
import pandas as pd
import numpy as np
from sklearn.model_selection import (
    cross_val_score,
    StratifiedKFold,
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from src.entity import ModelSelectionConfig
from src.utils import create_path, dump_json


class ModelSelection:
    def __init__(self, config: ModelSelectionConfig) -> None:
        """
        Initializing ModelSelection class.
        """
        self.config = config
        self.train = pd.read_csv(self.config.train_input_path)
        self.best_model: dict | None = None
        self.best_params: dict | None = None

    def split_data(self) -> None:
        self.x_train = self.train.drop(columns=["is_canceled"])
        self.y_train = self.train["is_canceled"].values.ravel()

    def select_model(self) -> None:
        models = {
            "DecisionTreeClassifier": DecisionTreeClassifier(),
            "RandomForestClassifier": RandomForestClassifier(),
            "XGBClassifier": XGBClassifier(),
        }

        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=121)
        model_stats = []
        for model, estimator in models.items():
            accuracy_score = cross_val_score(
                estimator=estimator,
                X=self.x_train,
                y=self.y_train,
                n_jobs=-1,
                scoring="accuracy",
                cv=skf,
            )

            current_model = {"name": model, "accuracy": np.mean(accuracy_score)}

            if self.best_model is None:
                self.best_model = current_model

            if current_model["accuracy"] > self.best_model["accuracy"]:
                self.best_model = current_model

            model_stats.append(current_model)
        print(f"Best model : {self.best_model}")

    def tune_model(self) -> bool:
        model_name = self.best_model.get("name", "")
        match model_name:
            case "DecisionTreeClassifier":
                params = self.config.params[model_name]
                self.best_params = self._hyperparameter_tunning(
                    estimator=DecisionTreeClassifier(), params=params
                )
                print(best_params)
                return True

            case "RandomForestClassifier":
                params = self.config.params[model_name]
                self.best_params = self._hyperparameter_tunning(
                    estimator=RandomForestClassifier(), params=params
                )
                print(best_params)
                return True

            case "XGBClassifier":
                params = self.config.params[model_name]
                self.best_params = self._hyperparameter_tunning(
                    estimator=XGBClassifier(), params=params
                )
                return True
        return False

    def save_model_info(self) -> None:
        best_params = {
            "best_model": self.best_model["name"],
            "best_params": self.best_params,
        }
        best_params["best_params"].update({"n_jobs": -1})

        create_path(self.config.best_model_info_path)
        dump_json(path=self.config.best_model_info_path, data=best_params, indent=1)

    def _hyperparameter_tunning(self, estimator: Any, params: dict) -> dict:
        from sklearn.model_selection import RandomizedSearchCV

        model = RandomizedSearchCV(
            estimator=estimator, param_distributions=params, n_jobs=-1
        )
        model.fit(self.x_train, self.y_train)
        return model.best_params_
