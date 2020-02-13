import itertools
import random
from dataclasses import dataclass
from typing import Callable, List

from .attributes import Modifiers
from .decorators.arithmetic import arithmetic
from .player_class import Class


@dataclass
@arithmetic
class HitPoints:
    value: int

    @staticmethod
    def random(classes: List[Class], modifiers: Modifiers) -> "HitPoints":
        return HitPoints._calculate(
            classes, modifiers.constitution, lambda c: random.randint(2, c.hit_die)
        )

    @staticmethod
    def max(classes: List[Class], modifiers: Modifiers) -> "HitPoints":
        return HitPoints._calculate(
            classes, modifiers.constitution, lambda c: c.hit_die
        )

    @staticmethod
    def min(classes: List[Class], modifiers: Modifiers) -> "HitPoints":
        return HitPoints._calculate(classes, modifiers.constitution, lambda c: 2)

    @staticmethod
    def _calculate(
        classes: List[Class], con_modifier: int, hit_die_value: Callable[[Class], int]
    ) -> "HitPoints":
        if len(classes) == 0:
            return HitPoints(0)
        base_class, multi_class = classes[0], classes[1:]
        return HitPoints(
            sum(
                itertools.chain(
                    [base_class.hit_die, con_modifier],
                    (
                        con_modifier + hit_die_value(base_class)
                        for _ in range(base_class.level - 1)
                    ),
                    (
                        con_modifier + hit_die_value(cls)
                        for cls in multi_class
                        for _ in range(cls.level)
                    ),
                )
            )
        )
