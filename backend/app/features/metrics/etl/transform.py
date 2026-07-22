import pandas as pd
from app.features.metrics.etl.extract import extract_dataset

dataset = extract_dataset()

def transform_dataset(dataset_path: str) -> pd.DataFrame:
    df = pd.read_csv(dataset_path)
    
    print("Initial DataFrame shape:", df.shape)
    return df

transform_dataset(dataset)