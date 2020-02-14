from .attributes import Attribute
from .player_class import PlayerClass

barbarian = PlayerClass(
    "barbarian", 12, [Attribute.strengh], [Attribute.strengh, Attribute.constitution]
)
bard = PlayerClass(
    "bard", 8, [Attribute.charisma], [Attribute.dexterity, Attribute.charisma]
)
cleric = PlayerClass(
    "cleric", 8, [Attribute.wisdom], [Attribute.wisdom, Attribute.charisma]
)
druid = PlayerClass(
    "druid", 8, [Attribute.wisdom], [Attribute.intelligence, Attribute.wisdom]
)
fighter = PlayerClass(
    "fighter", 10, [Attribute.strengh], [Attribute.strengh, Attribute.constitution]
)
monk = PlayerClass(
    "monk",
    8,
    [Attribute.dexterity, Attribute.wisdom],
    [Attribute.strengh, Attribute.dexterity],
)
paladin = PlayerClass(
    "paladin",
    10,
    [Attribute.strengh, Attribute.charisma],
    [Attribute.wisdom, Attribute.charisma],
)
ranger = PlayerClass(
    "ranger",
    10,
    [Attribute.dexterity, Attribute.wisdom],
    [Attribute.strengh, Attribute.dexterity],
)
rogue = PlayerClass(
    "rogue", 8, [Attribute.dexterity], [Attribute.dexterity, Attribute.intelligence]
)
sorcerer = PlayerClass(
    "sorcerer", 6, [Attribute.charisma], [Attribute.constitution, Attribute.charisma]
)
warlock = PlayerClass(
    "warlock", 8, [Attribute.charisma], [Attribute.wisdom, Attribute.charisma]
)
wizard = PlayerClass(
    "wizard", 6, [Attribute.intelligence], [Attribute.intelligence, Attribute.wisdom]
)

_locals = locals()
all_classes = [v for k, v in _locals.items() if k != "_" and k[0] != k[0].upper()]
