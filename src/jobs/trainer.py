"""Runs the model.train for any model"""

from argparse import ArgumentParser
from importlib import import_module
import os

import pandas as pd

from src.io.files import save_model


def main(model_path: str, data_path: str):
    """Runs the trainer.

    Args:
        model_path (str): The path to the model (e.g. "src.models.linear_reg").
        data_path (str): The path to the data (e.g. "assets/datasets/train.csv").
    """
    model_module = import_module(model_path)
    model_class = getattr(model_module, "Model")
    model_name = model_path.split(os.extsep)[-1]

    df = pd.read_csv(data_path, parse_dates=["date"])
    model = model_class()
    model.train(df)
    save_model(model=model, model_name=model_name)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--model-path", default="src.models.linear_reg")
    parser.add_argument("--data-path", default="assets/datasets/train.csv")
    args = parser.parse_args()

    main(model_path=args.model_path, data_path=args.data_path)
