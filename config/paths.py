from pathlib import Path


class BasePaths:

    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_DIR: Path = PROJECT_DIR / "data"
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    CONFIG_DIR: Path = PROJECT_DIR / "config"

    @classmethod
    def get(cls, key: str) -> str:
        return getattr(cls, key)


if __name__ == "__main__":
    result = BasePaths.get("RAWDATA_PATH")
    print(result)
