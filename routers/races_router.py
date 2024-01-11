from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from infrastructure import get_race_repository
from repositories import IRaceRepository
from typing import Annotated
from dtos import RaceDto


router = APIRouter(prefix="/api/races")


@router.get("/active/{race_id}", response_model=bool)
async def check_race_if_active(race_id: int, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    existing_races = repo.get_races()
    race = next((element for element in existing_races if element.id == race_id), None)

    if not race:
        raise HTTPException(status_code=404, detail=f"Race with ID {race_id} not found.")

    return race.isActive


@router.post("/")
async def create_race(race: RaceDto, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    for r in repo.get_races():
        if r.name == race.name:
            raise HTTPException(status_code=409, detail="Race with the specified name already exists.")

    response = repo.add_race(race)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())


@router.put("/{race_id}")
async def update_race(race_id: int, race: RaceDto, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    for r in repo.get_races():
        if r.name == race.name and r.id != race_id:
            raise HTTPException(status_code=409, detail="Race with the specified name already exists.")

    response = repo.update_race(race_id, race)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())
