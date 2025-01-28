import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


def convert_dtype(df: pd.DataFrame, columns: dict[str, str]) -> pd.DataFrame:
    """convert column dtype into the given type

    Args:
        df (DataFrame) : dataframe object
        columns (dict[str, str]) : column and its dtype to convert
    """

    for column, dtype in columns.items():
        match dtype:
            case "int":
                df[column] = pd.to_numeric(df[column], errors="coerce")

            case "float":
                df[column] = df[column].astype(np.float64)

            case "object":
                df[column] = df[column].astype("O")

            case "datetime":
                df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def handle_missing_values(
    df: pd.DataFrame, columns: dict[str, list[str] | str]
) -> pd.DataFrame:
    # FIXME: fix this shit
    for dtype, column in columns.items():

        if isinstance(column, str):
            column = [column]

            for each in column:

                match dtype:
                    case "categorical":
                        simple_imputer = SimpleImputer(strategy="most_frequent")
                    case "numerical":
                        simple_imputer = SimpleImputer(strategy="mean")
                df[each] = simple_imputer.fit_transform(df[[each]])
    return df
