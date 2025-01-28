import yaml
from pathlib import Path
from src.config import logger


def load_yaml(absolute_path: Path) -> dict:
    """read .yml file and return its content"""
    with open(absolute_path, "r") as file:
        content = yaml.safe_load(file)
    logger.info(f"load yaml file from {absolute_path}")
    return content


def get_config(yaml_path: Path, keys: list[str]) -> dict:
    """return the configuration data corresponding its keys"""
    data = load_yaml(yaml_path)
    for key in keys:
        data = data[key]
    return data
