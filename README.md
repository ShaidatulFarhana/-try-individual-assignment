# -try-individual-assignment
Imported Kaggle Dataset for Individual Assignment

# About the Project
This project aims to migrate from a notebook-based workflow to a modularized Python codebase using `.py` files.

The original code was obtained from the following Kaggle dataset: [Sleep, Screen Time and Stress Analysis](https://www.kaggle.com/datasets/jayjoshi37/sleep-screen-time-and-stress-analysis)

# Downloading the Dataset
The original code is downloaded from [Sleep, Screen Time and Stress Analysis](https://www.kaggle.com/datasets/jayjoshi37/sleep-screen-time-and-stress-analysis) Kaggle page. Click on the download button on the right side of the page. Zip file will be given.

# Downloading the CSV Dataset
Initially, the intention was to programmatically download the CSV dataset. Please download the `sleep_mobile_stress_dataset_15000.csv` file from the Datasets tab on the Kaggle dataset page linked above and place it in the `data` folder.

# Decomposing the Notebook Code into Modules
When decomposing the original notebook `(.ipynb)` into modular Python files `(.py)`, please adhere to the folder structure outlined below. This structure organizes the code into logical components: `data`, `preprocessing`, `models`, `evaluation`, `utils`, and `tests`.

While there are no strict naming conventions for the `.py` files within each folder, consider adopting descriptive names for clarity and maintainability. For example, you might use the following naming scheme:

- data/data_loader.py
- preprocessing/preprocessing.py
- utils/visualization.py

```
sleep_mobile_stress_dataset_15000/
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   └── data_loader.py
│
├── preprocessing/
│   └── preprocessing.py
│
├── utils/
│   └── visualization.py
```

