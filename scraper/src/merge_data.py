from pathlib import Path
import pandas as pd
import shutil

from src.constants import CURRENT_FINAL_CSV, FINAL_LAST_CSV, STAGE_FINAL_CSV, STAGE_IMAGES_PATH, CURRENT_IMAGES_PATH, \
    IMAGES_LAST_PATH, URLS_LAST_TXT_PATH, CURRENT_URLS_TXT_PATH, STAGE_URLS_TXT_PATH, STAGE_DATA_PATH
from src.utils.decorators import send_notification, show_elapsed_time
from src.utils.dirs import create_dir_if_not_exists


@show_elapsed_time
@send_notification
def merge_data():
    create_dir_if_not_exists(STAGE_DATA_PATH)

    old_df = pd.read_csv(FINAL_LAST_CSV)
    new_df = pd.read_csv(CURRENT_FINAL_CSV)
    initial_number_of_rows = len(old_df)
    number_of_new_rows = len(new_df)

    print(f"Initial number of rows: {initial_number_of_rows}")
    print(f"Number of new rows: {number_of_new_rows}")

    # Merge the data
    final_df = pd.concat([old_df, new_df], ignore_index=True)

    # Save the final data
    final_df.to_csv(STAGE_FINAL_CSV, index=False)

    # Urls txt files
    with open(URLS_LAST_TXT_PATH, "r") as file:
        old_urls = set(file.read().splitlines())

    with open(CURRENT_URLS_TXT_PATH, "r") as file:
        new_urls = set(file.read().splitlines())

    urls = old_urls.union(new_urls)

    with open(STAGE_URLS_TXT_PATH, "w") as file:
        for url in urls:
            file.write(url + "\n")

    # Images
    create_dir_if_not_exists(STAGE_IMAGES_PATH)

    for dir in Path(CURRENT_IMAGES_PATH).iterdir():
        shutil.copytree(dir, STAGE_IMAGES_PATH / dir.name)

    for dir in Path(IMAGES_LAST_PATH).iterdir():
        shutil.copytree(dir, STAGE_IMAGES_PATH / dir.name)


if __name__ == '__main__':
    merge_data()
