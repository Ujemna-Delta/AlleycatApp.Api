import requests
from abc import abstractmethod
from repositories.repository import UrlRepository
from dtos import LeagueDto


class ILeagueRepository:
    @abstractmethod
    def get_leagues(self):
        pass

    @abstractmethod
    def add_league(self, league: LeagueDto):
        pass

    @abstractmethod
    def update_league(self, league_id: int, league: LeagueDto):
        pass


class LeagueRepository(UrlRepository, ILeagueRepository):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_leagues(self) -> list[LeagueDto]:
        elements = requests.get(f"{self.base_url}/api/leagues").json()
        return [LeagueDto.from_dict(dto) for dto in elements]

    def add_league(self, league: LeagueDto) -> requests.Response:
        return requests.post(f"{self.base_url}/api/leagues", json=league.to_dict())

    def update_league(self, league_id: int, league: LeagueDto) -> requests.Response:
        return requests.put(f"{self.base_url}/api/leagues/{league_id}", json=league.to_dict())
