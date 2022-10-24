import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../Causal-Inference/scripts/")))
from eda_pipeline import EDAPipeline
df = pd.read_csv("./tests/sample_data.csv")

class TestEDAPipeline(unittest.TestCase):
    def setUp(self) -> None:
        # self.df = df_g.copy()
        self.pipeline = EDAPipeline()

    def test_is_weekend(self):
        df['is_weekend'] = df['Trip Start Time'].apply(lambda x: self.pipeline.isWeekend(x))
        self.assertEqual(df['is_weekend'].tolist(), [0,0,0,0,0,0])

    def test_is_holiday(self):
        df['is_holiday'] = df['Trip Start Time'].apply(lambda x: self.pipeline.isHoliday(x))
        self.assertEqual(df['is_holiday'].tolist(), [0,0,0,0,0,0])


if __name__ == "__main__":
    unittest.main()