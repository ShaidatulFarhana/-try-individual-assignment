import pandas as pd

def get_dataset_overview(df):
    """Prints the schema information of the DataFrame."""
    return df.info()

def get_statistical_summary(df):
    """Returns basic descriptive statistical matrix data."""
    return df.describe()

def compute_average_screen_time(df):
    """Groups by occupation and calculates mean screen time."""
    return df.groupby('occupation')['daily_screen_time_hours'].mean().sort_values()
