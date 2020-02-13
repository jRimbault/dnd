import random

from dnd import classes
from dnd.attributes import Attributes
from dnd.hitpoints import HitPoints


def test_level_one_hitpoints():
    modifiers = Attributes.random().modifiers()
    for clss in classes.all_classes:
        assert HitPoints(modifiers.constitution + clss.hit_die) == HitPoints.random(
            [clss], modifiers
        )


def test_random_level_hitpoints():
    modifiers = Attributes.random().modifiers()
    for clss in classes.all_classes:
        clss.level = random.randint(1, 20)
        assert (
            HitPoints.min([clss], modifiers)
            <= HitPoints.random([clss], modifiers)
            <= HitPoints.max([clss], modifiers)
        )


def test_multiclassing_hitpoints():
    modifiers = Attributes.random(5, 2).modifiers()
    multi_class = [classes.paladin(level=10), classes.sorcerer(level=6)]
    min_hp = HitPoints.min(multi_class, modifiers)
    max_hp = HitPoints.max(multi_class, modifiers)
    assert min_hp <= HitPoints.random(multi_class, modifiers) <= max_hp
