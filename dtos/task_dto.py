from datetime import datetime
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


class TaskCompletionDto(Dto):
    id: int = 0
    timestamp: datetime = datetime(1970, 1, 1)
    attendeeId: str = ""
    taskId: int = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> 'TaskCompletionDto':
        obj = cls()

        obj.id = dictionary['id']
        obj.timestamp = dictionary['timestamp']
        obj.attendeeId = dictionary['attendeeId']
        obj.taskId = dictionary['taskId']

        return obj

    def to_dict(self) -> dict:
        obj = {'id': self.id, 'timestamp': self.timestamp, 'attendeeId': self.attendeeId, 'taskId': self.taskId}

        return obj
