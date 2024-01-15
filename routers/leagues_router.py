from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import LeagueDto, LeagueResultDto
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
async def update_league(league_id: int, league: LeagueDto,
                        repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):
    for r in repo.get_leagues():
        if r.name == league.name and r.id != league_id:
            raise HTTPException(status_code=409, detail="League with the specified name already exists.")

    response = repo.update_league(league_id, league)
    return redirect_response(response)


@router.get("/results/{league_id}")
async def get_league_results(league_id: int, repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):
    league = repo.get_league_by_id(league_id)
    if not league:
        raise HTTPException(status_code=404, detail=f"League with ID {league_id} not found.")

    league_scores = repo.get_league_scores_by_league_id(league_id)
    sorted_league_scores = sorted(league_scores, key=lambda x: x.score, reverse=True)

    league_results_list = [
        LeagueResultDto(
            attendeeId=league_score.attendeeId,
            rank=rank+1,
            score=league_score.score,
            leagueId=league_score.leagueId
        ).to_dict()
        for rank, league_score in enumerate(sorted_league_scores)
    ]

    return league_results_list


@router.get("/results/user/{attendee_id}")
async def get_league_results_by_attendee_id(attendee_id: str,
                                            repo: Annotated[ILeagueRepository, Depends(get_league_repository)]):

    league_scores = repo.get_league_scores_by_attendee_id(attendee_id)
    league_ids = [league_score.leagueId for league_score in league_scores]

    league_results_final = []
    for league_id in league_ids:
        league_scores = repo.get_league_scores_by_league_id(league_id)
        sorted_league_scores = sorted(league_scores, key=lambda x: x.score, reverse=True)

        league_results_list = [
            LeagueResultDto(
                attendeeId=league_score.attendeeId,
                rank=rank + 1,
                score=league_score.score,
                leagueId=league_score.leagueId
            ).to_dict()
            for rank, league_score in enumerate(sorted_league_scores)
            if league_score.attendeeId == attendee_id
        ]

        league_results_final.extend(league_results_list)

    return league_results_final
