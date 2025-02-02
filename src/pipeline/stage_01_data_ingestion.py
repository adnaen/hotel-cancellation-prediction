from src.components import DataIngestion


class DataIngestionPipeline:
    def __init__(self) -> None:
        """
        Initializing DataIngestionPipeline class.
        """

        self.data_ingestion = DataIngestion()
