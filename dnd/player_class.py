from dataclasses import dataclass, field
from enum import Enum
from typing import Final, List, Optional

from .attributes import Attribute, Attributes


@dataclass
class Class:
    """Represent a player character class.

    The default instance is of a a level 1 of the given class.
    Each instance can be used to build an instance of the same player class
    but of a different level.

    Example :
    ```
    # `barbarian` is both a struct representing a level 1 barbarian and
    # a factory for making more barbarians
    barbarian = Class(
        name=ClassName.barbarian,
        hit_die=12,
        primary_ability=[Attribute.strengh],
        saves=[Attribute.strengh, Attribute.constitution],
        requirements=ClassRequirements(hard=Attributes(strengh=13)),
    )
    # `b2` is both a struct representing a level 10 barbarian and
    # a factory for making more barbarians
    b2 = barbarian(level=10)
    ```
    """

    name: "ClassName"
    hit_die: int
    primary_ability: Final[List[Attribute]] = field(repr=False)
    saves: Final[List[Attribute]] = field(repr=False)
    requirements: "ClassRequirements" = field(repr=False)
    level: int = 1

    def __call__(self, /, *, level: Optional[int] = None):
        return Class(
            name=self.name,
            hit_die=self.hit_die,
            primary_ability=self.primary_ability,
            saves=self.saves,
            requirements=self.requirements,
            level=level if level else self.level,
        )


@dataclass
class ClassRequirements:
    hard: Final[Optional[Attributes]] = None
    soft: Final[Optional[Attributes]] = None

    def possible(self, attributes: Attributes) -> bool:
        def test_soft_requirement(attribute: Attribute):
            return (
                self.soft.__dict__[attribute] != 0
                and attributes.__dict__[attribute] >= self.soft.__dict__[attribute]
            )

        hard_requirements_are_met = (
            True
            if not self.hard
            else (
                attributes.strength >= self.hard.strength
                and attributes.constitution >= self.hard.constitution
                and attributes.dexterity >= self.hard.dexterity
                and attributes.intelligence >= self.hard.intelligence
                and attributes.wisdom >= self.hard.wisdom
                and attributes.charisma >= self.hard.charisma
            )
        )
        soft_requirements_are_met = (
            True
            if not self.soft
            else (
                test_soft_requirement(Attribute.strength)
                or test_soft_requirement(Attribute.constitution)
                or test_soft_requirement(Attribute.dexterity)
                or test_soft_requirement(Attribute.intelligence)
                or test_soft_requirement(Attribute.wisdom)
                or test_soft_requirement(Attribute.charisma)
            )
        )
        return hard_requirements_are_met and soft_requirements_are_met


class ClassName(str, Enum):
    barbarian = "barbarian"
    bard = "bard"
    cleric = "cleric"
    druid = "druid"
    fighter = "fighter"
    monk = "monk"
    paladin = "paladin"
    ranger = "ranger"
    rogue = "rogue"
    sorcerer = "sorcerer"
    warlock = "warlock"
    wizard = "wizard"
