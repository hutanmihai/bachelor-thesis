import os
import shutil
from pathlib import Path

import pandas as pd
from constants import FINAL_CSV, IMAGES_PATH
from tqdm import tqdm

df = pd.read_csv(FINAL_CSV, dtype={"unique_id": str})
df["unique_id"] = df["unique_id"].apply(lambda x: x.zfill(6))

train_images = df["unique_id"].values
source_paths = [IMAGES_PATH / path / "00.png" for path in train_images]

destination_folder = Path("./images")

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

for src, unique_id in tqdm(zip(source_paths, train_images)):
    dest = destination_folder / f"{unique_id}.png"
    shutil.copy(src, dest)  # This moves and renames the file

print("Files have been moved and renamed successfully.")
