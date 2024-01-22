from repositories import LeagueRepository, ILeagueRepository
from repositories import PointRepository, IPointRepository
from repositories import RaceRepository, IRaceRepository
from repositories import TaskRepository, ITaskRepository
from infrastructure import get_settings, AppSettings
from typing import Annotated
from fastapi import Depends


def get_league_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> ILeagueRepository:
    return LeagueRepository(app_settings.persistence_url)


def get_point_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> IPointRepository:
    return PointRepository(app_settings.persistence_url)


def get_race_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> IRaceRepository:
    return RaceRepository(app_settings.persistence_url)


def get_task_repository(app_settings: Annotated[AppSettings, Depends(get_settings)]) -> ITaskRepository:
    return TaskRepository(app_settings.persistence_url)
