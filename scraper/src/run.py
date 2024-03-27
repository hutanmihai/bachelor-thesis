from src.check_images import check_images
from src.clean_csv import clean_csv
from src.download_images import download_images
from src.extract_ads import extract_ads
from src.merge_data import merge_data
from src.scrape_ads import get_ads_details_to_csv

if __name__ == '__main__':
    extract_ads()
    get_ads_details_to_csv()
    clean_csv()
    download_images()
    check_images()
    merge_data()
