import re

import emoji
from transformers import AutoModelForTextEncoding, AutoTokenizer


def preprocess_description(description: str) -> str:
    def replace_patterns(text: str):
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
        html_pattern = r"<.*?>"
        text = re.sub(email_pattern, "[EMAIL]", text)
        text = re.sub(phone_pattern, "[TEL]", text)
        text = re.sub(html_pattern, "[HTML]", text)
        return text

    def replace_emojis(text: str):
        return emoji.demojize(text, delimiters=("[", "]"))

    def replace_repeated_whitespace(text: str):
        return re.sub(r"\s+", " ", text)

    description = replace_patterns(description)
    description = replace_emojis(description)
    description = replace_repeated_whitespace(description)
    return description


tokenizer = AutoTokenizer.from_pretrained("dumitrescustefan/bert-base-romanian-cased-v1")
model = AutoModelForTextEncoding.from_pretrained("dumitrescustefan/bert-base-romanian-cased-v1")
