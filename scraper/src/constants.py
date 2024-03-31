from pathlib import Path

BASE_URL = "https://www.autovit.ro/autoturisme?search%5Bfilter_enum_damaged%5D=0"
NUMBER_OF_PAGES = 500

NUMBER_OF_IMAGES_MAX_PER_AD = 10

STAGE_DATA_PATH = Path("../data/stage")
CURRENT_DATA_PATH = Path("../data/current")
BEST_DATA_PATH = Path("../data/best")

STAGE_IMAGES_PATH = STAGE_DATA_PATH / "images"
CURRENT_IMAGES_PATH = CURRENT_DATA_PATH / "images"
BEST_IMAGES_PATH = BEST_DATA_PATH / "images"

CURRENT_URLS_TXT_PATH = CURRENT_DATA_PATH / "urls.txt"
CURRENT_RAW_CSV = CURRENT_DATA_PATH / "raw.csv"

STAGE_FINAL_CSV = STAGE_DATA_PATH / "final.csv"
CURRENT_FINAL_CSV = CURRENT_DATA_PATH / "final.csv"
BEST_FINAL_CSV = BEST_DATA_PATH / "final.csv"
