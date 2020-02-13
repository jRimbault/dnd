import random
from dataclasses import dataclass
from typing import Final, List, Optional, cast

from .attributes import Attributes, Modifiers
from .classes import all_classes
from .hitpoints import HitPoints
from .level import Level
from .player_class import Class
from .race import Race
from .races import all_races
from .skills import Skill


@dataclass(init=False)
class Character:
    race: Final[Race]
    hitpoints: Final[HitPoints]
    level: Final[Level]
    classes: Final[List[Class]]
    attributes: Final[Attributes]
    modifiers: Final[Modifiers]
    proficiencies: List[Skill]

    def __init__(
        self,
        attributes: Attributes,
        race: Race,
        classes: List[Class],
        hitpoints: HitPoints,
        proficiencies: List[Skill],
    ):
        self.race = race
        self.hitpoints = hitpoints
        self.level = Level(classes)
        self.classes = sorted(classes, key=lambda c: c.level, reverse=True)
        self.attributes = attributes + race.bonuses
        self.modifiers = self.attributes.modifiers()
        self.proficiencies = proficiencies

    def roll(self, skill: Skill) -> int:
        proficiency = self.level.proficiency if skill in self.proficiencies else 0
        return (
            random.randint(1, 20)
            + self.modifiers.__dict__[skill.value.name]
            + proficiency
        )

    @staticmethod
    def random(
        attributes: Optional[Attributes] = None,
        race: Optional[Race] = None,
        classes: Optional[Class] = None,
        level: Optional[int] = None,
    ):
        level = level if level else random.randint(1, 20)
        race = race if race else random.choice(all_races)
        attributes = attributes if attributes else Attributes.random()
        tmp_attr = attributes + race.bonuses
        possible_classes = list(
            filter(lambda c: c.requirements.possible(tmp_attr), all_classes)
        )
        if len(possible_classes) == 0:
            raise Exception(f"No possible classes for : {tmp_attr}\nRoll again.")
        chosen_class = (classes if classes else random.choice(possible_classes))(
            level=level
        )
        return Character(
            attributes,
            race,
            [chosen_class],
            HitPoints.random([chosen_class], (race.bonuses + attributes).modifiers()),
            random.sample(list(Skill), 4),
        )

    @staticmethod
    def builder():
        """Provides a fluent interface for building a character.

        Check the coherence of the character's various attributes :
        - class(es)
        - hit points

        The `build` method will only be available once the character
        is coherent and ready to be built.

        Example :
        ```
        character = (
            Character.builder()
            .attributes(Attributes(13, 13, 13, 13, 13, 13))
            .race(races.elf)
            .classes([classes.rogue(level=3), classes.fighter(level=7)])
            .hitpoints(HitPoints(100))
            .proficiencies([])
            .build() # only available once all information has been correctly filled
        )
        ```
        """

        class CharBuilder:
            _attributes: Optional[Attributes]
            _classes: Optional[List[Class]]
            _race: Optional[Race]
            _hitpoints: Optional[HitPoints]
            _proficiencies: Optional[List[Skill]]

            def attributes(self, attributes: Attributes):
                self._attributes = attributes
                check_builder(self)
                return self

            def race(self, race: Race):
                self._race = race
                check_builder(self)
                return self

            def hitpoints(self, hitpoints: HitPoints):
                attr = Attributes()
                multi_class: List[Class] = []
                if hasattr(self, "_attributes") and self._attributes is not None:
                    attr += self._attributes
                if hasattr(self, "_race") and self._race is not None:
                    attr += self._race.bonuses
                if hasattr(self, "_classes") and self._classes is not None:
                    multi_class += self._classes
                min_hp = HitPoints.min(multi_class, attr.modifiers())
                max_hp = HitPoints.max(multi_class, attr.modifiers())
                if not min_hp.value <= hitpoints.value <= max_hp.value:
                    raise ValueError(
                        "Hitpoint value needs to be between"
                        + f" {min_hp} and {max_hp} for this combination"
                        + " of race, classes, and attributes."
                    )
                self._hitpoints = hitpoints
                check_builder(self)
                return self

            def classes(self, classes: List[Class]):
                attr = Attributes()
                if self._race:
                    attr = self._race.bonuses + attr
                if self._attributes:
                    attr = self._attributes + attr
                if any(not clss.requirements.possible(attr) for clss in classes):
                    raise ValueError(
                        "Cannot choose "
                        + ("that" if len(classes) < 2 else "those")
                        + f"classes with these {attr}"
                    )
                levels = [cls.level for cls in classes]
                if sum(levels) > 20:
                    raise ValueError(f"Total levels exceeds level 20 : {levels}")
                self._classes = classes
                check_builder(self)
                return self

            def proficiencies(self, proficiencies: List[Skill]):
                self._proficiencies = proficiencies
                check_builder(self)
                return self

        def check_builder(builder: CharBuilder):
            def check_attribute(name: str):
                return hasattr(builder, name) and builder.__dict__[name] is not None

            def build(self: CharBuilder):
                return Character(
                    attributes=cast(Attributes, self._attributes),
                    race=cast(Race, self._race),
                    classes=cast(List[Class], self._classes),
                    hitpoints=cast(HitPoints, self._hitpoints),
                    proficiencies=cast(List[Skill], self._proficiencies),
                )

            if (
                check_attribute("_attributes")
                and check_attribute("_classes")
                and check_attribute("_race")
                and check_attribute("_hitpoints")
                and check_attribute("_proficiencies")
            ):
                setattr(CharBuilder, build.__name__, build)

        return CharBuilder()
