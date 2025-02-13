import logging
import sys
from datetime import datetime

from .paths import BasePaths


# LOG_NAME = f"{datetime.now():%d_%m_%Y_%M_%H}.log"
LOG_NAME = f"{datetime.now()}.log"
file_path = BasePaths.PROJECT_DIR / f"logs/{LOG_NAME}"
file_path.parent.mkdir(exist_ok=True, parents=True)
file_path.touch(exist_ok=True)


format = "%(asctime)s %(levelname)s %(filename)s %(message)s"

logging.basicConfig(
    format=format,
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(filename=file_path, mode="w"),
        logging.StreamHandler(sys.stdout),
    ],
)


logger = logging.getLogger("HotelCancellation")
