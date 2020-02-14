from .attributes import Attribute, Attributes
from .player_class import PlayerClass, ClassRequirements

barbarian = PlayerClass(
    "barbarian",
    12,
    [Attribute.strengh],
    [Attribute.strengh, Attribute.constitution],
    ClassRequirements(hard=Attributes(strengh=13)),
)
bard = PlayerClass(
    "bard",
    8,
    [Attribute.charisma],
    [Attribute.dexterity, Attribute.charisma],
    ClassRequirements(hard=Attributes(charisma=13)),
)
cleric = PlayerClass(
    "cleric",
    8,
    [Attribute.wisdom],
    [Attribute.wisdom, Attribute.charisma],
    ClassRequirements(hard=Attributes(wisdom=13)),
)
druid = PlayerClass(
    "druid",
    8,
    [Attribute.wisdom],
    [Attribute.intelligence, Attribute.wisdom],
    ClassRequirements(hard=Attributes(wisdom=13)),
)
fighter = PlayerClass(
    "fighter",
    10,
    [Attribute.strengh],
    [Attribute.strengh, Attribute.constitution],
    ClassRequirements(soft=Attributes(strengh=13, dexterity=13)),
)
monk = PlayerClass(
    "monk",
    8,
    [Attribute.dexterity, Attribute.wisdom],
    [Attribute.strengh, Attribute.dexterity],
    ClassRequirements(hard=Attributes(dexterity=13, wisdom=13)),
)
paladin = PlayerClass(
    "paladin",
    10,
    [Attribute.strengh, Attribute.charisma],
    [Attribute.wisdom, Attribute.charisma],
    ClassRequirements(hard=Attributes(strengh=13, charisma=13)),
)
ranger = PlayerClass(
    "ranger",
    10,
    [Attribute.dexterity, Attribute.wisdom],
    [Attribute.strengh, Attribute.dexterity],
    ClassRequirements(hard=Attributes(dexterity=13, wisdom=13)),
)
rogue = PlayerClass(
    "rogue",
    8,
    [Attribute.dexterity],
    [Attribute.dexterity, Attribute.intelligence],
    ClassRequirements(hard=Attributes(dexterity=13)),
)
sorcerer = PlayerClass(
    "sorcerer",
    6,
    [Attribute.charisma],
    [Attribute.constitution, Attribute.charisma],
    ClassRequirements(hard=Attributes(charisma=13)),
)
warlock = PlayerClass(
    "warlock",
    8,
    [Attribute.charisma],
    [Attribute.wisdom, Attribute.charisma],
    ClassRequirements(hard=Attributes(charisma=13)),
)
wizard = PlayerClass(
    "wizard",
    6,
    [Attribute.intelligence],
    [Attribute.intelligence, Attribute.wisdom],
    ClassRequirements(hard=Attributes(intelligence=13)),
)

_locals = locals()
all_classes = [v for k, v in _locals.items() if k != "_" and k[0] != k[0].upper()]
