import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


RAW_DATA_PATH = "data/raw/Apr_2023.csv.zip"   
PROCESSED_DATA_PATH = "data/processed/microgrid_processed.csv"

def preprocess():
    print("🔄 Loading raw data...")
    df = pd.read_csv(RAW_DATA_PATH)

    
    df = df.fillna(method="ffill")

    
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"✅ Data saved to {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    preprocess()
