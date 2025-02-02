import yaml
from pathlib import Path
from src.config import logger


def load_yaml(absolute_path: Path) -> dict:
    """
    read yml file and return.

    Args:
        absolute_path (Path) : path of the yml file

    Returns:
        dict : yml file data
    """
    with open(absolute_path, "r") as file:
        content = yaml.safe_load(file)
    logger.info(f"load yaml file from {absolute_path}")
    return content


def get_config(yaml_path: Path, keys: list[str] | None = None) -> dict:
    """
    load and return a specific key's value of yml.

    Args:
        yaml_path (Path) : path of the yml file
        keys (list[str]) : nested keys, to be return

    Returns:
        dict : keys data
    """
    data = load_yaml(yaml_path)
    if keys:
        for key in keys:
            data = data[key]
    return data
