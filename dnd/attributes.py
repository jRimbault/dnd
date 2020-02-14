from dataclasses import dataclass
from enum import Enum
from .random import roll_attribute


class Attribute(Enum):
    strengh = 0
    constitution = 1
    dexterity = 2
    intelligence = 3
    wisdom = 4
    charisma = 6


@dataclass
class Attributes:
    strengh: int = 0
    constitution: int = 0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0

    def __add__(self, other):
        return Attributes(
            strengh=self.strengh + other.strengh,
            constitution=self.constitution + other.constitution,
            dexterity=self.dexterity + other.dexterity,
            intelligence=self.intelligence + other.intelligence,
            wisdom=self.wisdom + other.wisdom,
            charisma=self.charisma + other.charisma,
        )

    def modifiers(self):
        def modifier(value: int) -> int:
            return round((value - 10) / 2)

        return Modifiers(
            modifier(self.strengh),
            modifier(self.constitution),
            modifier(self.dexterity),
            modifier(self.intelligence),
            modifier(self.wisdom),
            modifier(self.charisma),
        )

    @staticmethod
    def random(dices: int = 4, skipped_dices: int = 1, dice_type: int = 6):
        return Attributes(
            *(roll_attribute(dices, skipped_dices, dice_type) for _ in range(6))
        )


class Modifiers(Attributes):
    pass
