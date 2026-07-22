from pathlib import Path

import kagglehub

DATASET_HANDLE = "suraj520/customer-support-ticket-dataset"
DATASET_FILENAME = "customer_support_tickets.csv"

METRICS_DIR = Path(__file__).resolve().parents[1]
BRONZE_DIR = METRICS_DIR / "data" / "bronze"
BRONZE_FILE = BRONZE_DIR / DATASET_FILENAME

def extract_dataset(force_download: bool = False) -> Path:
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)
    if BRONZE_FILE.exists() and not force_download:
        return BRONZE_FILE
    
    download_file = kagglehub.dataset_download(
        DATASET_HANDLE,
        path=DATASET_FILENAME,
        output_dir=BRONZE_DIR,
        force_download=force_download,
    )
    
    dataset_path = Path(download_file)
    
    if not dataset_path.exists():
        raise FileNotFoundError(f"Failed to download the dataset: {DATASET_FILENAME}")
    
    return dataset_path


