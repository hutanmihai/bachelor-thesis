from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import PIL
import requests
from PIL import Image
from src.constants import CLEANED_CSV, IMAGES_PATH, NUMBER_OF_IMAGES_MAX_PER_AD
from src.utils.decorators import show_elapsed_time
from src.utils.dirs import create_dir_if_not_exists


def download_image(image_url, folder_path, image_index):
    try:
        response = requests.get(image_url, stream=True)
        actual_image = Image.open(response.raw).convert("RGB")
        actual_image.save(f"{folder_path}/{str(image_index).zfill(2)}.png")
    except requests.ConnectionError:
        print(f"DNS failure, Failed to download {image_url}")
    except PIL.UnidentifiedImageError:
        print(f"PIL error, Failed to download {image_url}")


@show_elapsed_time
def download_images():
    df = pd.read_csv(CLEANED_CSV)

    create_dir_if_not_exists(IMAGES_PATH)

    with ThreadPoolExecutor() as executor:
        futures = []
        for index, row in df.iterrows():
            try:
                images_urls = row["images"]
                images_urls = images_urls.split(",")
            except AttributeError:
                print(f"Failed to extract images for {row['images']}")
                continue

            id = row["id"]

            create_dir_if_not_exists(IMAGES_PATH / id)

            try:
                for idx, image in enumerate(images_urls):
                    if idx > NUMBER_OF_IMAGES_MAX_PER_AD - 1:
                        break
                    future = executor.submit(download_image, image, f"{IMAGES_PATH}/{id}", idx)
                    futures.append(future)
            except:
                print(images_urls)

        for future in futures:
            future.result()


if __name__ == "__main__":
    download_images()
