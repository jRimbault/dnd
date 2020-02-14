import typing
from dataclasses import dataclass, field
from .attributes import Attribute, Attributes


@dataclass
class ClassRequirements:
    hard: typing.Optional[Attributes] = None
    soft: typing.Optional[Attributes] = None

    def possible(self, attributes: Attributes) -> bool:
        if self.hard:
            return (
                attributes.strengh >= self.hard.strengh
                and attributes.constitution >= self.hard.constitution
                and attributes.dexterity >= self.hard.dexterity
                and attributes.intelligence >= self.hard.intelligence
                and attributes.wisdom >= self.hard.wisdom
                and attributes.charisma >= self.hard.charisma
            )
        if self.soft:
            return (
                (self.soft.strengh != 0 and attributes.strengh >= self.soft.strengh)
                or (
                    self.soft.constitution != 0
                    and attributes.constitution >= self.soft.constitution
                )
                or (
                    self.soft.dexterity != 0
                    and attributes.dexterity >= self.soft.dexterity
                )
                or (
                    self.soft.intelligence != 0
                    and attributes.intelligence >= self.soft.intelligence
                )
                or (self.soft.wisdom != 0 and attributes.wisdom >= self.soft.wisdom)
                or (
                    self.soft.charisma != 0
                    and attributes.charisma >= self.soft.charisma
                )
            )
        return False


@dataclass
class PlayerClass:
    name: str
    hit_die: int
    primary_ability: typing.List[Attribute]
    saves: typing.List[Attribute]
    requirements: ClassRequirements = field(repr=False)
    level: int = 1
