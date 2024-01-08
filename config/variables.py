# Standard Libraries
import logging

# Third-party Libraries
from dotenv import load_dotenv
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

load_dotenv()


class Settings(BaseSettings):
    COMPOSE_PROJECT_NAME: str = Field(
        default="psychology",
        env="COMPOSE_PROJECT_NAME",
    )
    DJANGO_SETTINGS_MODULE: str = Field(
        env="DJANGO_SETTINGS_MODULE",
        default="config.settings.base",
    )
    SECRET_KEY: SecretStr | None = Field(
        default="*",
        env="SECRET_KEY",
    )
    DEBUG: bool = Field(env="DEBUG", default=True)
    DATABASE_URL: str | None = Field(
        default=None,
        env="DATABASE_URL",
    )
    SITE_NAME: str = Field(env="SITE_NAME", default="AiTuring!")
    SITE_URL: str = Field(
        env="SITE_URL",
        default="http://localhost:8000",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
    )


settings = Settings()
