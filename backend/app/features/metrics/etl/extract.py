from pathlib import Path

import pandas as pd


def extract_csv_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)


def extract_json_data(file_path: Path) -> pd.DataFrame:
    return pd.read_json(file_path)
