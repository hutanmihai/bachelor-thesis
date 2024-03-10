import timeit

import requests
from bs4 import BeautifulSoup
from src.constants import NUMBER_OF_PAGES
from utils.search import add_page


def extract_ads():
    hrefs = set()

    for i in range(1, NUMBER_OF_PAGES + 1):
        page = add_page(i)
        found = 0

        response = requests.get(page)
        if response.status_code != 200:
            print(f"Failed to fetch page {i}")
            continue

        soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")
        sections = soup.find_all("section", class_="ooa-10gfd0w e1oqyyyi1")

        for section in sections:
            h1_tag = section.find("h1", class_="e1oqyyyi9 ooa-1ed90th er34gjf0")
            a_tag = h1_tag.find("a")
            hrefs.add(a_tag["href"])
            found += 1

        print(f"Page {i}: Found {found} hrefs.")

    with open("../data/ads_hrefs.txt", "w") as file:
        for href in hrefs:
            file.write(href + "\n")


if __name__ == "__main__":
    start_time = timeit.default_timer()
    extract_ads()
    elapsed = timeit.default_timer() - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds.")
