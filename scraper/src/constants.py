from pathlib import Path

BASE_URL = "https://www.autovit.ro/autoturisme?search%5Bfilter_enum_damaged%5D=0"
NUMBER_OF_PAGES = 500

DATA_PATH = Path("../data")
IMAGES_PATH = DATA_PATH / "images"
ADS_URLS_PATH = DATA_PATH / "ads_urls.txt"
ADS_CSV_PATH = DATA_PATH / "ads.csv"
CLEANED_ADS_CSV_PATH = DATA_PATH / "cleaned_ads.csv"
FINAL_DATA_PATH = DATA_PATH / "final_data.csv"
