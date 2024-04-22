from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str
    predictions: int
