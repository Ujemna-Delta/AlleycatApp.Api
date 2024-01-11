from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import TaskDto
from infrastructure import get_task_repository, redirect_response
from repositories import ITaskRepository

router = APIRouter(prefix="/api/tasks")


@router.post("/")
async def create_task(task: TaskDto, repo: Annotated[ITaskRepository, Depends(get_task_repository)]):
    for r in repo.get_tasks():
        if r.name == task.name:
            raise HTTPException(status_code=409, detail="Task with the specified name already exists.")

    response = repo.add_task(task)
    return redirect_response(response)


@router.put("/{task_id}")
async def update_task(task_id: int, task: TaskDto, repo: Annotated[ITaskRepository, Depends(get_task_repository)]):
    for r in repo.get_tasks():
        if r.name == task.name and r.id != task_id:
            raise HTTPException(status_code=409, detail="Task with the specified name already exists.")

    response = repo.update_task(task_id, task)
    return redirect_response(response)
