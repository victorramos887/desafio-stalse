from __future__ import annotations

import logging
from pathlib import Path
from typing import Final

import pandas as pd

LOGGER = logging.getLogger(__name__)

DATE_COLUMNS: Final[tuple[str, ...]] = (
    "date_of_purchase",
    "first_response_time",
    "time_to_resolution",
)

LOWERCASE_COLUMNS: Final[tuple[str, ...]] = (
    "customer_gender",
    "ticket_type",
    "ticket_subject",
    "ticket_status",
    "ticket_priority",
    "ticket_channel",
)

REQUIRED_COLUMNS: Final[frozenset[str]] = frozenset(
    {
        "ticket_id",
        "customer_age",
        "customer_gender",
        "product_purchased",
        "date_of_purchase",
        "ticket_type",
        "ticket_subject",
        "ticket_status",
        "ticket_priority",
        "ticket_channel",
        "first_response_time",
        "time_to_resolution",
        "customer_satisfaction_rating",
    }
)

SILVER_COLUMNS: Final[tuple[str, ...]] = (
    "ticket_id",
    "customer_age",
    "customer_gender",
    "product_purchased",
    "date_of_purchase",
    "ticket_type",
    "ticket_subject",
    "ticket_status",
    "ticket_priority",
    "ticket_channel",
    "first_response_time",
    "time_to_resolution",
    "customer_satisfaction_rating",
    "resolution_time_hours",
    "is_resolved",
)


def normalize_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    normalized = dataframe.copy()

    normalized.columns = (
        normalized.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    LOGGER.info("Column names normalized")

    return normalized


def validate_required_columns(dataframe: pd.DataFrame) -> None:
    missing_columns = sorted(REQUIRED_COLUMNS - set(dataframe.columns))

    if missing_columns:
        missing = ", ".join(missing_columns)

        raise ValueError(f"Dataset is missing required columns: {missing}")


def normalize_categories(dataframe: pd.DataFrame) -> pd.DataFrame:
    normalized = dataframe.copy()

    for column in LOWERCASE_COLUMNS:
        normalized[column] = normalized[column].astype("string").str.strip().str.lower()

    normalized["product_purchased"] = (
        normalized["product_purchased"].astype("string").str.strip()
    )

    LOGGER.info("Categorical columns normalized")

    return normalized


def normalize_types(dataframe: pd.DataFrame) -> pd.DataFrame:
    normalized = dataframe.copy()

    normalized["ticket_id"] = pd.to_numeric(
        normalized["ticket_id"],
        errors="coerce",
    ).astype("Int64")

    normalized["customer_age"] = pd.to_numeric(
        normalized["customer_age"],
        errors="coerce",
    ).astype("Int64")

    normalized["customer_satisfaction_rating"] = pd.to_numeric(
        normalized["customer_satisfaction_rating"],
        errors="coerce",
    )

    for column in DATE_COLUMNS:
        normalized[column] = pd.to_datetime(normalized[column], errors="coerce")

    LOGGER.info("Column types normalized")

    return normalized


def validate_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    validated = dataframe.copy()

    validated["customer_age"] = validated["customer_age"].where(
        validated["customer_age"].between(0, 120)
    )

    validated["customer_satisfaction_rating"] = validated[
        "customer_satisfaction_rating"
    ].where(validated["customer_satisfaction_rating"].between(1, 5))

    LOGGER.info("Invalid ages and ratings replaced with null")

    return validated


def create_derived_columns(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    derived = dataframe.copy()

    resolution_time = derived["time_to_resolution"] - derived["first_response_time"]

    resolution_hours = resolution_time.dt.total_seconds().div(3600)
    valid_resolution = resolution_hours.ge(0)

    # Algumas linhas do dataset possuem resolução anterior
    # à primeira resposta. Essas durações são consideradas inválidas.
    derived["resolution_time_hours"] = resolution_hours.where(valid_resolution)

    derived["is_resolved"] = (
        derived["ticket_status"].eq("closed")
        & derived["time_to_resolution"].notna()
        & valid_resolution.fillna(False)
    )

    LOGGER.info("Derived columns created")

    return derived


def remove_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    initial_rows = len(dataframe)

    cleaned = dataframe.drop_duplicates(
        subset=["ticket_id"],
        keep="last",
    )

    removed_rows = initial_rows - len(cleaned)

    LOGGER.info("%s duplicated tickets removed", removed_rows)

    return cleaned


def transform_dataset(
    dataset_path: str | Path,
) -> pd.DataFrame:
    dataframe = pd.read_csv(dataset_path)

    LOGGER.info("Bronze dataset loaded with shape %s", dataframe.shape)

    dataframe = normalize_column_names(dataframe)
    validate_required_columns(dataframe)

    dataframe = normalize_categories(dataframe)
    dataframe = normalize_types(dataframe)
    dataframe = validate_values(dataframe)
    dataframe = remove_duplicates(dataframe)
    dataframe = create_derived_columns(dataframe)

    dataframe = dataframe.loc[:, SILVER_COLUMNS].reset_index(drop=True)

    LOGGER.info("Transformation completed with shape %s", dataframe.shape)

    return dataframe
