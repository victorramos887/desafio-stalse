
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

LOGGER = logging.getLogger(__name__)

METRICS_DIR = Path(__file__).resolve().parents[1]
GOLD_FILE = METRICS_DIR / "data" / "gold" / "metrics.json"


class ServiceMetrics:
    @staticmethod
    def get_metrics() -> dict[str, Any]:
        if not GOLD_FILE.exists():
            LOGGER.warning(
                "Gold metrics file not found at %s - running pipeline",
                GOLD_FILE,
            )
            from app.features.metrics.etl.pipeline import run_pipeline

            run_pipeline()

        if not GOLD_FILE.exists():
            raise FileNotFoundError(
                f"Metrics file was not generated at {GOLD_FILE}"
            )

        return json.loads(GOLD_FILE.read_text(encoding="utf-8"))
