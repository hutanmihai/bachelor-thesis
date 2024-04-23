from pydantic import BaseModel, EmailStr, Field


class RegisterSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "test",
                "email": "test@test.com",
                "password": "test",
            }
        }


class LoginSchema(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "test@test.com",
                "password": "test",
            }
        }
