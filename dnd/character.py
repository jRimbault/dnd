import random
from .attributes import Attributes
from .classes import all_classes
from .player_class import PlayerClass
from .race import Race
from .races import all_races


class Character:
    def __init__(self, attributes: Attributes, race: Race, player_class: PlayerClass):
        self.race = race
        self.attributes = attributes + race.modifiers
        self.player_class = player_class

    def __repr__(self):
        return "\n".join(map(str, list(self.__dict__.values())))

    @staticmethod
    def random():
        return Character(
            Attributes.random(), random.choice(all_races), random.choice(all_classes),
        )
