import unittest
import pandas as pd
from data.data_loader import load_dataset
import config

class TestDataLoader(unittest.TestCase):

    def test_load_dataset_success(self):
        """Test that the dataset loads successfully into a pandas DataFrame."""
        df = load_dataset(config.DATA_PATH)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_load_dataset_file_not_found(self):
        """Test that a FileNotFoundError is raised if the path doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            load_dataset('invalid_path/wrong_file.csv')

if __name__ == '__main__':
    unittest.main()
