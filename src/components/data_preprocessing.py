import pandas as pd
from category_encoders import OrdinalEncoder, CountEncoder
from sklearn.preprocessing import StandardScaler, TargetEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.entity import DataPreprocessingConfig
from src.config import logger
from src.utils import dump_joblib, create_path


class DataPreprocessing:
    """
    Reusable data preprocessing pipeline.
    """

    def __init__(self, config: DataPreprocessingConfig) -> None:
        """
        Initialize DataPreprocessing class.

        Args:
            config (DataPreprocessingConfig): configurations for data preprocessing stage

        """
        self.config = config
        self.X = pd.read_csv(self.config.x_input_path)
        self.Y = pd.read_csv(self.config.y_input_path)

    def preprocessing(self) -> bool:
        """
        create pipeline and transform data with it.

        Args:
            None

        Returns:
            None

        """
        categorical_transformer = ColumnTransformer(
            transformers=[
                (
                    "ordinal_encoder",
                    Pipeline(
                        steps=[
                            ("encoder", OrdinalEncoder()),
                            ("scaler", StandardScaler()),
                        ]
                    ),
                    self.config.encodings["ordinal_encoder"],
                ),
                (
                    "count_encoder",
                    Pipeline(
                        steps=[
                            ("encoder", CountEncoder()),
                            ("scaler", StandardScaler()),
                        ]
                    ),
                    self.config.encodings["count_encoder"],
                ),
                (
                    "target_encoder",
                    Pipeline(
                        steps=[
                            ("encoder", TargetEncoder()),
                            ("scaler", StandardScaler()),
                        ]
                    ),
                    self.config.encodings["target_encoder"],
                ),
            ],
            remainder="passthrough",
            verbose_feature_names_out=False,
            force_int_remainder_cols=False,
        )

        numerical_transformer = ColumnTransformer(
            transformers=[("scaler", StandardScaler(), self.config.numerical_features)],
            remainder="passthrough",
            verbose_feature_names_out=False,
            force_int_remainder_cols=False,
        )

        preprocessor = Pipeline(
            steps=[
                ("categorical features", categorical_transformer),
                ("numerical features", numerical_transformer),
            ]
        )

        try:
            preprocessor.set_output(transform="pandas")
            preprocessor.fit(self.X, self.Y)
            preprocessed_x = preprocessor.transform(self.X)
            create_path(self.config.x_output_path)
            preprocessed_x.to_csv(self.config.x_output_path, index=False)
            dump_joblib(path=self.config.pipeline_path, data=preprocessor)
            return True

        except Exception as e:
            logger.error(
                f"Error occured in {__class__.__name__} while preprocessing pipeline :",
                e,
            )
            raise e
