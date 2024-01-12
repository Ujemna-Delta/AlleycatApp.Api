import requests
from abc import abstractmethod
from repositories.repository import UrlRepository
from dtos import RaceDto, RaceAttendanceDto, RaceCompletionDto


class IRaceRepository:
    @abstractmethod
    def get_races(self):
        pass

    @abstractmethod
    def get_race_by_id(self, race_id: int):
        pass

    @abstractmethod
    def add_race(self, race: RaceDto):
        pass

    @abstractmethod
    def update_race(self, race_id: int, race: RaceDto):
        pass

    @abstractmethod
    def add_race_attendance(self, race_attendance: RaceAttendanceDto):
        pass

    @abstractmethod
    def add_race_completion(self, race_completion: RaceCompletionDto):
        pass


class RaceRepository(UrlRepository, IRaceRepository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_races(self) -> list[RaceDto]:
        elements = requests.get(f"{self.base_url}/api/races").json()
        return [RaceDto.from_dict(dto) for dto in elements]

    def get_race_by_id(self, race_id: int) -> RaceDto | None:
        result = requests.get(f"{self.base_url}/api/races/{race_id}")
        if result.status_code == 200:
            return RaceDto.from_dict(result.json())

        return None

    def add_race(self, race: RaceDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/races", json=race.to_dict())

    def update_race(self, race_id: int, race: RaceDto) -> requests.Response:
        return requests.put(f"{self.base_url}/api/races/{race_id}", json=race.to_dict())

    def add_race_attendance(self, race_attendance: RaceAttendanceDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/races/attendances", json=race_attendance.to_dict())

    def add_race_completion(self, race_completion: RaceCompletionDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/completions/races", json=race_completion.to_dict())
