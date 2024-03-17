import requests
from bs4 import BeautifulSoup
from src.constants import DATA_PATH, NUMBER_OF_PAGES, URLS_TXT_PATH
from src.utils.decorators import send_notification, show_elapsed_time
from src.utils.dirs import create_dir_if_not_exists
from src.utils.search import add_page

MAIN_PAGE_SECTION_CLASS = "ooa-10gfd0w ekwd5px1"
H1_INSIDE_SECTION_CLASS = "ekwd5px9 ooa-1ed90th er34gjf0"


@show_elapsed_time
@send_notification
def extract_ads():

    create_dir_if_not_exists(DATA_PATH)

    urls = set()

    for i in range(NUMBER_OF_PAGES):
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
            urls.add(a_tag["href"])

    with open(URLS_TXT_PATH, "w") as file:
        for url in urls:
            file.write(url + "\n")

    print(f"Extracted {len(urls)} urls")


if __name__ == "__main__":
    extract_ads()
