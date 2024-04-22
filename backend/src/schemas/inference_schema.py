from pydantic import BaseModel, Field


class StructuredDataSchema(BaseModel):
    # categorical
    manufacturer: str
    model: str
    fuel: str
    sold_by: bool  # True for dealer, False for private
    gearbox: bool  # True for automatic, False for manual
    chassis: str

    # numerical
    km: int
    power: int
    engine: int
    year: int


class InferenceResponseSchema(BaseModel):
    prediction: float = Field(..., example=10000)
