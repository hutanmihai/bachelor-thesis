from enum import Enum

from pydantic import BaseModel, field_validator
from src.settings import settings


class ProductID(str, Enum):
    three = "three"
    five = "five"
    ten = "ten"


class CreateCheckoutSessionRequestSchema(BaseModel):
    price_id: ProductID

    @field_validator("price_id", mode="after")
    def map_id_to_stripe_price_id(cls, value):
        mapping = {
            "three": settings.stripe_price_id_three,
            "five": settings.stripe_price_id_five,
            "ten": settings.stripe_price_id_ten,
        }
        return mapping.get(value, value)


class CreateCheckoutSessionResponseSchema(BaseModel):
    url: str
