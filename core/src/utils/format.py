import re

import bs4
import emoji
import pandas as pd


def drop_na(df: pd.DataFrame, col: str) -> pd.DataFrame:
    initial_len = len(df)
    df = df.dropna(subset=[col])
    final_len = len(df)
    print(f"Dropped {initial_len - final_len} rows for missing {col} values.")
    return df


def replace_patterns(text: str):
    email_pattern = r'\b(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))\b'
    phone_pattern = r"\b^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$\b"
    url_pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
    soup = bs4.BeautifulSoup(text, "html.parser")
    text = re.sub(email_pattern, "", text)
    text = re.sub(phone_pattern, "", text)
    text = re.sub(url_pattern, "", text)
    text = soup.get_text(text)

    # bert specific
    replacements = {"ţ": "ț", "ş": "ș", "Ţ": "Ț", "Ş": "Ș"}
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def replace_emojis(text: str):
    return emoji.replace_emoji(text, "")


def preprocess_text(text: str) -> str:
    text = replace_patterns(text)
    text = replace_emojis(text)
    return text
