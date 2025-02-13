import pandas as pd
from sklearn.pipeline import Pipeline

from src.utils import create_path
from src.config import logger
from src.entity import DataCleaningConfig
from src.utils.transformers import (
    InitialCleaningTransformer,
    HandleMissingValuesTransformer,
    OutlierTransformer,
)


class DataCleaning:

    def __init__(self, config: DataCleaningConfig) -> None:
        """
        Initialize the DataCleaning class.

        Args:
            config (DataCleaningConfig): configurations for data cleaning stage
        """

        self.config = config
        self.df = pd.read_csv(self.config.input_path)

    def clean(self) -> None:
        """
        initial data cleaning pipeline, and save cleaned data.

        Args:
            None

        Return:
            None
        """
        iqr_columns = self.config.outlier_columns["iqr"]
        log_columns = self.config.outlier_columns["log"]
        dtype_column_map = self.config.dtype_convertion
        columns_to_drop = self.config.columns_to_drop

        cleaner = Pipeline(
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
            ]
        )

        try:

            df = cleaner.fit_transform(self.df)
            logger.info(
                f"Cleaned Df Stats\nCleaned x shape: {df.shape}\nMissing Values: {df.isna().sum()}\nDuplicates: {df[df.duplicated()].count()}"
            )
            create_path(self.config.df_output_path)
            df.to_csv(self.config.df_output_path, index=False)
        except Exception as e:
            logger.error(
                f"Error occured in {__class__.__name__} while preprocessing pipeline :",
                e,
            )
            raise e
