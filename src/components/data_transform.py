import pandas as pd
from pandas.core.common import random_state
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from src.entity import DataTransformationConfig
from src.utils.transformers import (
    InitialCleaningTransformer,
    HandleMissingValuesTransformer,
    OutlierTransformer,
    FeatureEngineeringTransformer,
)
from src.utils import create_path
from src.config import logger


class DataTransform:

    def __init__(self, config: DataTransformationConfig) -> None:
        """
        Initialize the DataTransform class.

        Args:
            config (DataPreprocessingConfig): configurations for data preprocessing stage
        """

        self.config = config
        self.df = pd.read_csv(
            self.config.input_path, parse_dates=["reservation_status_date"]
        )

    def transform(self) -> None:
        """
        create preprocessing pipeline
        """
        iqr_columns = self.config.outlier_columns["iqr"]
        log_columns = self.config.outlier_columns["log"]
        dtype_column_map = self.config.dtype_convertion
        columns_to_drop = self.config.columns_to_drop

        preprocessing_pipeline = Pipeline(
            steps=[
                (
                    "InitialCleaning",
                    InitialCleaningTransformer(
                        columns_map=dtype_column_map, columns_to_drop=columns_to_drop
                    ),
                ),
                ("HandleMissingValues", HandleMissingValuesTransformer()),
                ("IQROutlierTreatment", OutlierTransformer(columns=iqr_columns)),
                (
                    "LOGOutlierTreatment",
                    OutlierTransformer(columns=log_columns, stratergy="log"),
                ),
                (
                    "FeatureEngineering",
                    FeatureEngineeringTransformer(),
                ),
            ]
        )

        try:

            preprocessed_data = preprocessing_pipeline.fit_transform(self.df)
            new_x = pd.DataFrame(preprocessed_data)
            print(new_x.columns)
            create_path(self.config.x_train_output_path)
            x = new_x.drop(columns=self.config.target_variable)
            y = new_x[self.config.target_variable].astype("int")

            # store train test splitted data
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, test_size=0.2, random_state=2313
            )
            x_train.to_csv(self.config.x_train_output_path, index=False)
            x_test.to_csv(self.config.x_test_output_path, index=False)

            y_train.to_csv(self.config.y_train_output_path, index=False)
            y_test.to_csv(self.config.y_test_output_path, index=False)

        except Exception as e:
            logger.error(
                f"Error occured in {__class__.__name__} while preprocessing pipeline :",
                e,
            )
            raise e
