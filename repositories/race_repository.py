import requests
from repository import Repository
from dtos import RaceDto


class RaceRepository(Repository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_races(self):
        elements = requests.get(f"{self.base_url}/api/races").json()
        return [RaceDto.from_dict(dto) for dto in elements]
