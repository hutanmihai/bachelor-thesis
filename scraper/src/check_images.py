import glob
import os

import pandas as pd
from src.constants import CLEANED_CSV, FINAL_CSV, IMAGES_PATH, NUMBER_OF_IMAGES_MAX_PER_AD

if __name__ == "__main__":
    found = 0
    ids = set()
    for dir in os.listdir(IMAGES_PATH):
        images = glob.glob(f"{IMAGES_PATH}/{dir}/*.png")
        if len(images) < NUMBER_OF_IMAGES_MAX_PER_AD:
            found += 1
            print(f"Found {len(images)} images for {dir}")
            ids.add(dir)

    df = pd.read_csv(CLEANED_CSV)
    print(f"Initial number of rows: {len(df)}")

    df = df[~df["id"].isin(ids)]
    df = df.drop(columns=["images"])

    df.to_csv(FINAL_CSV, index=False)

    print(f"Number of rows after removing missing images: {len(df)}")
