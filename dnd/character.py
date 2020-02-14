from .attributes import Attributes
from .race import Race


class Character:
    def __init__(self, attributes: Attributes, race: Race):
        self.race = race
        self.attributes = attributes + race.modifiers

    def __repr__(self):
        return "\n".join(map(str, list(self.__dict__.values())))
