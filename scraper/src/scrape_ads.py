from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.constants import CURRENT_URLS_TXT_PATH, CURRENT_RAW_CSV
from src.utils.decorators import send_notification, show_elapsed_time


def get_ads_urls() -> list[str]:
    """
    Reads the ADS_URLS_PATH txt file and returns a list of URLs.
    :return: A list of URLs.
    """
    with open(CURRENT_URLS_TXT_PATH, "r") as file:
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


def get_images_urls(soup: BeautifulSoup) -> list[str] | None:
    """
    Extracts the URLs of the images from the html.
    :param soup:
    :return: A list of URLs.
    """
    try:
        photo_gallery = soup.find("div", {"data-testid": "photo-gallery"})
        images = photo_gallery.find_all("img")
        return [image["src"] for image in images]
    except AttributeError:
        return None


def get_details(soup: BeautifulSoup) -> dict | None:
    """
    Extracts the details from the html.
    :param soup:
    :return: A dictionary with the categories as keys and the values as values.
    """
    details = {}
    try:
        content_details_section = soup.find("div", {"data-testid": "content-details-section"})
        details_items = content_details_section.find_all("div", {"data-testid": "advert-details-item"})

        for item in details_items:
            children = item.find_all(["p", "a"])
            # use first children as key and second as value
            key: str = children[0].text.lower()
            value = children[1].text.lower()

            details[key] = value

        return details

    except AttributeError:
        return None


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


def get_equipment(soup: BeautifulSoup) -> dict[str, list[str]] | None:
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
        return None


def get_price(soup: BeautifulSoup) -> str | None:
    """
    Extracts the price from the html.
    :param soup:
    :return: The price or None if not found.
    """
    try:
        price = soup.find("h3", class_="offer-price__number eqdspoq4 ooa-o7wv9s er34gjf0")
        # replace spcaes
        price = price.text.replace(" ", "")
        return price
    except AttributeError:
        return None
    except ValueError:
        return None


def get_currency(soup: BeautifulSoup) -> str | None:
    """
    Extracts the currency from the html.
    :param soup:
    :return: The currency or None if not found.
    """
    try:
        currency = soup.find("p", class_="offer-price__currency eqdspoq5 ooa-pk2ls er34gjf0")
        return currency.text.lower()
    except AttributeError:
        return None


def process_row(df, index, row):
    global response

    url = row["url"]

    # retry requsting 3 times if it fails
    for _ in range(3):
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print(f"DNS failure, retrying {url}")
            continue
        if response.status_code == 200:
            break

    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return

    soup = BeautifulSoup(response.text, "lxml")

    images = get_images_urls(soup)
    if images:
        df.at[index, "images"] = ",".join(images)

    details = get_details(soup)
    if details:
        for key, value in details.items():
            df.at[index, key] = value

    description = get_description(soup)
    df.at[index, "description"] = description

    equipment = get_equipment(soup)
    if equipment:
        for key, value in equipment.items():
            df.at[index, key] = ",".join(value)

    price = get_price(soup)
    df.at[index, "price"] = price

    currency = get_currency(soup)
    df.at[index, "currency"] = currency


@show_elapsed_time
@send_notification
def get_ads_details_to_csv():
    df = pd.DataFrame(get_ads_urls(), columns=["url"])
    df["id"] = df["url"].apply(get_id)
    df["path"] = df["url"].apply(get_last_path_element)

    df["images"] = None
    df["audio si tehnologie"] = [None] * df.shape[0]
    df["confort si echipamente optionale"] = [None] * df.shape[0]
    df["electronice si sisteme de asistenta"] = [None] * df.shape[0]
    df["performanta"] = [None] * df.shape[0]
    df["siguranta"] = [None] * df.shape[0]
    df["vehicule electrice"] = [None] * df.shape[0]

    with ThreadPoolExecutor() as executor:
        futures = []

        for index, row in df.iterrows():
            future = executor.submit(process_row, df, index, row)
            futures.append(future)

        # Wait for all futures to complete
        for future in futures:
            future.result()

    df.to_csv(CURRENT_RAW_CSV, index=False)


if __name__ == "__main__":
    get_ads_details_to_csv()
