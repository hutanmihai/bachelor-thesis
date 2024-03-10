import time

import requests
from bs4 import BeautifulSoup
from PIL import Image
from utils.search import add_page

if __name__ == "__main__":
    first_page = add_page(1)

    response = requests.get(first_page)
    html_content = response.text

    soup: BeautifulSoup = BeautifulSoup(html_content, "lxml")

    sections = soup.find_all("section", class_="ooa-10gfd0w e1oqyyyi1")

    images_urls = []

    for section in sections:
        # Standalone images
        standalone_images = section.find_all("img", class_="e17vhtca4 ooa-2zzg2s", recursive=True)
        for img in standalone_images:
            if not img.find_parent("div", {"data-testid": "carousel-container"}):
                images_urls.append(img["src"])

        # Carousel images
        carousels = section.find_all("div", {"data-testid": "carousel-container"}, recursive=True)
        for carousel in carousels:
            # Attempt to find the first image within the carousel
            img = carousel.find("img", class_="e17vhtca4 ooa-2zzg2s")
            if img and img["src"] not in images_urls:
                images_urls.append(img["src"])

    images = [img for img in images_urls if img.startswith("https://")]

    for image in images:
        actual_image = Image.open(requests.get(image, stream=True).raw).resize((224, 224))
        actual_image.show()
        time.sleep(5)
        actual_image.close()
