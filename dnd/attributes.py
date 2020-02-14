from dataclasses import dataclass
from .random import roll_attribute


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

    @staticmethod
    def random(dices: int = 4, skipped_dices: int = 1, dice_type: int = 6):
        return Attributes(
            *(roll_attribute(dices, skipped_dices, dice_type) for _ in range(6))
        )
