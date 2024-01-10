from repositories import RaceRepository, IRaceRepository
from repositories import LeagueRepository, ILeagueRepository
from infrastructure import get_settings, AppSettings
from typing import Annotated
from fastapi import Depends


def get_race_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> IRaceRepository:
    return RaceRepository(app_settings.persistence_url)


def get_league_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> ILeagueRepository:
    return LeagueRepository(app_settings.persistence_url)
