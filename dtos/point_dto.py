from .dto import Dto


class PointDto(Dto):
    id: int = 0
    name: str = ""
    address: str = ""
    value: int = 0
    isPrepared: bool = False
    isHidden: bool = False
    order: int | None = None
    raceId: int | None = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'PointDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.name = dictionary['name']
        obj.address = dictionary['address']
        obj.value = dictionary['value']
        obj.isPrepared = dictionary['isPrepared']
        obj.isHidden = dictionary['isHidden']
        obj.order = dictionary['order']
        obj.raceId = dictionary['raceId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'name': self.name, 'address': self.address, 'value': self.value,
               'isPrepared': self.isPrepared, 'isHidden': self.isHidden, 'order': self.order, 'raceId': self.raceId}

        return obj
