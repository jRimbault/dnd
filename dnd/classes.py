from .attributes import Attribute, Attributes
from .player_class import Class, ClassRequirements

barbarian = Class(
    "barbarian",
    12,
    [Attribute.strengh],
    [Attribute.strengh, Attribute.constitution],
    ClassRequirements(hard=Attributes(strengh=13)),
)
bard = Class(
    "bard",
    8,
    [Attribute.charisma],
    [Attribute.dexterity, Attribute.charisma],
    ClassRequirements(hard=Attributes(charisma=13)),
)
cleric = Class(
    "cleric",
    8,
    [Attribute.wisdom],
    [Attribute.wisdom, Attribute.charisma],
    ClassRequirements(hard=Attributes(wisdom=13)),
)
druid = Class(
    "druid",
    8,
    [Attribute.wisdom],
    [Attribute.intelligence, Attribute.wisdom],
    ClassRequirements(hard=Attributes(wisdom=13)),
)
fighter = Class(
    "fighter",
    10,
    [Attribute.strengh],
    [Attribute.strengh, Attribute.constitution],
    ClassRequirements(soft=Attributes(strengh=13, dexterity=13)),
)
monk = Class(
    "monk",
    8,
    [Attribute.dexterity, Attribute.wisdom],
    [Attribute.strengh, Attribute.dexterity],
    ClassRequirements(hard=Attributes(dexterity=13, wisdom=13)),
)
paladin = Class(
    "paladin",
    10,
    [Attribute.strengh, Attribute.charisma],
    [Attribute.wisdom, Attribute.charisma],
    ClassRequirements(hard=Attributes(strengh=13, charisma=13)),
)
ranger = Class(
    "ranger",
    10,
    [Attribute.dexterity, Attribute.wisdom],
    [Attribute.strengh, Attribute.dexterity],
    ClassRequirements(hard=Attributes(dexterity=13, wisdom=13)),
)
rogue = Class(
    "rogue",
    8,
    [Attribute.dexterity],
    [Attribute.dexterity, Attribute.intelligence],
    ClassRequirements(hard=Attributes(dexterity=13)),
)
sorcerer = Class(
    "sorcerer",
    6,
    [Attribute.charisma],
    [Attribute.constitution, Attribute.charisma],
    ClassRequirements(hard=Attributes(charisma=13)),
)
warlock = Class(
    "warlock",
    8,
    [Attribute.charisma],
    [Attribute.wisdom, Attribute.charisma],
    ClassRequirements(hard=Attributes(charisma=13)),
)
wizard = Class(
    "wizard",
    6,
    [Attribute.intelligence],
    [Attribute.intelligence, Attribute.wisdom],
    ClassRequirements(hard=Attributes(intelligence=13)),
)

_locals = locals()
all_classes = [v for k, v in _locals.items() if k != "_" and k[0] != k[0].upper()]
