import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import numpy as np 

RAW_DATA_PATH = "data/raw/Apr_2023.csv.zip"
PROCESSED_DATA_PATH = "data/processed/microgrid_processed.csv"

def preprocess():
    print("🔄 Loading raw data...")
    df = pd.read_csv(RAW_DATA_PATH)

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)

    df.replace(-999999.0, np.nan, inplace=True)

    df = df.fillna(method="ffill")
    df.dropna(axis=1, how='all', inplace=True)

    print(" Scaling data...")
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("Saving processed data...")
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH)
    print(f" Data saved to {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    preprocess()
