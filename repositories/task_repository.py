import requests
from abc import abstractmethod
from repositories.repository import UrlRepository
from dtos import TaskDto


class ITaskRepository:
    @abstractmethod
    def get_tasks(self):
        pass

    @abstractmethod
    def add_task(self, task: TaskDto):
        pass

    @abstractmethod
    def update_task(self, task_id: int, task: TaskDto):
        pass


class TaskRepository(UrlRepository, ITaskRepository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_tasks(self) -> list[TaskDto]:
        elements = requests.get(f"{self.base_url}/api/tasks").json()
        return [TaskDto.from_dict(dto) for dto in elements]

    def add_task(self, task: TaskDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/tasks", json=task.to_dict())

    def update_task(self, task_id: int, task: TaskDto) -> requests.Response:
        return requests.put(f"{self.base_url}/api/tasks/{task_id}", json=task.to_dict())
