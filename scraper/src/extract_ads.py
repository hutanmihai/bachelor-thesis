import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from src.constants import BEST_FINAL_CSV, CURRENT_DATA_PATH, CURRENT_URLS_TXT_PATH, NUMBER_OF_PAGES
from src.scrape_ads import get_id
from src.utils.decorators import send_notification, show_elapsed_time
from src.utils.dirs import create_dir_if_not_exists
from src.utils.search import add_page

MAIN_PAGE_SECTION_CLASS = "ooa-10gfd0w emjt7sh1"
H1_INSIDE_SECTION_CLASS = "emjt7sh9 ooa-1ed90th er34gjf0"


@show_elapsed_time
@send_notification
def extract_ads_urls():
    create_dir_if_not_exists(CURRENT_DATA_PATH)

    old_df = pd.read_csv(BEST_FINAL_CSV)

    old_ids = set(old_df["id"])

    urls = set()

    for i in tqdm(range(NUMBER_OF_PAGES)):
        page = add_page(i)

        response = requests.get(page)
        if response.status_code != 200:
            print(f"Failed to fetch page {i}")
            continue

        soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")
        sections = soup.find_all("section", class_=MAIN_PAGE_SECTION_CLASS)

        for section in sections:
            h1_tag = section.find("h1", class_=H1_INSIDE_SECTION_CLASS)
            a_tag = h1_tag.find("a")
            if get_id(a_tag["href"]) not in old_ids:
                urls.add(a_tag["href"])

    with open(CURRENT_URLS_TXT_PATH, "w") as file:
        for url in urls:
            file.write(url + "\n")

    print(f"Extracted {len(urls)} urls")


if __name__ == "__main__":
    extract_ads_urls()
