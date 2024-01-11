from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from infrastructure import get_point_repository
from repositories import IPointRepository
from typing import Annotated
from dtos import PointDto, PointPreparationDto


router = APIRouter(prefix="/api/points")


@router.post("/")
async def create_point(point: PointDto, repo: Annotated[IPointRepository, Depends(get_point_repository)]):
    for r in repo.get_points():
        if r.name == point.name:
            raise HTTPException(status_code=409, detail="Point with the specified name already exists.")

    response = repo.add_point(point)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())


@router.put("/{point_id}")
async def update_point(point_id: int, point: PointDto, repo: Annotated[IPointRepository, Depends(get_point_repository)]):
    for r in repo.get_points():
        if r.name == point.name and r.id != point_id:
            raise HTTPException(status_code=409, detail="Point with the specified name already exists.")

    response = repo.update_point(point_id, point)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())


@router.post("/preparation")
async def prepare_point(point_to_prepare: PointPreparationDto, repo: Annotated[IPointRepository, Depends(get_point_repository)]):
    existing_points = repo.get_points()
    point_to_update = next((point for point in existing_points if point.id == point_to_prepare.id), None)

    if not point_to_update:
        raise HTTPException(status_code=404, detail=f"Point with ID {point_to_prepare.id} not found.")

    point_to_update.isPrepared = True

    response = repo.update_point(point_to_update.id, point_to_update)
    content = response.json() if response.json() is not None else ""
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=response.json())
