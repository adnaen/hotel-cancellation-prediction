import pandas as pd
from pandas.core.dtypes import api as pd_utils
from src.config import logger


def check_dtypes(df: pd.DataFrame, base_type_counts: dict[str, int]) -> bool:
    ERROR_COUNT = 0
    dtype_counts = get_dtype_count(df)
    print("count of dtype of our dataset", dtype_counts)
    for key1, key2 in zip(dtype_counts, base_type_counts):
        if dtype_counts[key1] != base_type_counts[key2]:
            ERROR_COUNT += 1

    return True if ERROR_COUNT == 0 else False


def get_dtype_count(df: pd.DataFrame) -> dict[str, int]:

    INTEGER_COUNT = 0
    OBJECT_COUNT = 0
    FLOAT_COUNT = 0
    DATETIME_COUNT = 0

    for column in df.columns:

        if pd_utils.is_float_dtype(df[column]):
            FLOAT_COUNT += 1

        elif pd_utils.is_object_dtype(df[column]):
            OBJECT_COUNT += 1

        elif pd_utils.is_integer_dtype(df[column]):
            INTEGER_COUNT += 1

        elif pd_utils.is_datetime64_any_dtype(df[column]):
            DATETIME_COUNT += 1

    return {
        "Integer": INTEGER_COUNT,
        "float": FLOAT_COUNT,
        "object": OBJECT_COUNT,
        "datetime": DATETIME_COUNT,
    }


def is_empty_missing_values(df: pd.DataFrame) -> bool:
    MISSING_VALUES = 0
    for column in df.columns:
        if any(df[column].isna()):
            MISSING_VALUES += 1
    return False if MISSING_VALUES == 0 else True
