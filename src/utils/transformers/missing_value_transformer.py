import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

from src.config import logger


class HandleMissingValuesTransformer(BaseEstimator, TransformerMixin):

    def __init__(
        self,
        num_stratergy: str = "mean",
        cat_stratergy: str = "most_frequent",
    ) -> None:
        self.num_imputer = SimpleImputer(strategy=num_stratergy)
        self.cat_imputer = SimpleImputer(strategy=cat_stratergy)

    def fit(self, X, y=None) -> "HandleMissingValuesTransformer":
        self.numerical_cols = X.select_dtypes("number").columns
        self.categorical_cols = X.select_dtypes("O").columns
        self.num_imputer.fit(X[self.numerical_cols])
        self.cat_imputer.fit(X[self.categorical_cols])
        return self

    def transform(self, X) -> pd.DataFrame:
        try:
            df = X.copy()
            df[self.numerical_cols] = self.num_imputer.transform(
                df[self.numerical_cols]
            )
            df[self.categorical_cols] = self.cat_imputer.transform(
                df[self.categorical_cols]
            )
            df = df.drop_duplicates()
            logger.info(f"df shape after complete {__class__.__name__} is : {df.shape}")
            return pd.DataFrame(df, columns=X.columns)

        except Exception as e:
            print(f"error occured in {__class__.__name__}, as {e}")
            raise e
