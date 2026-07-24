import json
from pathlib import Path
from unittest.mock import patch

from app.features.metrics.service.service import ServiceMetrics


def test_get_metrics_reads_existing_json(tmp_path: Path) -> None:
    metrics_file = tmp_path / "metrics.json"
    expected_metrics = {
        "total": 2,
        "by_status": {"open": 1, "closed": 1},
        "by_priority": {"high": 1, "low": 1},
        "by_channel": {"email": 1, "chat": 1},
    }
    metrics_file.write_text(json.dumps(expected_metrics), encoding="utf-8")

    with patch("app.features.metrics.service.service.GOLD_FILE", metrics_file):
        metrics = ServiceMetrics.get_metrics()

    assert metrics == expected_metrics


def test_get_metrics_runs_pipeline_when_json_missing(tmp_path: Path) -> None:
    metrics_file = tmp_path / "metrics.json"
    expected_metrics = {
        "total": 1,
        "by_status": {"open": 1},
        "by_priority": {"high": 1},
        "by_channel": {"email": 1},
    }

    def _fake_run_pipeline(*_: object, **__: object) -> tuple[Path, Path]:
        metrics_file.write_text(json.dumps(expected_metrics), encoding="utf-8")
        return tmp_path / "silver.parquet", metrics_file

    with (
        patch("app.features.metrics.service.service.GOLD_FILE", metrics_file),
        patch(
            "app.features.metrics.etl.pipeline.run_pipeline",
            side_effect=_fake_run_pipeline,
        ) as mock_run_pipeline,
    ):
        metrics = ServiceMetrics.get_metrics()

    mock_run_pipeline.assert_called_once_with()
    assert metrics == expected_metrics
