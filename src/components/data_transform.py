import pandas as pd
from sklearn.pipeline import Pipeline

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

        self.X = self.df.drop(columns=list(self.config.target_variable))
        self.Y = self.df[self.config.target_variable]

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

            preprocessed_data = preprocessing_pipeline.fit_transform(self.X)
            new_x = pd.DataFrame(preprocessed_data)
            print(new_x.columns)
            create_path(self.config.x_output_path)
            new_x.to_csv(self.config.x_output_path, index=False)
            self.Y.to_csv(self.config.y_output_path, index=False)

        except Exception as e:
            logger.error(
                f"Error occured in {__class__.__name__} while preprocessing pipeline :",
                e,
            )
            raise e
