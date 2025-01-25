from pathlib import Path
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    gdrive_url: str
    output_path: Path


@dataclass
class DataCleaningConfig:
    input_path: Path
    output_path: Path
    columns_to_drop: tuple[str]
    # TODO:
