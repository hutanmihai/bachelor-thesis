import pandas as pd
from src.constants import ADS_CSV_PATH, CLEANED_ADS_CSV_PATH

if __name__ == "__main__":
    df = pd.read_csv(ADS_CSV_PATH)

    print(f"Initial number of rows: {len(df)}")

    df = df.dropna(subset=["images", "price", "currency", "marca", "model", "anul producției"])
    df.to_csv(CLEANED_ADS_CSV_PATH, index=False)

    print(f"Number of rows after removing missing values: {len(df)}")
