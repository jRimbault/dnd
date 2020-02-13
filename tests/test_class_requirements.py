from dnd import classes
from dnd.attributes import Attributes


def test_simple_hard_requirements():
    attributes = Attributes()
    clss = classes.barbarian
    assert not clss.requirements.possible(attributes)
    attributes.strength = 13
    assert clss.requirements.possible(attributes)


def test_soft_requirements():
    attributes = Attributes()
    fighter = classes.fighter
    attributes.strength = 13
    assert fighter.requirements.possible(attributes)
    attributes.strength = 0
    assert not fighter.requirements.possible(attributes)
    attributes.dexterity = 13
    assert fighter.requirements.possible(attributes)


def test_wizard_ranger():
    attributes = Attributes(12, 16, 15, 12, 14, 12)
    assert not classes.wizard.requirements.possible(attributes)
    assert classes.ranger.requirements.possible(attributes)
