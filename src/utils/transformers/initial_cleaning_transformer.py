import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from src.config import logger


class InitialCleaningTransformer(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        columns_map: dict[str, str],
        columns_to_drop: list[str],
    ) -> None:
        self.columns_map = columns_map
        self.columns_to_drop = columns_to_drop

    def fit(self, X, y=None) -> "InitialCleaningTransformer":
        return self

    def transform(self, X) -> pd.DataFrame:
        try:
            df = X.copy()
            logger.info(f"df shape in {__class__.__name__} is : {df.shape}")
            df = df.drop(columns=self.columns_to_drop)
            df = self.__convert_dtypes(df)
            df = df.drop_duplicates()
            logger.info(f"df shape after complte {__class__.__name__} is : {df.shape}")
            print(df.head(1))
            return df
        except Exception as e:
            logger.error(f"error occured in {__class__.__name__}, as {e}")
            raise e

    def __convert_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        df_cp = df.copy(deep=True)
        logger.info("Data Type convertion")
        for column, _type in self.columns_map.items():
            logger.info(f"column : {column} dtype: {df[column].dtype}")
            df_cp[column] = df_cp[column].astype(_type, errors="ignore")
            logger.info(f"column : {column} coverted to dtype: {_type}")

        return df_cp
