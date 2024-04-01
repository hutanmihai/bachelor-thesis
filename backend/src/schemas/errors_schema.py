from pydantic import BaseModel


class ApiError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "<error description>",
            }
        }
