import pickle
import pandas as pd

def load_data(path: str):
    return pd.read_csv(path)

def save_model(model, path: str):
    with open(path, "wb") as f:
        pickle.dump(model, f)

def load_model(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)
