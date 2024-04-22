from pydantic import UUID4, BaseModel


class EntrySchema(BaseModel):
    id: UUID4
    manufacturer: str
    model: str
    fuel: str
    chassis: str
    sold_by: str
    gearbox: str
    km: int
    power: int
    engine: int
    year: int
    description: str
    prediction: int


class EntryListSchema(BaseModel):
    entries: list[EntrySchema] = []
