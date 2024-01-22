from .dto import Dto


class LeagueDto(Dto):
    id: int = 0
    name: str = ""
    description: str | None = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'LeagueDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.name = dictionary['name']
        obj.description = dictionary['description']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'name': self.name, 'description': self.description}

        return obj


class LeagueScoreDto(Dto):
    id: int = 0
    score: float = 0
    attendeeId: str = ""
    leagueId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'LeagueScoreDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.score = dictionary['score']
        obj.attendeeId = dictionary['attendeeId']
        obj.leagueId = dictionary['leagueId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'score': self.score, 'attendeeId': self.attendeeId, 'leagueId': self.leagueId}

        return obj


class LeagueResultDto(Dto):
    attendeeId: str = ""
    rank: int = 0
    score: float = 0
    leagueId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'LeagueResultDto':
        obj = cls()

        obj.attendeeId = dictionary['attendeeId']
        obj.rank = dictionary['rank']
        obj.score = dictionary['score']
        obj.leagueId = dictionary['leagueId']

        return obj

    def to_dict(self) -> dict:
        obj = {'attendeeId': self.attendeeId, 'rank': self.rank, 'score': self.score, 'leagueId': self.leagueId}

        return obj
