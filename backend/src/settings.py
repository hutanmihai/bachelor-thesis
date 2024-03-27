from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    algorithm: str = Field(..., env="ALGORITHM")
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expire_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")

    app_host: str = Field(..., env="APP_HOST")
    app_port: str = Field(..., env="APP_PORT")

    database_url: str = Field(..., env="DATABASE_URL")


settings: AppSettings = AppSettings()
