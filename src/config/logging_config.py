import logging
import sys

from .paths import BasePaths


file_path = BasePaths.PROJECT_DIR / "logs/app.log"
file_path.parent.mkdir(exist_ok=True, parents=True)
file_path.touch(exist_ok=True)


format = (
    "%(asctime)s %(levelname)s from: %(filename)s at_line: %(lineno)d : %(message)s"
)

logging.basicConfig(
    format=format,
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(filename=file_path, mode="w"),
        logging.StreamHandler(sys.stdout),
    ],
)


logger = logging.getLogger("HotelCancellation")
