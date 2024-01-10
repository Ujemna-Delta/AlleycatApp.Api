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
