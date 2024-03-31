import glob
import os
import shutil

import pandas as pd
from src.constants import CURRENT_RAW_CSV, CURRENT_FINAL_CSV, CURRENT_IMAGES_PATH, NUMBER_OF_IMAGES_MAX_PER_AD


def check_images():
    found = 0
    ids = set()
    for dir in os.listdir(CURRENT_IMAGES_PATH):
        images = glob.glob(f"{CURRENT_IMAGES_PATH}/{dir}/*.png")
        if len(images) < NUMBER_OF_IMAGES_MAX_PER_AD:
            found += 1
            print(f"Found {len(images)} images for {dir}")
            ids.add(dir)

    df = pd.read_csv(CURRENT_RAW_CSV, dtype={'unique_id': str})
    print(f"Initial number of rows: {len(df)}")

    df = df[~df["unique_id"].zfill(6).isin(ids)]
    df = df.drop(columns=["images"])

    df.to_csv(CURRENT_FINAL_CSV, index=False)

    for _id in ids:
        shutil.rmtree(f"{CURRENT_IMAGES_PATH}/{_id}")

    print(f"Number of rows after removing missing images: {len(df)}")


if __name__ == "__main__":
    check_images()
