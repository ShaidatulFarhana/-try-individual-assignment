import config
from data.data_loader import load_dataset
from preprocessing.preprocessing import (
    get_dataset_overview, 
    get_statistical_summary, 
    compute_average_screen_time
)
from utils.visualization import generate_and_save_plots

def main():
    try:
        # 1. Load Data
        df = load_dataset(config.DATA_PATH)

        # 2. Process Data & Log Summaries
        print("\n" + "="*30)
        print("1. DATASET OVERVIEW")
        print("="*30)
        get_dataset_overview(df)

        print("\n" + "="*30)
        print("2. STATISTICAL SUMMARY")
        print("="*30)
        print(get_statistical_summary(df))

        avg_screen_time = compute_average_screen_time(df)

        # 3. Build & Save Visualizations
        generate_and_save_plots(df, avg_screen_time, config.OUTPUT_IMAGE_PATH)
        print(f"\n[Success] Graph saved as '{config.OUTPUT_IMAGE_PATH}' via clean architecture!")

    except Exception as e:
        print(f"An error occurred during pipeline execution: {e}")

if __name__ == "__main__":
    main()
