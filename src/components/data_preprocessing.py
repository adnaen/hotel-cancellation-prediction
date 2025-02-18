import pandas as pd
from category_encoders import OrdinalEncoder, CountEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from src.entity import DataPreprocessingConfig
from src.config import logger
from src.utils.joblib_utils import dump_joblib
from src.utils.common import create_path


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
        self.df = pd.read_csv(self.config.df_input_path)

    def preprocessing(self) -> bool:
        """
        create pipeline and transform data with it.

        Args:
            None

        Returns:
            None

        """
        preprocessor = ColumnTransformer(
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
                            ("encoder", CountEncoder(handle_unknown=0)),
                            ("scaler", StandardScaler()),
                        ]
                    ),
                    self.config.encodings["count_encoder"],
                ),
                ("scaler", StandardScaler(), self.config.numerical_features),
            ],
            remainder="passthrough",
            verbose_feature_names_out=False,
            force_int_remainder_cols=False,
        )

        try:

            train, test = train_test_split(
                self.df, test_size=0.2, random_state=2323, shuffle=True
            )

            train = pd.DataFrame(train)
            test = pd.DataFrame(test)

            x_train = train.drop(columns=["is_canceled"])
            y_train = train["is_canceled"].astype("int16")

            preprocessor.set_output(transform="pandas")
            preprocessor.fit(x_train)
            processed_train = preprocessor.transform(x_train)
            processed_train["is_canceled"] = y_train.values

            create_path(self.config.train_output_path)

            processed_train.to_csv(self.config.train_output_path, index=False)
            test.to_csv(self.config.test_output_path, index=False)
            dump_joblib(path=self.config.pipeline_path, data=preprocessor)
            return True

        except Exception as e:
            logger.error(
                f"Error occured in {__class__.__name__} while preprocessing pipeline :",
                e,
            )
            raise e
