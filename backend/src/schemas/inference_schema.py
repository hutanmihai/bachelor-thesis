from pydantic import BaseModel, Field


class StructuredDataSchema(BaseModel):
    # categorical
    manufacturer: str
    model: str
    fuel: str
    chassis: str
    sold_by: str
    gearbox: str

    # numerical
    km: int
    power: int
    engine: int
    year: int

    # description
    description: str


class InferenceResponseSchema(BaseModel):
    prediction: float = Field(..., example=10000)
