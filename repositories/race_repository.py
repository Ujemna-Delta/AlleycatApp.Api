import requests
from abc import abstractmethod
from repositories.repository import UrlRepository
from dtos import RaceDto


class IRaceRepository:
    @abstractmethod
    def get_races(self):
        pass

    @abstractmethod
    def add_race(self, race: RaceDto):
        pass

    @abstractmethod
    def update_race(self, race_id: int, race: RaceDto):
        pass


class RaceRepository(UrlRepository, IRaceRepository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_races(self) -> list[RaceDto]:
        elements = requests.get(f"{self.base_url}/api/races").json()
        return [RaceDto.from_dict(dto) for dto in elements]

    def add_race(self, race: RaceDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/races", json=race.to_dict())

    def update_race(self, race_id: int, race: RaceDto) -> requests.Response:
        return requests.put(f"{self.base_url}/api/races/{race_id}", json=race.to_dict())
