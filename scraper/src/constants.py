from pathlib import Path

BASE_URL = "https://www.autovit.ro/autoturisme?search%5Bfilter_enum_damaged%5D=0"
NUMBER_OF_PAGES = 600

NUMBER_OF_IMAGES_MAX_PER_AD = 10

DATA_PATH = Path("../data")
IMAGES_PATH = DATA_PATH / "images"
URLS_TXT_PATH = DATA_PATH / "urls.txt"
RAW_CSV = DATA_PATH / "raw.csv"
CLEANED_CSV = DATA_PATH / "cleaned.csv"
GROUPED_CSV = DATA_PATH / "grouped.csv"
FINAL_CSV = DATA_PATH / "final.csv"
