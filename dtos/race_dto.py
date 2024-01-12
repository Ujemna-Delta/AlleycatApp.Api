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
    id: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceActivationDto':
        obj = cls()

        obj.id = dictionary['id']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id}

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
