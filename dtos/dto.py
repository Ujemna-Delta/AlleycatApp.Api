from abc import abstractmethod


class Dto:
    @abstractmethod
    def from_dict(self, dictionary: dict):
        pass
