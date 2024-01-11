from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import RaceDto
from infrastructure import get_race_repository, redirect_response
from repositories import IRaceRepository

router = APIRouter(prefix="/api/races")


@router.get("/active/{race_id}", response_model=bool)
async def check_race_if_active(race_id: int, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    race = repo.get_race_by_id(race_id)
    if not race:
        raise HTTPException(status_code=404, detail=f"Race with ID {race_id} not found.")

    return race.isActive


@router.post("/")
async def create_race(race: RaceDto, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    for r in repo.get_races():
        if r.name == race.name:
            raise HTTPException(status_code=409, detail="Race with the specified name already exists.")

    response = repo.add_race(race)
    return redirect_response(response)


@router.put("/{race_id}")
async def update_race(race_id: int, race: RaceDto, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    for r in repo.get_races():
        if r.name == race.name and r.id != race_id:
            raise HTTPException(status_code=409, detail="Race with the specified name already exists.")

    response = repo.update_race(race_id, race)
    return redirect_response(response)
