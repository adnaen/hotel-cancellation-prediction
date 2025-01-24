from pathlib import Path
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    gdrive_url: str
    output_path: Path
