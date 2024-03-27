from pathlib import Path

BASE_URL = "https://www.autovit.ro/autoturisme?search%5Bfilter_enum_damaged%5D=0"
NUMBER_OF_PAGES = 600

NUMBER_OF_IMAGES_MAX_PER_AD = 10

STAGE_DATA_PATH = Path("../data/stage")
CURRENT_DATA_PATH = Path("../data/current")
DATA_LAST_PATH = Path("../data/last_data")

STAGE_IMAGES_PATH = STAGE_DATA_PATH / "images"
CURRENT_IMAGES_PATH = CURRENT_DATA_PATH / "images"
IMAGES_LAST_PATH = DATA_LAST_PATH / "images"

STAGE_URLS_TXT_PATH = STAGE_DATA_PATH / "urls.txt"
CURRENT_URLS_TXT_PATH = CURRENT_DATA_PATH / "urls.txt"
URLS_LAST_TXT_PATH = DATA_LAST_PATH / "urls.txt"

CURRENT_RAW_CSV = CURRENT_DATA_PATH / "raw.csv"
CURRENT_CLEANED_CSV = CURRENT_DATA_PATH / "cleaned.csv"

STAGE_FINAL_CSV = STAGE_DATA_PATH / "final.csv"
CURRENT_FINAL_CSV = CURRENT_DATA_PATH / "final.csv"
FINAL_LAST_CSV = DATA_LAST_PATH / "final.csv"
