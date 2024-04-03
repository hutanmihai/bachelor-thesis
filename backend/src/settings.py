from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    algorithm: str = Field(..., env="ALGORITHM")
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expire_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")

    app_host: str = Field(..., env="APP_HOST")
    app_port: str = Field(..., env="APP_PORT")

    stripe_public_key: str = Field(..., env="STRIPE_PUBLIC_KEY")
    stripe_secret_key: str = Field(..., env="STRIPE_SECRET_KEY")
    stripe_webhook_secret: str = Field(..., env="STRIPE_WEBHOOK_SECRET")
    stripe_price_id_three: str = Field(..., env="STRIPE_PRICE_ID_THREE")
    stripe_price_id_five: str = Field(..., env="STRIPE_PRICE_ID_FIVE")
    stripe_price_id_ten: str = Field(..., env="STRIPE_PRICE_ID_TEN")
    payment_methods: str = Field(..., env="PAYMENT_METHODS")
    stripe_api_version: str = Field(..., env="STRIPE_API_VERSION")
    frontend_domain: str = Field(..., env="FRONTEND_DOMAIN")

    database_url: str = Field(..., env="DATABASE_URL")


settings: AppSettings = AppSettings()
