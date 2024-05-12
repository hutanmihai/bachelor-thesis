from constants import DATA_PATH, IMAGES_PATH
from PIL import Image
from tqdm import tqdm


# read all images from the folder and resize them to 256x256
# save them in a new folder named resized_images
def resize_images():
    resized_images_path = DATA_PATH / "resized_images"
    resized_images_path.mkdir(exist_ok=True)
    for image_path in tqdm(IMAGES_PATH.iterdir()):
        if image_path.is_file():
            image = Image.open(image_path)
            image = image.resize((256, 256))
            image.save(resized_images_path / image_path.name)


if __name__ == "__main__":
    resize_images()
