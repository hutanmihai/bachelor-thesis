import pandas as pd


def drop_na(df: pd.DataFrame, col: str) -> pd.DataFrame:
    initial_len = len(df)
    df = df.dropna(subset=[col])
    final_len = len(df)
    print(f"Dropped {initial_len - final_len} rows for missing {col} values.")
    return df
