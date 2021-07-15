"""Contains file io."""

import pickle
from typing import Any
import uuid

import pandas as pd


def save_model(model: Any, model_name: str) -> None:
    """Saves the model locally.

    Args:
        model (Any): The model to save.
        model_name (str): The name of the model
    """
    file_path = f"assets/models/{model_name}-{uuid.uuid4()}.pkl"
    with open(file_path, "wb") as file:
        pickle.dump(model, file)


def load_model(path: str) -> Any:
    """Loads the model.

    Args:
        path (src): The path to the model.

    Returns:
        Any: The model object.
    """
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def save_preds(df: pd.DataFrame, model_id: str) -> None:
    """Saves the predictions.

    Args:
        df (pd.DataFrame): The predictions DataFrame.
        model_id (str): The model id (e.g. "linear_reg-7869645b-7a67-432d-8916-1e0351fafd29")
    """
    file_path = f"assets/predictions/data-{uuid.uuid4()}-{model_id}.csv"
    df.to_csv(file_path, index=False)
