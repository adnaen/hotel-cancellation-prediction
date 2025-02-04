import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import logger


class FeatureEngineeringTransformer(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        pass

    def fit(self, df: pd.DataFrame, Y=None) -> "FeatureEngineeringTransformer":
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        df = X.copy()
        try:
            logger.info(f"df shape in {__class__.__name__} is : {df.shape}")
            df["reservation_status_year"] = df["reservation_status_date"].dt.year
            df["reservation_status_month"] = df["reservation_status_date"].dt.month
            df["reservation_status_day_of_month"] = df[
                "reservation_status_date"
            ].dt.date
            df["reservation_status_weekday"] = df["reservation_status_date"].dt.weekday
            df["reservation_status_is_weekend"] = (
                df["reservation_status_date"]
                .dt.weekday.apply(lambda x: True if x in [5, 6] else False)
                .astype("int")
            )
            df = df.drop(columns=["reservation_status_date"])
            logger.info(f"df shape after complte {__class__.__name__} is : {df.shape}")
            return df
        except Exception as e:
            print(f"error occured in {__class__.__name__}, as {e}")
            raise e
