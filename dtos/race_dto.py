from datetime import datetime
from .dto import Dto


class RaceDto(Dto):
    id: int
    name: str
    description: str | None
    beginTime: datetime
    startAddress: str
    valueModifier: float
    isActive: bool
    isFreeOrder: bool
    leagueId: int | None

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
