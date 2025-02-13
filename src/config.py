import logging
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: str = None
    hanko_api_url: str = None

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
