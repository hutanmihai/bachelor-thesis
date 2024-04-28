import torch
from src.ml import ml_ops
from src.services.preprocess_srv import PreprocessSrv
from torch import cat, cuda, float32, tensor


class InferenceSrv:
    def __init__(self):
        self.DEVICE = "cuda" if cuda.is_available() else "cpu"
        self.preprocess = PreprocessSrv()

    DEVICE = "cuda" if cuda.is_available() else "cpu"

    async def get_image_features(self, image_url: str):
        image = self.preprocess.preprocess_image(image_url)
        image = image.to(self.DEVICE)
        with torch.no_grad():
            image_features = ml_ops.fastvit_model(image)
        return image_features

    async def get_text_features(self, text):
        text = self.preprocess.preprocess_text(text)
        text = self.preprocess.tokenize(text)
        input_ids = text["input_ids"].to(self.DEVICE)
        attention_mask = text["attention_mask"].to(self.DEVICE)
        with torch.no_grad():
            outputs = ml_ops.bert_model(input_ids, attention_mask=attention_mask)
        text_features = outputs.hidden_states[-1].mean(dim=1)
        return text_features

    async def get_structured_data_features(self, numerical_data, categorical_data):
        data = self.preprocess.preprocess_structured_data(numerical_data, categorical_data)
        return data

    async def predict(
        self,
        manufacturer: str,
        model: str,
        fuel: str,
        chassis: str,
        sold_by: str,
        gearbox: str,
        km: int,
        power: int,
        engine: int,
        year: int,
        description: str,
        image_url: str,
    ):
        image = await self.get_image_features(image_url)
        text = await self.get_text_features(description)

        numerical_data = [km, power, engine, 2024 - year]
        categorical_data = [manufacturer, model, fuel, chassis]

        structured_data = await self.get_structured_data_features(numerical_data, categorical_data)

        structured = tensor(structured_data, dtype=float32).to(self.DEVICE)
        booleans = tensor([[1 if sold_by == "dealer" else 0, 1 if gearbox == "automatic" else 0]]).to(self.DEVICE)
        structured = cat([structured, booleans], dim=1)

        features = cat([image, text, structured], dim=1)

        with torch.no_grad():
            prediction = ml_ops.model(features)
        prediction = int(prediction.item())

        return prediction
