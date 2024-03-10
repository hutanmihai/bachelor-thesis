import requests
from bs4 import BeautifulSoup
from constants import ADS_URLS_PATH, DATA_PATH, NUMBER_OF_PAGES
from utils.decorators import show_elapsed_time
from utils.dirs import create_dir_if_not_exists
from utils.search import add_page


@show_elapsed_time
def extract_ads():

    create_dir_if_not_exists(DATA_PATH)

    urls = set()

    for i in range(1, NUMBER_OF_PAGES + 1):
        page = add_page(i)

        response = requests.get(page)
        if response.status_code != 200:
            print(f"Failed to fetch page {i}")
            continue

        soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")
        sections = soup.find_all("section", class_="ooa-10gfd0w e1oqyyyi1")

        for section in sections:
            h1_tag = section.find("h1", class_="e1oqyyyi9 ooa-1ed90th er34gjf0")
            a_tag = h1_tag.find("a")
            urls.add(a_tag["href"])

    with open(ADS_URLS_PATH, "w") as file:
        for url in urls:
            file.write(url + "\n")


if __name__ == "__main__":
    extract_ads()
