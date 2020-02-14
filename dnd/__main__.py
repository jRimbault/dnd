from .attributes import Attributes
from .character import Character
from . import races


character = Character(Attributes.random(), races.elf)

print(character)
