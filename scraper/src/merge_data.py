import shutil
from pathlib import Path

import pandas as pd
from src.constants import (
    BEST_FINAL_CSV,
    BEST_IMAGES_PATH,
    CURRENT_FINAL_CSV,
    CURRENT_IMAGES_PATH,
    STAGE_DATA_PATH,
    STAGE_FINAL_CSV,
    STAGE_IMAGES_PATH,
)
from src.utils.decorators import send_notification, show_elapsed_time
from src.utils.dirs import create_dir_if_not_exists
from tqdm import tqdm


@show_elapsed_time
@send_notification
def merge_data():
    create_dir_if_not_exists(STAGE_DATA_PATH)

    old_df = pd.read_csv(BEST_FINAL_CSV)
    new_df = pd.read_csv(CURRENT_FINAL_CSV)
    initial_number_of_rows = len(old_df)
    number_of_new_rows = len(new_df)

    print(f"Initial number of rows: {initial_number_of_rows}")
    print(f"Number of new rows: {number_of_new_rows}")

    # Merge the data
    final_df = pd.concat([old_df, new_df], ignore_index=True)

    # Quick check for any collision on id and unique_id columns
    if final_df["id"].nunique() != final_df["id"].count():
        raise ValueError("There are duplicate ids in the final dataframe.")
    if final_df["unique_id"].nunique() != final_df["unique_id"].count():
        raise ValueError("There are duplicate unique_ids in the final dataframe.")

    # Save the final data
    final_df.to_csv(STAGE_FINAL_CSV, index=False)

    # Images
    create_dir_if_not_exists(STAGE_IMAGES_PATH)

    for dir in tqdm(Path(CURRENT_IMAGES_PATH).iterdir()):
        shutil.copytree(dir, STAGE_IMAGES_PATH / dir.name)

    for dir in tqdm(Path(BEST_IMAGES_PATH).iterdir()):
        shutil.copytree(dir, STAGE_IMAGES_PATH / dir.name)


if __name__ == "__main__":
    merge_data()
