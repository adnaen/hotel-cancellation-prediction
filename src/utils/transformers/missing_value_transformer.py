import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer


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
            df_cp = X.copy()
            df_cp[self.numerical_cols] = self.num_imputer.transform(
                df_cp[self.numerical_cols]
            )
            df_cp[self.categorical_cols] = self.cat_imputer.transform(
                df_cp[self.categorical_cols]
            )

            return pd.DataFrame(df_cp, columns=X.columns)

        except Exception as e:
            print(f"error occured in {__class__.__name__}, as {e}")
            raise e
