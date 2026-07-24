from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from app.features.metrics.etl.extract import extract_dataset
from app.features.metrics.etl.load import load_gold, load_silver
from app.features.metrics.etl.transform import transform_dataset

LOGGER = logging.getLogger(__name__)


def build_metrics(dataframe: pd.DataFrame) -> dict[str, object]:
    by_date = (
        dataframe["date_of_purchase"]
        .dropna()
        .dt.strftime("%Y-%m-%d")
        .value_counts()
        .sort_index()
        .to_dict()
    )
    by_subject = dataframe["ticket_subject"].value_counts().to_dict()
    return {
        "total": int(len(dataframe)),
        "by_status": dataframe["ticket_status"].value_counts().to_dict(),
        "by_priority": dataframe["ticket_priority"].value_counts().to_dict(),
        "by_channel": dataframe["ticket_channel"].value_counts().to_dict(),
        "by_date": by_date,
        "by_subject": by_subject,
    }


def run_pipeline(force_download: bool = False) -> tuple[Path, Path]:
    bronze_dataset_path = extract_dataset(force_download=force_download)
    dataframe = transform_dataset(bronze_dataset_path)

    silver_path = load_silver(dataframe)
    gold_path = load_gold(build_metrics(dataframe))

    LOGGER.info("ETL pipeline completed")

    return silver_path, gold_path


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    run_pipeline()


if __name__ == "__main__":
    main()
