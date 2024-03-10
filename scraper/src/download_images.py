import timeit

import pandas as pd
import requests
from PIL import Image
from src.constants import ADS_CSV_PATH, IMAGES_PATH
from src.utils.decorators import show_elapsed_time
from src.utils.dirs import create_dir_if_not_exists


@show_elapsed_time
def download_images():
    df = pd.read_csv(ADS_CSV_PATH)

    create_dir_if_not_exists(IMAGES_PATH)

    for index, row in df.iterrows():
        start_time = timeit.default_timer()

        images_urls = row["images"].split(",")
        id = row["id"]

        create_dir_if_not_exists(IMAGES_PATH / id)

        for idx, image in enumerate(images_urls):
            actual_image = Image.open(requests.get(image, stream=True).raw)
            actual_image.save(f"{IMAGES_PATH}/{id}/{str(idx).zfill(2)}.jpg")

            # Limit the number of images to download for each ad
            if idx > 20:
                break

        print(f"Elapsed time for {row['url']}: {timeit.default_timer() - start_time:.2f} seconds.")


if __name__ == "__main__":
    download_images()
