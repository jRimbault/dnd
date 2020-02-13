from .attributes import Attribute, Attributes
from .player_class import Class, ClassName, ClassRequirements

barbarian = Class(
    name=ClassName.barbarian,
    hit_die=12,
    primary_ability=[Attribute.strength],
    saves=[Attribute.strength, Attribute.constitution],
    requirements=ClassRequirements(hard=Attributes(strength=13)),
)
bard = Class(
    name=ClassName.bard,
    hit_die=8,
    primary_ability=[Attribute.charisma],
    saves=[Attribute.dexterity, Attribute.charisma],
    requirements=ClassRequirements(hard=Attributes(charisma=13)),
)
cleric = Class(
    name=ClassName.cleric,
    hit_die=8,
    primary_ability=[Attribute.wisdom],
    saves=[Attribute.wisdom, Attribute.charisma],
    requirements=ClassRequirements(hard=Attributes(wisdom=13)),
)
druid = Class(
    name=ClassName.druid,
    hit_die=8,
    primary_ability=[Attribute.wisdom],
    saves=[Attribute.intelligence, Attribute.wisdom],
    requirements=ClassRequirements(hard=Attributes(wisdom=13)),
)
fighter = Class(
    name=ClassName.fighter,
    hit_die=10,
    primary_ability=[Attribute.strength],
    saves=[Attribute.strength, Attribute.constitution],
    requirements=ClassRequirements(soft=Attributes(strength=13, dexterity=13)),
)
monk = Class(
    name=ClassName.monk,
    hit_die=8,
    primary_ability=[Attribute.dexterity, Attribute.wisdom],
    saves=[Attribute.strength, Attribute.dexterity],
    requirements=ClassRequirements(hard=Attributes(dexterity=13, wisdom=13)),
)
paladin = Class(
    name=ClassName.paladin,
    hit_die=10,
    primary_ability=[Attribute.strength, Attribute.charisma],
    saves=[Attribute.wisdom, Attribute.charisma],
    requirements=ClassRequirements(hard=Attributes(strength=13, charisma=13)),
)
ranger = Class(
    name=ClassName.ranger,
    hit_die=10,
    primary_ability=[Attribute.dexterity, Attribute.wisdom],
    saves=[Attribute.strength, Attribute.dexterity],
    requirements=ClassRequirements(hard=Attributes(dexterity=13, wisdom=13)),
)
rogue = Class(
    name=ClassName.rogue,
    hit_die=8,
    primary_ability=[Attribute.dexterity],
    saves=[Attribute.dexterity, Attribute.intelligence],
    requirements=ClassRequirements(hard=Attributes(dexterity=13)),
)
sorcerer = Class(
    name=ClassName.sorcerer,
    hit_die=6,
    primary_ability=[Attribute.charisma],
    saves=[Attribute.constitution, Attribute.charisma],
    requirements=ClassRequirements(hard=Attributes(charisma=13)),
)
warlock = Class(
    name=ClassName.warlock,
    hit_die=8,
    primary_ability=[Attribute.charisma],
    saves=[Attribute.wisdom, Attribute.charisma],
    requirements=ClassRequirements(hard=Attributes(charisma=13)),
)
wizard = Class(
    name=ClassName.wizard,
    hit_die=6,
    primary_ability=[Attribute.intelligence],
    saves=[Attribute.intelligence, Attribute.wisdom],
    requirements=ClassRequirements(hard=Attributes(intelligence=13)),
)

all_classes = [v for v in locals().values() if isinstance(v, Class)]
