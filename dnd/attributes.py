import math
from dataclasses import dataclass
from enum import Enum
from typing import Final

from .random import roll_attribute


class Attribute(str, Enum):
    strength = "strength"
    constitution = "constitution"
    dexterity = "dexterity"
    intelligence = "intelligence"
    wisdom = "wisdom"
    charisma = "charisma"


@dataclass
class BaseAttributes:
    strength: Final[int] = 0
    constitution: Final[int] = 0
    dexterity: Final[int] = 0
    intelligence: Final[int] = 0
    wisdom: Final[int] = 0
    charisma: Final[int] = 0


class Modifiers(BaseAttributes):
    pass


class Attributes(BaseAttributes):
    def __add__(self, other: "Attributes") -> "Attributes":
        return Attributes(
            strength=self.strength + other.strength,
            constitution=self.constitution + other.constitution,
            dexterity=self.dexterity + other.dexterity,
            intelligence=self.intelligence + other.intelligence,
            wisdom=self.wisdom + other.wisdom,
            charisma=self.charisma + other.charisma,
        )

    def modifiers(self) -> Modifiers:
        def modifier(value: int) -> int:
            return math.floor((value - 10) / 2)

        return Modifiers(
            modifier(self.strength),
            modifier(self.constitution),
            modifier(self.dexterity),
            modifier(self.intelligence),
            modifier(self.wisdom),
            modifier(self.charisma),
        )

    @staticmethod
    def random(
        dices: int = 4, skipped_dices: int = 1, dice_type: int = 6
    ) -> "Attributes":
        return Attributes(
            *(roll_attribute(dices, skipped_dices, dice_type) for _ in range(6))
        )
