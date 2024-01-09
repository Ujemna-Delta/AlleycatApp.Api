from pydantic_settings import BaseSettings
from functools import lru_cache


class AppSettings(BaseSettings):
    persistence_url: str = "http://localhost:5067"


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
