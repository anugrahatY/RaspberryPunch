import pandas as pd
import os

PROCESSED_DATA_PATH = "data/processed/microgrid_processed.csv"
FEATURED_DATA_PATH = "data/processed/microgrid_featured.csv"

def create_features():
    print("🔧 Creating new features...")
    df = pd.read_csv(PROCESSED_DATA_PATH)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)

    df['hour'] = df.index.hour
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['is_weekend'] = (df.index.dayofweek >= 5).astype(int)
    
    df.to_csv(FEATURED_DATA_PATH)
    print(f"✅ Features saved to {FEATURED_DATA_PATH}")

if __name__ == "__main__":
    create_features()
