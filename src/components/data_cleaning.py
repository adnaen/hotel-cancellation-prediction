from src.entity import DataCleaningConfig
from src.utils import load_csv, save_csv
from src.utils.stages_utils import convert_dtype, handle_missing_values, handle_outliers
from src.config import logger


class DataCleaning:
    def __init__(self, config: DataCleaningConfig) -> None:
        self.config = config
        self.df = load_csv(self.config.input_path)
        logger.info("DATA CLEANING STARTED")

    def drop_columns(self) -> bool:
        try:
            df_copy = self.df.copy(deep=True)
            df_copy = df_copy.drop(columns=self.config.columns_to_drop)
            self.df = df_copy
            logger.info("droped unqanted column")
            return True
        except Exception:
            return False

    def dtype_conversion(self) -> bool:
        try:
            df_copy = self.df.copy(deep=True)
            df_copy = convert_dtype(df=df_copy, columns=self.config.dtype_convertion)
            self.df = df_copy
            logger.info("convert dtypes")
            return True
        except Exception:
            return False

    def handle_missing_values(self) -> bool:
        try:
            df_copy = self.df.copy(deep=True)
            df_copy = handle_missing_values(
                df=df_copy, columns=self.config.missing_values
            )
            df_copy = df_copy[~df_copy.duplicated()]
            self.df = df_copy
            logger.info("missing values handled")
            return True
        except Exception:
            return False

    def treat_outliers(self) -> bool:
        try:
            df_copy = self.df.copy(deep=True)
            df_copy = handle_outliers(
                df=df_copy, columns_maps=self.config.outlier_columns
            )
            self.df = df_copy
            logger.info("outlier treatment complete")
            return True
        except Exception:
            return False

    def run(self) -> bool:
        step1 = self.drop_columns()
        step2 = self.dtype_conversion()
        step3 = self.handle_missing_values()
        step4 = self.treat_outliers()
        if all((step1, step2, step3, step4)):
            save_csv(df=self.df, path=self.config.output_path)
            return True
        else:
            return False
