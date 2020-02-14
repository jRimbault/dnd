import typing
from dataclasses import dataclass
from .attributes import Attributes
from .languages import Languages


@dataclass
class Race:
    name: str
    attributes_bonuses: Attributes
    languages: typing.List[Languages]
