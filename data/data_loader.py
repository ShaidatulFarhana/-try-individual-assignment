import pandas as pd
import os

def load_dataset(file_path):
    """Loads the CSV data file safely into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: Target data file not found at {file_path}")
    return pd.read_csv(file_path)
