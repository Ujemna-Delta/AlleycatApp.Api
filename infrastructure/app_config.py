from pydantic_settings import BaseSettings
from functools import lru_cache


class AppSettings(BaseSettings):
    persistence_url: str = "https://localhost:7024"


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
