import glob
import os

import pandas as pd
from src.constants import CLEANED_ADS_CSV_PATH, FINAL_DATA_PATH, IMAGES_PATH

if __name__ == "__main__":
    found = 0
    ids = set()
    for dir in os.listdir(IMAGES_PATH):
        images = glob.glob(f"{IMAGES_PATH}/{dir}/*.png")
        if len(images) < 2:
            found += 1
            print(f"Found {len(images)} images for {dir}")
            ids.add(dir)

    df = pd.read_csv(CLEANED_ADS_CSV_PATH)
    print(f"Initial number of rows: {len(df)}")

    df = df[~df["id"].isin(ids)]
    df = df.drop(columns=["images"])

    df.to_csv(FINAL_DATA_PATH, index=False)

    print(f"Number of rows after removing missing images: {len(df)}")
