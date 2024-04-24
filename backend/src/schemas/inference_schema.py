from pydantic import BaseModel, Field


class InferenceSchema(BaseModel):
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

    # image
    image_url: str


class InferenceResponseSchema(BaseModel):
    prediction: float = Field(..., example=10000)
