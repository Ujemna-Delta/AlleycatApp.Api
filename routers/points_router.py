from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import PointDto, PointPreparationDto, PointCompletionDto
from infrastructure import get_point_repository, get_race_repository, redirect_response
from repositories import IPointRepository, IRaceRepository

router = APIRouter(prefix="/api/points")
completion_router = APIRouter(prefix="/api/completions/points")


@router.post("/")
async def create_point(point: PointDto, repo: Annotated[IPointRepository, Depends(get_point_repository)]):
    for r in repo.get_points():
        if r.name == point.name:
            raise HTTPException(status_code=409, detail="Point with the specified name already exists.")

    response = repo.add_point(point)
    return redirect_response(response)


@router.put("/{point_id}")
async def update_point(point_id: int, point: PointDto,
                       repo: Annotated[IPointRepository, Depends(get_point_repository)]):
    for r in repo.get_points():
        if r.name == point.name and r.id != point_id:
            raise HTTPException(status_code=409, detail="Point with the specified name already exists.")

    response = repo.update_point(point_id, point)
    return redirect_response(response)


@router.post("/preparation")
async def prepare_point(point_to_prepare: PointPreparationDto,
                        repo: Annotated[IPointRepository, Depends(get_point_repository)]):
    point_to_update = repo.get_point_by_id(point_to_prepare.id)

    if not point_to_update:
        raise HTTPException(status_code=404, detail=f"Point with ID {point_to_prepare.id} not found.")

    point_to_update.isPrepared = True

    response = repo.update_point(point_to_update.id, point_to_update)
    return redirect_response(response)


@router.get("/remaining/{point_id}")
async def get_remaining_users_on_point(point_id: int,
                                       point_repo: Annotated[IPointRepository, Depends(get_point_repository)],
                                       race_repo: Annotated[IRaceRepository, Depends(get_race_repository)]):

    point_to_check = point_repo.get_point_by_id(point_id)

    if not point_to_check:
        raise HTTPException(status_code=404, detail=f"Point with ID {point_id} not found.")

    race_id_to_check = point_to_check.raceId

    race_attendance_to_check = race_repo.get_race_attendance_by_race_id(race_id_to_check)

    attendees = [race_attendance.attendeeId for race_attendance in race_attendance_to_check]

    race_completions = race_repo.get_race_completion_by_race_id(race_id_to_check)
    point_completions = point_repo.get_point_completion_by_point_id(point_id)

    race_finish_attendees = [race_completion.attendeeId for race_completion in race_completions]
    point_finish_attendees = [point_completion.attendeeId for point_completion in point_completions]

    remaining_attendees = [attendee for attendee in attendees
                           if attendee not in race_finish_attendees
                           and attendee not in point_finish_attendees]

    return {"remaining_attendees": remaining_attendees}


@completion_router.post("/")
async def complete_task(point_completion: PointCompletionDto,
                        repo: Annotated[IPointRepository, Depends(get_point_repository)]):

    response = repo.add_point_completion(point_completion)
    return redirect_response(response)
