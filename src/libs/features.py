"""Contains feature engineering helpers."""
import pandas as pd


def add_lag_feature(df: pd.DataFrame, col: str, nb_lags: int) -> pd.DataFrame:
    """Adds lag features.

     Args:
        df (pd.DataFrame): The input DataFrame.
        col (str): The column to lag.
        nb_lags (str): The number of lags.

    Returns:
        pd.DataFrame: The output DataFrame.
    """
    for n_lag in range(1, nb_lags):
        df.loc[:, f"{col}_lag_{n_lag}"] = df[col].shift(n_lag)
    return df


def add_day_of_week(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Adds day_of_week feature.

    Args:
        df (pd.DataFrame): The input DataFrame.
        date_col (str): The date column.

    Returns:
        pd.DataFrame: The output DataFrame.
    """
    df["day_of_week"] = df[date_col].dt.dayofweek
    return df
