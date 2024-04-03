from typing import Any, Optional, Union

from pydantic import Field, PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # JWT
    algorithm: str = Field(..., env="ALGORITHM")
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expire_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # APP
    app_host: str = Field(..., env="APP_HOST")
    app_port: str = Field(..., env="APP_PORT")

    # STRIPE
    stripe_public_key: str = Field(..., env="STRIPE_PUBLIC_KEY")
    stripe_secret_key: str = Field(..., env="STRIPE_SECRET_KEY")
    stripe_webhook_secret: str = Field(..., env="STRIPE_WEBHOOK_SECRET")
    stripe_price_id_three: str = Field(..., env="STRIPE_PRICE_ID_THREE")
    stripe_price_id_five: str = Field(..., env="STRIPE_PRICE_ID_FIVE")
    stripe_price_id_ten: str = Field(..., env="STRIPE_PRICE_ID_TEN")
    payment_methods: str = Field(..., env="PAYMENT_METHODS")
    stripe_api_version: str = Field(..., env="STRIPE_API_VERSION")
    frontend_domain: str = Field(..., env="FRONTEND_DOMAIN")

    # DATABASE
    database_user: str = Field(..., env="DATABASE_USER")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
    database_hostname: str = Field(..., env="DATABASE_HOSTNAME")
    database_port: str = Field(..., env="DATABASE_PORT")
    database_db: Optional[str] = Field(None, env="DATABASE_DB")
    database_url: Union[Optional[PostgresDsn], Optional[str]] = None

    @field_validator("database_url", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=str(values.data.get("database_user")),
            password=str(values.data.get("database_password")),
            host=str(values.data.get("database_hostname")),
            port=int(values.data.get("database_port")),
            path=f"{str(values.data.get('database_db')) or ''}",
        )


settings: AppSettings = AppSettings()
