import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import TargetEncoder
from category_encoders import OrdinalEncoder, CountEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.entity import ModelTrainingConfig


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig) -> None:
        self.config = config
        self.x_train = pd.read_csv(self.config.x_train_input_path)
        self.y_train = pd.read_csv(self.config.y_train_input_path)

    def preprocessing(self) -> None:
        categorical_pipeline = ColumnTransformer(
            transformers=[
                (
                    "ordinal_encoder",
                    OrdinalEncoder(),
                    self.config.encodings["ordinal_encoder"],
                ),
                (
                    "count_encoder",
                    CountEncoder(),
                    self.config.encodings["count_encoder"],
                ),
                (
                    "target_encoder",
                    TargetEncoder(),
                    self.config.encodings["target_encoder"],
                ),
            ]
        )

        preprocessor = Pipeline(
            steps=[("categorical", categorical_pipeline), ("numerical")]
        )

        new_data = preprocessor.fit_transform(self.x_train, self.y_train)

        return None

    def train(self) -> None:
        raise NotImplementedError
