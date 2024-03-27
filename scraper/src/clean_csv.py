import pandas as pd
from src.constants import CURRENT_CLEANED_CSV, CURRENT_RAW_CSV


def clean_csv():
    df = pd.read_csv(CURRENT_RAW_CSV)

    print(f"Initial number of rows: {len(df)}")

    df = df.dropna(subset=["images", "price", "currency", "marca", "model", "anul producției"])
    df.to_csv(CURRENT_CLEANED_CSV, index=False)

    print(f"Number of rows after removing missing values: {len(df)}")


if __name__ == "__main__":
    clean_csv()
