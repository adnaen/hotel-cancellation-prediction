import pandas as pd
from src.entity import DataPreprocessingConfig


class DataTransform:

    def __init__(self, config: DataPreprocessingConfig) -> None:
        self.config = config
        self.df = pd.read_csv(
            self.config.input_path, parse_dates=["reservation_status_date"]
        )

    def feature_selection(self) -> bool:
        raise NotImplementedError

    def run(self) -> bool:
        raise NotImplementedError
