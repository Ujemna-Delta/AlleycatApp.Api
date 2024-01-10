from abc import abstractmethod
from pydantic import BaseModel


class Dto(BaseModel):
    @abstractmethod
    def from_dict(self, dictionary: dict):
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
