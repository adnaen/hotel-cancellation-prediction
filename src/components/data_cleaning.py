from src.utils import load_csv, convert_dtype, handle_missing_values
from src.entity import DataCleaningConfig


class DataCleaning:
    def __init__(self, config: DataCleaningConfig) -> None:
        self.config = config
        self.df = load_csv(self.config.input_path)

    def drop_columns(self) -> bool:
        self.df = self.df.drop(columns=self.config.columns_to_drop)
        return True

    def dtype_conversion(self) -> None:
        self.df = convert_dtype(df=self.df, columns=self.config.dtype_convertion)

    def handle_missing_values(self) -> None:
        self.df = handle_missing_values(df=self.df, columns=self.config.missing_values)

    def treat_outliers(self) -> None:
        # TODO:
        raise NotImplementedError

    def run(self) -> bool:
        drop_columns_status = self.drop_columns()
        dtype_convertion_status = self.dtype_conversion()
        handle_missing_value_status = self.handle_missing_values()
        if all(
            (drop_columns_status, dtype_convertion_status, handle_missing_value_status)
        ):
            return True
        else:
            return False
