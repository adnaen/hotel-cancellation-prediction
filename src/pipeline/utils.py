from datetime import datetime
from src.utils.json_utils import dump_json, load_json


def is_exist_stage(stage: str) -> bool:
    FILE_PATH: str = "artifacts/pipelines_status.json"

    pipelines_status = load_json(path=FILE_PATH)

    if not pipelines_status.get(stage, {}).get("is_complete", False):
        pipelines_status = update_status(status=pipelines_status, stage=stage)
        dump_json(path=FILE_PATH, data=pipelines_status)
        return False
    else:
        return True


def update_status(status: dict, stage: str, is_complete: bool = True):
    status[stage] = {
        "is_complete": is_complete,
        "last_run": datetime.now().isoformat(),
    }
    return status
