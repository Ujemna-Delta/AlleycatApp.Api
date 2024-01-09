from datetime import datetime
from .dto import Dto


class RaceDto(Dto):
    id: int
    name: str
    description: str | None
    begin_time: datetime
    start_address: str
    value_modifier: float
    is_active: bool
    is_free_order: bool
    league_id: int | None

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'RaceDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.name = dictionary['name']
        obj.description = dictionary['description']
        obj.begin_time = dictionary['beginTime']
        obj.start_address = dictionary['startAddress']
        obj.value_modifier = dictionary['valueModifier']
        obj.is_active = dictionary['isActive']
        obj.is_free_order = dictionary['isFreeOrder']
        obj.league_id = dictionary['leagueId']

        return obj
