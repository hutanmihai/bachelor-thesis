from pydantic import BaseModel


class TokenSchema(BaseModel):
    token: str

    class Config:
        json_schema_extra = {
            "token": "<jwt token>",
        }
