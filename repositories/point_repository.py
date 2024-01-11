import requests
from abc import abstractmethod
from repositories.repository import UrlRepository
from dtos import PointDto


class IPointRepository:
    @abstractmethod
    def get_points(self):
        pass

    @abstractmethod
    def get_point_by_id(self, point_id: int):
        pass

    @abstractmethod
    def add_point(self, point: PointDto):
        pass

    @abstractmethod
    def update_point(self, point_id: int, point: PointDto):
        pass


class PointRepository(UrlRepository, IPointRepository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_points(self) -> list[PointDto]:
        elements = requests.get(f"{self.base_url}/api/points").json()
        return [PointDto.from_dict(dto) for dto in elements]

    def get_point_by_id(self, point_id: int) -> PointDto | None:
        result = requests.get(f"{self.base_url}/api/points/{point_id}")
        if result.status_code == 200:
            return PointDto.from_dict(result.json())

        return None

    def add_point(self, point: PointDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/points", json=point.to_dict())

    def update_point(self, point_id: int, point: PointDto) -> requests.Response:
        return requests.put(f"{self.base_url}/api/points/{point_id}", json=point.to_dict())
