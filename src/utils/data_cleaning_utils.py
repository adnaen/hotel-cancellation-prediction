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
    df = df.copy(deep=True)
    for dtype, column in columns.items():
        if isinstance(column, str):
            column = [column]

        for each in column:

            match dtype:
                case "categorical":
                    simple_imputer = SimpleImputer(strategy="most_frequent")
                    df[each] = simple_imputer.fit_transform(df[[each]]).ravel()
                case "numerical":
                    simple_imputer = SimpleImputer(strategy="mean")
                    df[each] = simple_imputer.fit_transform(df[[each]]).ravel()
    return df


def handle_outliers(
    df: pd.DataFrame, columns_maps: dict[str, str | list[str]]
) -> pd.DataFrame:
    try:
        df = df.copy(deep=True)

        for method, columns in columns_maps.items():
            if isinstance(columns, str):
                columns = [columns]

            for column in columns:

                match method:
                    case "iqr":
                        Q1, Q3 = df[column].quantile([0.25, 0.75])
                        IQR = Q3 - Q1
                        lower_limit = Q1 - (IQR * 1.5)
                        upper_limit = Q3 + (IQR * 1.5)

                        df = df[df[column].between(lower_limit, upper_limit)]

                    case "log":
                        min_val = df[column].min()
                        if min_val <= 0:
                            df[column] = np.log1p(df[column])
                        else:
                            df[column] = np.log(df[column])
        return df

    except Exception as e:
        print(f"Error during outlier handling: {e}")
        return df
