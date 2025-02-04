from typing import Literal
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import logger


class OutlierTransformer(BaseEstimator, TransformerMixin):
    def __init__(
        self, columns: list[str] | str, stratergy: Literal["iqr", "log"] = "iqr"
    ) -> None:
        self.columns = columns
        self.stratergy = stratergy

    def fit(self, X, Y=None) -> "OutlierTransformer":
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        try:
            df = X.copy()
            match self.stratergy:
                case "iqr":
                    result_df = self.__iqr_method(X=df)
                    return result_df

                case "log":
                    result_df = self.__log_method(X=df)
                    return result_df
                case _:
                    return df
        except Exception as e:
            print(f"error occured in {__class__.__name__}, as {e}")
            raise e

    def __log_method(self, X: pd.DataFrame) -> pd.DataFrame:
        try:
            df = X.copy()
            if isinstance(self.columns, str):
                self.columns = [self.columns]

            for column in self.columns:
                min_val = df[column].min()
                if min_val <= 0:
                    shift_value = abs(min_val) + 1
                    df[column] = np.log(df[column] + shift_value)
                else:
                    df[column] = np.log(df[column])

            logger.info(
                f"df shape after complete log method outlier treat {__class__.__name__} is : {df.shape}"
            )
            return df
        except Exception as e:
            logger.error(f"error occured in {__class__.__name__}, as {e}")
            raise e

    def __iqr_method(self, X: pd.DataFrame, threshold: float = 1.5) -> pd.DataFrame:
        try:
            df = X.copy()
            if isinstance(self.columns, str):
                self.columns = [self.columns]

            for column in self.columns:
                Q1, Q3 = df[column].quantile([0.25, 0.75])
                IQR = Q3 - Q1
                lower_limit = Q1 - (IQR * threshold)
                upper_limit = Q3 + (IQR * threshold)
                df = df[df[column].between(lower_limit, upper_limit)]

            logger.info(
                f"df shape after complete iqr method outlier treat {__class__.__name__} is : {df.shape}"
            )
            return pd.DataFrame(df)
        except Exception as e:
            logger.error(f"error occured in {__class__.__name__}, as {e}")
            raise e
