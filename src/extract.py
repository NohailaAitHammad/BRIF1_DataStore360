import pandas as pd


def extract_data() :
      file_path = r'data/raw/Sample - Superstore.csv'
      df = pd.read_csv(file_path)
      print("/=== Extraction ===/")
      print("Shape de dataset", df.shape)
      return df