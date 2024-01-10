from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from infrastructure import get_league_repository
from repositories import ILeagueRepository
from typing import Annotated
from dtos import LeagueDto


router = APIRouter(prefix="/api/leagues")


@router.post("/")
async def create_league(league: LeagueDto, repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):
    for r in repo.get_leagues():
        if r.name == league.name:
            raise HTTPException(status_code=409, detail="League with the specified name already exists.")

    response = repo.add_league(league)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())


@router.put("/{league_id}")
async def update_league(league_id: int, league: LeagueDto, repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):
    for r in repo.get_leagues():
        if r.name == league.name and r.id != league_id:
            raise HTTPException(status_code=409, detail="League with the specified name already exists.")

    response = repo.update_league(league_id, league)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())
