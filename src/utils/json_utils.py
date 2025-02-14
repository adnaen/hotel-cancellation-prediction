from typing import Any
import json
from pathlib import Path


def dump_json(path: str | Path, data: Any, *args, **kwargs) -> bool:
    try:
        with open(path, "w") as file:
            json.dump(data, file, *args, **kwargs)
        return True
    except Exception as e:
        print(e)
        return False


def load_json(path: str | Path, *args, **kwargs) -> dict:
    try:
        with open(path, "r") as file:
            content = json.load(file, *args, **kwargs)
            return content
    except FileNotFoundError:
        print(f"Not File Found on {path}")
        return {}

    except Exception as e:
        print(e)
        return {}
