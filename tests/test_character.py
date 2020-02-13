import pytest

from dnd import classes, races
from dnd.attributes import Attributes
from dnd.character import Character
from dnd.hitpoints import HitPoints
from dnd.level import Level


def test_character_builder_designer():
    character = (
        Character.builder()
        .attributes(Attributes(13, 13, 13, 13, 13, 13))
        .race(races.human)
        .classes([classes.rogue(level=3), classes.fighter(level=7)])
        .proficiencies([])
        .hitpoints(HitPoints(100))
        .build()
    )
    with pytest.raises(AttributeError, match="object has no attribute 'build'"):
        Character.builder().build()
    assert character.attributes.strength == 14
    assert character.modifiers.strength == 2
    assert character.race == races.human
    assert character.level == Level(10)
    assert classes.rogue(level=6) not in character.classes
    assert classes.rogue(level=3) in character.classes
    assert classes.fighter(level=7) in character.classes
    assert classes.paladin(level=7) not in character.classes
    assert classes.fighter(level=6) not in character.classes


def test_level_arithmetic_decorator():
    level = Level(7)
    assert level > Level(6)
    assert level >= Level(6)
    assert level == Level(7)
    assert level != Level(8)
    assert level <= Level(8)
    assert level < Level(8)
