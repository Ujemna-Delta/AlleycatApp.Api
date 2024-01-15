from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import RaceDto, RaceActivationDto, RaceAttendanceDto, RaceCompletionDto, RaceResultDto
from infrastructure import get_race_repository, redirect_response
from repositories import IRaceRepository

router = APIRouter(prefix="/api/races")
completion_router = APIRouter(prefix="/api/completions/races")


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


@router.post("/activation")
async def activate_race(race_to_activate: RaceActivationDto,
                        repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    race_to_update = repo.get_race_by_id(race_to_activate.id)

    if not race_to_update:
        raise HTTPException(status_code=404, detail=f"Race with ID {race_to_activate.id} not found.")

    race_to_update.isActive = True

    response = repo.update_race(race_to_update.id, race_to_update)
    return redirect_response(response)


@router.put("/{race_id}")
async def update_race(race_id: int, race: RaceDto, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    for r in repo.get_races():
        if r.name == race.name and r.id != race_id:
            raise HTTPException(status_code=409, detail="Race with the specified name already exists.")

    response = repo.update_race(race_id, race)
    return redirect_response(response)


@router.post("/attendances")
async def create_race_attendance(race_attendance: RaceAttendanceDto,
                                 repo: Annotated[IRaceRepository, Depends(get_race_repository)]):

    response = repo.add_race_attendance(race_attendance)
    return redirect_response(response)


@router.get("/results/{race_id}")
async def get_race_results(race_id: int, repo: Annotated[IRaceRepository, Depends(get_race_repository)]):
    race = repo.get_race_by_id(race_id)
    if not race:
        raise HTTPException(status_code=404, detail=f"Race with ID {race_id} not found.")

    race_scores = repo.get_race_completion_by_race_id(race_id)
    sorted_race_scores = sorted(race_scores, key=lambda x: x.score, reverse=True)

    race_results_list = [
        RaceResultDto(
            attendeeId=race_score.attendeeId,
            rank=rank + 1,
            score=race_score.score,
            raceId=race_score.raceId
        ).to_dict()
        for rank, race_score in enumerate(sorted_race_scores)
    ]

    return race_results_list


@router.get("/results/user/{attendee_id}")
async def get_race_results_by_attendee_id(attendee_id: str,
                                          repo: Annotated[IRaceRepository, Depends(get_race_repository)]):

    race_scores = repo.get_race_completion_by_attendee_id(attendee_id)
    race_ids = [race_score.raceId for race_score in race_scores]

    race_results_final = []
    for race_id in race_ids:
        race_scores = repo.get_race_completion_by_race_id(race_id)
        sorted_race_scores = sorted(race_scores, key=lambda x: x.score, reverse=True)

        race_results_list = [
            RaceResultDto(
                attendeeId=race_score.attendeeId,
                rank=rank + 1,
                score=race_score.score,
                raceId=race_score.raceId
            ).to_dict()
            for rank, race_score in enumerate(sorted_race_scores)
            if race_score.attendeeId == attendee_id
        ]

        race_results_final.extend(race_results_list)

    return race_results_final


@completion_router.post("/")
async def complete_race(race_completion: RaceCompletionDto,
                        repo: Annotated[IRaceRepository, Depends(get_race_repository)]):

    response = repo.add_race_completion(race_completion)
    return redirect_response(response)
