import pandas as pd
from src.constants import CLEANED_CSV, RAW_CSV

if __name__ == "__main__":
    df = pd.read_csv(RAW_CSV)

    print(f"Initial number of rows: {len(df)}")

    df = df.dropna(subset=["images", "price", "currency", "marca", "model", "anul producției"])
    df.to_csv(CLEANED_CSV, index=False)

    print(f"Number of rows after removing missing values: {len(df)}")
