from .dto import Dto


class TaskDto(Dto):
    id: int = 0
    name: str = ""
    description: str | None = None
    value: int = 0
    pointId: int | None = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'TaskDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.name = dictionary['name']
        obj.description = dictionary['description']
        obj.value = dictionary['value']
        obj.pointId = dictionary['pointId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'name': self.name, 'description': self.description, 'value': self.value,
               'pointId': self.pointId}

        return obj
