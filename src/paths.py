from pathlib import Path


class BasePaths:

    PROJECT_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_DIR: Path = PROJECT_DIR / "data"
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    CONFIG_DIR: Path = PROJECT_DIR / "config"

    @classmethod
    def resolve(cls, relative_path: Path | str) -> Path:
        """resolve relative path into absolute path"""
        return cls.PROJECT_DIR / relative_path
