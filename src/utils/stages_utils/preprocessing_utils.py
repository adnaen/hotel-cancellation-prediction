from sklearn.preprocessing import LabelEncoder
import pandas as pd


def label_encode_columns(X: pd.DataFrame):
    return X.apply(lambda col: LabelEncoder().fit_transform(col))
