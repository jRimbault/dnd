import typing
from dataclasses import dataclass
from .attributes import Attribute


@dataclass
class PlayerClass:
    name: str
    hit_die: int
    primary_ability: typing.List[Attribute]
    saves: typing.List[Attribute]
    level: int = 1
