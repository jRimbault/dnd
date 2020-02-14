import typing
from dataclasses import dataclass, field
from .attributes import Attributes
from .languages import Languages


@dataclass
class Race:
    name: str
    bonuses: Attributes = field(repr=False)
    languages: typing.List[Languages] = field(repr=False)
