import math
import random
from dataclasses import dataclass
from typing import Optional, List
from .attributes import Attributes
from .classes import all_classes
from .player_class import Class
from .race import Race
from .races import all_races


class Character:
    def __init__(self, attributes: Attributes, race: Race, player_class: List[Class]):
        self.race = race
        total_level = sum(c.level for c in player_class)
        self.level = CharacterLevel(total_level, proficiency(total_level))
        self.player_class = sorted(player_class, key=lambda c: c.level, reverse=True)
        self.attributes = attributes + race.bonuses
        self.modifiers = self.attributes.modifiers()

    def __repr__(self):
        return "\n".join(
            [
                str(self.race),
                str(self.level),
                *[str(c) for c in self.player_class],
                str(self.attributes),
                str(self.modifiers),
            ]
        )

    @staticmethod
    def random(
        attributes: Optional[Attributes] = None,
        race: Optional[Race] = None,
        player_class: Optional[List[Class]] = None,
    ):
        attributes = attributes if attributes else Attributes.random()
        possible_classes = list(
            filter(lambda c: c.requirements.possible(attributes), all_classes)
        )
        return Character(
            attributes,
            race if race else random.choice(all_races),
            player_class
            if player_class
            else random.sample(
                possible_classes, random.randint(1, min(len(possible_classes), 3))
            ),
        )


@dataclass
class CharacterLevel:
    level: int
    proficiency: int


def proficiency(level: int):
    return math.floor((7 + level) / 4)
