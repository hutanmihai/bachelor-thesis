import os

import pandas as pd
from constants import TEST_DATA_CSV, TRAIN_DATA_CSV

train_data = pd.read_csv(TRAIN_DATA_CSV, dtype={"unique_id": "str"})
test_data = pd.read_csv(TEST_DATA_CSV, dtype={"unique_id": "str"})

unique_ids = pd.concat([train_data["unique_id"], test_data["unique_id"]], ignore_index=True)
unique_ids = unique_ids.values

for image in os.listdir("../data/resized_images"):
    if image.rstrip(".png") not in unique_ids:
        os.remove(f"../data/resized_images/{image}")
