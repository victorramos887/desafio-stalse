import json
import logging
from pathlib import Path
from typing import Any

import pandas as pd

METRICS_DIR = Path(__file__).resolve().parents[1]

SILVER_DIR = METRICS_DIR / "data" / "silver"
GOLD_DIR = METRICS_DIR / "data" / "gold"

SILVER_FILE = SILVER_DIR / "customer_support_tickets.parquet"
GOLD_FILE = GOLD_DIR / "metrics.json"


def load_silver(dataframe: pd.DataFrame) -> Path:
    """Salva os dados tratados na camada Silver."""
    SILVER_DIR.mkdir(parents=True, exist_ok=True)

    dataframe.to_parquet(
        SILVER_FILE,
        index=False,
    )

    logging.info("Silver dataset saved to %s", SILVER_FILE)

    return SILVER_FILE


def load_gold(metrics: dict[str, Any]) -> Path:
    """Salva as métricas agregadas na camada Gold."""
    GOLD_DIR.mkdir(parents=True, exist_ok=True)

    GOLD_FILE.write_text(
        json.dumps(
            metrics,
            ensure_ascii=False,
            indent=2,
            default=str,
        ),
        encoding="utf-8",
    )

    logging.info("Gold metrics saved to %s", GOLD_FILE)

    return GOLD_FILE
