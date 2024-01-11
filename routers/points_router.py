from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import PointDto, PointPreparationDto
from infrastructure import get_point_repository, redirect_response
from repositories import IPointRepository

router = APIRouter(prefix="/api/points")


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