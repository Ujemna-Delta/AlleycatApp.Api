from repositories import RaceRepository, IRaceRepository
from infrastructure import get_settings, AppSettings
from typing import Annotated
from fastapi import Depends


def get_race_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> IRaceRepository:
    return RaceRepository(app_settings.persistence_url)
