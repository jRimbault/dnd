import random
from typing import Optional
from .attributes import Attributes
from .classes import all_classes
from .player_class import PlayerClass
from .race import Race
from .races import all_races


class Character:
    def __init__(self, attributes: Attributes, race: Race, player_class: PlayerClass):
        self.race = race
        self.player_class = player_class
        self.attributes = attributes + race.modifiers

    def __repr__(self):
        return "\n".join(map(str, list(self.__dict__.values())))

    @staticmethod
    def random(
        attributes: Optional[Attributes] = None,
        race: Optional[Race] = None,
        player_class: Optional[PlayerClass] = None,
    ):
        return Character(
            attributes if attributes else Attributes.random(),
            race if race else random.choice(all_races),
            player_class if player_class else random.choice(all_classes),
        )
