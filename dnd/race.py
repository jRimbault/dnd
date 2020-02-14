import typing
from dataclasses import dataclass
from .attributes import Attributes
from .languages import Languages


@dataclass
class Race:
    name: str
    modifiers: Attributes
    languages: typing.List[Languages]
