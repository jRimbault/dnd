import math
from dataclasses import dataclass, field
from typing import List, Union

from .decorators.arithmetic import arithmetic
from .player_class import Class


@dataclass(init=False)
@arithmetic
class Level:
    value: int
    proficiency: int = field(init=False)

    def __init__(self, value: Union[int, List[Class]]):
        total_level = value if isinstance(value, int) else sum(c.level for c in value)
        self.value = total_level
        self.proficiency = Level.proficiency_bonus(total_level)

    @staticmethod
    def proficiency_bonus(level: int):
        return math.floor((7 + level) / 4)
