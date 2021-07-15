"""Runs the model.predict for any model."""
from argparse import ArgumentParser
import os

import pandas as pd

from src.io.files import load_model, save_preds

s = "linear_reg-ee81fbf8-7e71-46fe-ab4d-e6eaf486913c.pkl"


def main(model_path: str, data_path: str):
    """Runs the trainer.

    Args:
        model_path (str): The path to the model (e.g. "src.models.linear_reg")
        data_path (str): The path to the data (e.g. "assets/datasets/test.csv").
    """
    model_class = load_model(model_path)
    df = pd.read_csv(data_path, parse_dates=["date"])
    y_pred = model_class.predict(df)
    model_id = os.path.splitext(model_path.split(os.sep)[-1])[0]
    save_preds(y_pred, model_id=model_id)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--model-path", default="assets/models/linear_reg-b08769f8-7397-44a2-bac1-974222fecd80.pkl"
    )
    parser.add_argument("--data-path", default="assets/datasets/test.csv")
    args = parser.parse_args()

    main(model_path=args.model_path, data_path=args.data_path)
