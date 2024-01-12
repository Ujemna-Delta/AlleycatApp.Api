from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from dtos import TaskDto, TaskCompletionDto
from infrastructure import get_task_repository, redirect_response
from repositories import ITaskRepository

router = APIRouter(prefix="/api/tasks")
completion_router = APIRouter(prefix="/api/completions/tasks")


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


@completion_router.post("/")
async def complete_task(task_completion: TaskCompletionDto,
                        repo: Annotated[ITaskRepository, Depends(get_task_repository)]):

    response = repo.add_task_completion(task_completion)
    return redirect_response(response)
