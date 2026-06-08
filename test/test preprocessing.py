import unittest
from data.data_loader import load_dataset
from preprocessing.preprocessing import compute_average_screen_time
import pandas as pd
import config

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        """Load the real dataset once before running tests."""
        self.df = load_dataset(config.DATA_PATH)

    def test_compute_average_screen_time(self):
        """Test that the screen time aggregation returns a valid Pandas Series."""
        avg_screen_time = compute_average_screen_time(self.df)

        # Verify it outputted an indexed Series
        self.assertIsInstance(avg_screen_time, pd.Series)
        # Ensure it has values inside
        self.assertGreater(len(avg_screen_time), 0)

if __name__ == '__main__':
    unittest.main()
