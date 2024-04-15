import os

import pandas as pd

from src.constants import STAGE_FINAL_CSV, STAGE_IMAGES_PATH


def final_check():
    df = pd.read_csv(STAGE_FINAL_CSV, dtype={"unique_id": "str"})
    images_dirs = os.listdir(STAGE_IMAGES_PATH)

    # check if each unique_id has a corresponding folder in STAGE_IMAGES_PATH
    for index, row in df.iterrows():
        unique_id = row["unique_id"].zfill(6)
        if unique_id not in images_dirs:
            print(f"Missing folder for {unique_id}")

    print(len(images_dirs), "images folders found")
    print(len(df), "unique_ids found")


if __name__ == "__main__":
    final_check()
