import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    file_path = 'data/sleep_mobile_stress_dataset_15000.csv'

    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        sns.set_theme(style="whitegrid")

        # --- THIS IS THE LIST/INFO YOU ARE LOOKING FOR ---
        print("\n" + "="*30)
        print("1. DATASET OVERVIEW")
        print("="*30)
        print(df.info())

        print("\n" + "="*30)
        print("2. STATISTICAL SUMMARY")
        print("="*30)
        print(df.describe())

        # Create a 2x2 grid for the 4 plot types
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Sleep and Stress Data Analysis: 4 Key Visualizations', fontsize=20, fontweight='bold')

        # 1. Histogram
        sns.histplot(df['sleep_quality_score'], bins=20, kde=True, ax=axes[0, 0], color='skyblue')
        axes[0, 0].set_title('1. Histogram: Sleep Quality Distribution')

        # 2. Bar Chart (Fixed warning by adding hue)
        avg_screen_time = df.groupby('occupation')['daily_screen_time_hours'].mean().sort_values()
        sns.barplot(x=avg_screen_time.values, y=avg_screen_time.index, ax=axes[0, 1],
                    hue=avg_screen_time.index, palette='magma', legend=False)
        axes[0, 1].set_title('2. Bar Chart: Screen Time by Occupation')

        # 3. Box Plot (Fixed warning by adding hue)
        sns.boxplot(data=df, x='gender', y='stress_level', ax=axes[1, 0],
                    hue='gender', palette='Set2', legend=False)
        axes[1, 0].set_title('3. Box Plot: Stress Level by Gender')

        # 4. Line Plot
        sns.lineplot(data=df, x='caffeine_intake_cups', y='mental_fatigue_score', ax=axes[1, 1], color='brown', marker='o')
        axes[1, 1].set_title('4. Line Plot: Fatigue vs. Caffeine')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])

        print("\n[Action Required] Close the graph window to see the final output in the console.")
        plt.savefig('my_data_plots.png', bbox_inches='tight')
        print("\n[Success] Graph saved as 'my_data_plots.png' in your project folder!")

    except FileNotFoundError:
        print(f"Error: Could not find {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
