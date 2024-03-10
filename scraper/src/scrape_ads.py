import re
import timeit

import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.utils.decorators import show_elapsed_time


def get_ads_urls() -> list[str]:
    """
    Reads the ads_hrefs.txt file and returns a list of URLs.
    :return: A list of URLs.
    """
    with open("../data/ads_hrefs.txt", "r") as file:
        return [line.rstrip() for line in file.readlines()]


def get_full_path(url: str) -> str:
    """
    Extracts "skoda-octavia-1-6-tdi-ambition-ID7HkwJf" from https://www.autovit.ro/autoturisme/anunt/skoda-octavia-1-6-tdi-ambition-ID7HkwJf.html.
    :param url: The URL to extract the path from.
    :return: The extracted path.
    """
    start_index = url.find("anunt/") + len("anunt/")
    end_index = url.find(".html")

    return url[start_index:end_index]


def get_id(url: str) -> str:
    """
    Extract the ID from the URL.
    :param url: The URL to extract the ID from.
    :return: The extracted ID.
    """
    extracted_path = get_full_path(url)
    return extracted_path.split("-")[-1]


def get_images(soup: BeautifulSoup) -> list[str]:
    photo_gallery = soup.find("div", {"data-testid": "photo-gallery"})
    if not photo_gallery:
        return []  # No photo gallery found
    images = photo_gallery.find_all("img")
    return [image["src"] for image in images]


def get_details(soup: BeautifulSoup) -> dict:
    content_details_sections = soup.find("div", {"data-testid": "content-details-section"})
    details_items = content_details_sections.find_all("div", {"data-testid": "advert-details-item"})

    details = {}

    for item in details_items:
        children = item.find_all(["p", "a"])
        # use first children as key and second as value
        key: str = children[0].text.lower()
        value = children[1].text.lower()

        details[key] = value

    return details


def get_description(soup: BeautifulSoup) -> str | None:
    try:
        description = soup.find("div", {"data-testid": "content-description-section"})
        description = description.find("div", class_="ooa-unlmzs e9na3zb2")
        return description.text
    except AttributeError:
        return None


def get_equipment(soup: BeautifulSoup) -> dict[str, list[str] | list[None]]:
    equipment = {}
    try:
        equipment_section = soup.find("div", {"data-testid": "content-equipments-section"})
        wrapper_div = equipment_section.find("div", class_="es9zsnd0 ooa-wja48h")

        # find direct children divs
        children = wrapper_div.findChildren("div", recursive=False)

        for child_title, child_values in zip(children[::2], children[1::2]):
            title = child_title.text.lower()
            # find all paragraphs within the current category (each paragraph corresponds to an item)
            values = child_values.find_all("p", class_="e1ic0wg14 ooa-1i4y99d er34gjf0")
            values = [value.text.lower() for value in values]

            equipment[title] = values

        return equipment

    except AttributeError:
        return {}


@show_elapsed_time
def main():
    df = pd.DataFrame(get_ads_urls(), columns=["url"])
    df["id"] = df["url"].apply(get_id)
    df["path"] = df["url"].apply(get_full_path)

    df["images"] = ""
    df["audio si tehnologie"] = [None] * df.shape[0]
    df["confort si echipamente optionale"] = [None] * df.shape[0]
    df["electronice si sisteme de asistenta"] = [None] * df.shape[0]
    df["performanta"] = [None] * df.shape[0]
    df["siguranta"] = [None] * df.shape[0]
    df["vehicule electrice"] = [None] * df.shape[0]

    for index, row in df.iterrows():
        url = row["url"]
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.text, "lxml")

        images = get_images(soup)
        df.at[index, "images"] = images

        details = get_details(soup)
        for key, value in details.items():
            df.at[index, key] = value

        description = get_description(soup)
        df.at[index, "description"] = description

        equipment = get_equipment(soup)
        for key, value in equipment.items():
            df.at[index, key] = value

    df.to_csv("../data/ads.csv", index=False)


if __name__ == "__main__":
    main()
