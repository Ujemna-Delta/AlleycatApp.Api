from datetime import datetime
from .dto import Dto


class RaceDto(Dto):
    id: int = 0
    name: str = ""
    description: str | None = None
    beginTime: datetime = datetime(1970, 1, 1)
    startAddress: str = ""
    valueModifier: float = 0
    isActive: bool = False
    isFreeOrder: bool = False
    leagueId: int | None = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.name = dictionary['name']
        obj.description = dictionary['description']
        obj.beginTime = dictionary['beginTime']
        obj.startAddress = dictionary['startAddress']
        obj.valueModifier = dictionary['valueModifier']
        obj.isActive = dictionary['isActive']
        obj.isFreeOrder = dictionary['isFreeOrder']
        obj.leagueId = dictionary['leagueId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'name': self.name, 'description': self.description,
               'beginTime': self.beginTime.isoformat(), 'startAddress': self.startAddress,
               'valueModifier': self.valueModifier, 'isActive': self.isActive, 'isFreeOrder': self.isFreeOrder,
               'leagueId': self.leagueId}

        return obj


class RaceActivationDto(Dto):
    raceId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceActivationDto':
        obj = cls()

        obj.raceId = dictionary['raceId']

        return obj

    def to_dict(self) -> dict:
        obj = {'raceId': self.raceId}

        return obj


class RaceAttendanceDto(Dto):
    id: int = 0
    isConfirmed: bool = False
    attendeeId: str = ""
    raceId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceAttendanceDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.isConfirmed = dictionary['isConfirmed']
        obj.attendeeId = dictionary['attendeeId']
        obj.raceId = dictionary['raceId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'isConfirmed': self.isConfirmed, 'attendeeId': self.attendeeId, 'raceId': self.raceId}

        return obj


class RaceCompletionDto(Dto):
    id: int = 0
    timestamp: datetime = datetime(1970, 1, 1)
    hasWithdrawn: bool = False
    score: float = 0
    attendeeId: str = ""
    raceId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceCompletionDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.timestamp = dictionary['timestamp']
        obj.hasWithdrawn = dictionary['hasWithdrawn']
        obj.score = dictionary['score']
        obj.attendeeId = dictionary['attendeeId']
        obj.raceId = dictionary['raceId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'timestamp': self.timestamp, 'hasWithdrawn': self.hasWithdrawn, 'score': self.score,
               'attendeeId': self.attendeeId, 'raceId': self.raceId}

        return obj


class RaceResultDto(Dto):
    attendeeId: str = ""
    rank: int = 0
    score: float = 0
    raceId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceResultDto':
        obj = cls()

        obj.attendeeId = dictionary['attendeeId']
        obj.rank = dictionary['rank']
        obj.score = dictionary['score']
        obj.raceId = dictionary['raceId']

        return obj

    def to_dict(self) -> dict:
        obj = {'attendeeId': self.attendeeId, 'rank': self.rank, 'score': self.score, 'raceId': self.raceId}

        return obj


class RaceWithdrawalDto(Dto):
    attendeeId: str = ""
    raceId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceWithdrawalDto':
        obj = cls()

        obj.attendeeId = dictionary['attendeeId']
        obj.raceId = dictionary['raceId']

        return obj

    def to_dict(self) -> dict:
        obj = {'attendeeId': self.attendeeId, 'raceId': self.raceId}

        return obj
