from io import BytesIO
from re import sub

import pandas as pd
from bs4 import BeautifulSoup
from emoji import replace_emoji
from PIL import Image
from requests import get
from src.ml import ml_ops
from torch import cat, float32, tensor


class PreprocessSrv:
    def preprocess_text(self, text: str) -> str:
        def replace_patterns(text: str):
            email_pattern = r'\b(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))\b'
            phone_pattern = r"\b^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$\b"
            url_pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
            soup = BeautifulSoup(text, "lxml")
            text = sub(email_pattern, "", text)
            text = sub(phone_pattern, "", text)
            text = sub(url_pattern, "", text)
            text = soup.get_text(text)

            # bert specific
            replacements = {"ţ": "ț", "ş": "ș", "Ţ": "Ț", "Ş": "Ș"}
            for key, value in replacements.items():
                text = text.replace(key, value)
            return text

        def replace_emojis(text: str):
            return replace_emoji(text, "")

        text = replace_patterns(text)
        text = replace_emojis(text)
        return text

    def preprocess_image(self, image_url: str):
        response = get(image_url)
        image = BytesIO(response.content)
        image = Image.open(image)
        image = ml_ops.transforms(image).unsqueeze(0)
        return image

    def preprocess_structured_data(self, numerical_data: list, categorical_data: list):
        categorical_df = pd.DataFrame([categorical_data], columns=["manufacturer", "model", "fuel", "chassis"])
        numerical_df = pd.DataFrame([numerical_data], columns=["km", "power", "engine_capacity", "year"])
        categorical_encoded = ml_ops.target_encoder.transform(categorical_df)
        numerical_scaled = ml_ops.scaler_numerical.transform(numerical_df)
        numerical_scaled_df = pd.DataFrame(numerical_scaled, columns=["km", "power", "engine_capacity", "year"])
        categorical_scaled = ml_ops.scaler_categorical.transform(categorical_encoded)
        categorical_scaled_df = pd.DataFrame(categorical_scaled, columns=["manufacturer", "model", "fuel", "chassis"])
        df = pd.concat([numerical_scaled_df, categorical_scaled_df], axis=1)
        df = df[["manufacturer", "model", "year", "km", "power", "engine_capacity", "fuel", "chassis"]]
        data = tensor(df.values, dtype=float32)
        return data

    def tokenize(self, text: str) -> dict:
        return ml_ops.tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
