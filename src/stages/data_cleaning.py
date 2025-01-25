from src.config import DataCleaningConfig


class DataCleaning:
    def __init__(self, config: DataCleaningConfig) -> None:
        self.config = config

    def clean(self) -> None:
        raise NotImplementedError

    def run(self) -> None:
        raise NotImplementedError
