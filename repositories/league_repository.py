import requests
from abc import abstractmethod
from repositories.repository import UrlRepository
from dtos import LeagueDto, LeagueScoreDto


class ILeagueRepository:
    @abstractmethod
    def get_leagues(self):
        pass

    @abstractmethod
    def get_league_by_id(self, league_id: int):
        pass

    @abstractmethod
    def add_league(self, league: LeagueDto):
        pass

    @abstractmethod
    def update_league(self, league_id: int, league: LeagueDto):
        pass

    @abstractmethod
    def get_league_scores_by_league_id(self, league_id: int):
        pass

    @abstractmethod
    def get_league_scores_by_attendee_id(self, attendee_id: str):
        pass


class LeagueRepository(UrlRepository, ILeagueRepository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_leagues(self) -> list[LeagueDto]:
        elements = requests.get(f"{self.base_url}/api/leagues").json()
        return [LeagueDto.from_dict(dto) for dto in elements]

    def get_league_by_id(self, league_id: int) -> LeagueDto | None:
        result = requests.get(f"{self.base_url}/api/leagues/{league_id}")
        if result.status_code == 200:
            return LeagueDto.from_dict(result.json())

        return None

    def add_league(self, league: LeagueDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/leagues", json=league.to_dict())

    def update_league(self, league_id: int, league: LeagueDto) -> requests.Response:
        return requests.put(f"{self.base_url}/api/leagues/{league_id}", json=league.to_dict())

    def get_league_scores_by_league_id(self, league_id: int) -> list[LeagueScoreDto]:
        elements = requests.get(f"{self.base_url}/api/leagues/scores/league/{league_id}").json()
        return [LeagueScoreDto.from_dict(dto) for dto in elements]

    def get_league_scores_by_attendee_id(self, attendee_id: str) -> list[LeagueScoreDto]:
        elements = requests.get(f"{self.base_url}/api/leagues/scores/user/{attendee_id}").json()
        return [LeagueScoreDto.from_dict(dto) for dto in elements]
