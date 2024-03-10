import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.constants import ADS_CSV_PATH, ADS_URLS_PATH
from utils.decorators import show_elapsed_time


def get_ads_urls() -> list[str]:
    """
    Reads the ADD_URLS_PATH txt file and returns a list of URLs.
    :return: A list of URLs.
    """
    with open(ADS_URLS_PATH, "r") as file:
        return [line.rstrip() for line in file.readlines()]


def get_last_path_element(url: str) -> str:
    """
    Extracts "skoda-octavia-1-6-tdi-ambition-ID7HkwJf" from https://www.autovit.ro/autoturisme/anunt/skoda-octavia-1-6-tdi-ambition-ID7HkwJf.html.
    :param url: The URL to extract the last path element from.
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
    extracted_path = get_last_path_element(url)
    return extracted_path.split("-")[-1]


def get_images_urls(soup: BeautifulSoup) -> list[str]:
    """
    Extracts the URLs of the images from the html.
    :param soup:
    :return: A list of URLs.
    """
    photo_gallery = soup.find("div", {"data-testid": "photo-gallery"})
    if not photo_gallery:
        return []  # No photo gallery found
    images = photo_gallery.find_all("img")
    return [image["src"] for image in images]


def get_details(soup: BeautifulSoup) -> dict:
    """
    Extracts the details from the html.
    :param soup:
    :return: A dictionary with the categories as keys and the values as values.
    """
    content_details_section = soup.find("div", {"data-testid": "content-details-section"})
    details_items = content_details_section.find_all("div", {"data-testid": "advert-details-item"})

    details = {}

    for item in details_items:
        children = item.find_all(["p", "a"])
        # use first children as key and second as value
        key: str = children[0].text.lower()
        value = children[1].text.lower()

        details[key] = value

    return details


def get_description(soup: BeautifulSoup) -> str | None:
    """
    Extracts the description from the html.
    :param soup:
    :return: The description or None if not found.
    """
    try:
        description = soup.find("div", {"data-testid": "content-description-section"})
        description = description.find("div", class_="ooa-unlmzs e9na3zb2")
        return description.text.lower()
    except AttributeError:
        return None


def get_equipment(soup: BeautifulSoup) -> dict[str, list[str] | list[None]]:
    """
    Extracts the equipment from the html.
    :param soup:
    :return: A dictionary with the categories as keys and the values as lists.
    """
    equipment = {}
    try:
        equipment_section = soup.find("div", {"data-testid": "content-equipments-section"})
        wrapper_div = equipment_section.find("div", class_="es9zsnd0 ooa-wja48h")

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
def get_ads_details_to_csv():
    df = pd.DataFrame(get_ads_urls(), columns=["url"])
    df["id"] = df["url"].apply(get_id)
    df["path"] = df["url"].apply(get_last_path_element)

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

        images = get_images_urls(soup)
        df.at[index, "images"] = ",".join(images)

        details = get_details(soup)
        for key, value in details.items():
            df.at[index, key] = value

        description = get_description(soup)
        df.at[index, "description"] = description

        equipment = get_equipment(soup)
        for key, value in equipment.items():
            df.at[index, key] = ",".join(value)

    df.to_csv(ADS_CSV_PATH, index=False)


if __name__ == "__main__":
    get_ads_details_to_csv()
