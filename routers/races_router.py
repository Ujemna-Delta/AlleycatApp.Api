from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from infrastructure import get_race_repository
from repositories import RaceRepository
from typing import Annotated
from dtos import RaceDto


router = APIRouter(prefix="/api/races")


@router.get("/")
async def get_races(repo: Annotated[RaceRepository, Depends(get_race_repository)]):
    return repo.get_races()


@router.post("/")
async def create_race(race: RaceDto, repo: Annotated[RaceRepository, Depends(get_race_repository)]):
    for r in repo.get_races():
        if r.name == race.name:
            raise HTTPException(status_code=409, detail="Race with the specified name already exists.")

    response = repo.add_race(race)
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=response.json())

    raise HTTPException(status_code=response.status_code, detail=response.json())
