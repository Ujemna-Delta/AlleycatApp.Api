from fastapi import APIRouter, Depends
from infrastructure import get_race_repository
from repositories import RaceRepository
from typing import Annotated


router = APIRouter(prefix="/api/races")


@router.get("/")
async def get_races(repo: Annotated[RaceRepository, Depends(get_race_repository)]):
    return repo.get_races()
