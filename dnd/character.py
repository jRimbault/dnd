import math
import random
from dataclasses import dataclass
from typing import Optional, List
from .attributes import Attributes
from .classes import all_classes
from .player_class import PlayerClass
from .race import Race
from .races import all_races


class Character:
    def __init__(
        self, attributes: Attributes, race: Race, player_class: List[PlayerClass]
    ):
        self.race = race
        total_level = sum(c.level for c in player_class)
        self.level = CharacterLevel(total_level, proficiency_bonus(total_level))
        self.player_class = player_class
        self.attributes = attributes + race.attributes_bonuses
        self.modifiers = self.attributes.modifiers()

    def __repr__(self):
        return "\n".join(map(str, list(self.__dict__.values())))

    @staticmethod
    def random(
        attributes: Optional[Attributes] = None,
        race: Optional[Race] = None,
        player_class: Optional[List[PlayerClass]] = None,
    ):
        return Character(
            attributes if attributes else Attributes.random(),
            race if race else random.choice(all_races),
            player_class if player_class else [random.choice(all_classes)],
        )


@dataclass
class CharacterLevel:
    level: int
    profiency_bonus: int


def proficiency_bonus(level: int):
    return math.floor((7 + level) / 4)
