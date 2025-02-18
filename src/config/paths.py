from pathlib import Path


class BasePaths:
    """
    Project Paths
    """

    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_DIR: Path = PROJECT_DIR / "data"
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    CONFIG_DIR: Path = PROJECT_DIR / "config"
    MODEL_DIR: Path = PROJECT_DIR / "model"

    @classmethod
    def resolve(cls, relative_path: Path | str) -> Path:
        """

        Args:
            relative_path (Path | str) : path

        Returns:
            Path: absolute path
        """
        return cls.PROJECT_DIR / relative_path
