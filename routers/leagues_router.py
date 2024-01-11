from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import LeagueDto
from infrastructure import get_league_repository, redirect_response
from repositories import ILeagueRepository

router = APIRouter(prefix="/api/leagues")


@router.post("/")
async def create_league(league: LeagueDto, repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):
    for r in repo.get_leagues():
        if r.name == league.name:
            raise HTTPException(status_code=409, detail="League with the specified name already exists.")

    response = repo.add_league(league)
    return redirect_response(response)


@router.put("/{league_id}")
async def update_league(league_id: int, league: LeagueDto, repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):
    for r in repo.get_leagues():
        if r.name == league.name and r.id != league_id:
            raise HTTPException(status_code=409, detail="League with the specified name already exists.")

    response = repo.update_league(league_id, league)
    return redirect_response(response)
