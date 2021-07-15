"""Contains a Linear Regression."""

from dynaconf import settings
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from src.libs.features import add_day_of_week, add_lag_feature


class Model:
    """
    Linear regression model class.

    Attributes:
        model (Any): A trained model.
    """

    def __init__(self):
        """Inits Model."""
        self.model = None

    def train(self, df: pd.DataFrame):
        """Trains Model.

        Args:
            df (pd.DataFrame): The input DataFrame.
        """
        df = (
            df.pipe(add_day_of_week, date_col="date")
            .pipe(add_lag_feature, col="y", nb_lags=2)
            .dropna()
        )

        X = df[settings["linear_reg"]["X_cols"]]
        y = df[settings["linear_reg"]["y_col"]]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=settings["linear_reg"]["test_size"], random_state=42
        )

        reg = LinearRegression(**settings["linear_reg"]["hparams"]).fit(X_train, y_train)
        y_pred = reg.predict(X_test)

        print("Coefficients: \n", reg.coef_)
        print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

        self.model = reg
        return self

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """Predicts.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The output DataFrame.
        """
        df = (
            df.pipe(add_day_of_week, date_col="date")
            .pipe(add_lag_feature, col="y", nb_lags=2)
            .dropna()
        )
        X = df[settings["linear_reg"]["X_cols"]]
        y_pred = self.model.predict(X)
        return pd.DataFrame(y_pred, columns=["y_pred"])
