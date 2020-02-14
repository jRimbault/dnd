from dnd.attributes import Attributes
from dnd import classes


def test_simple_hard_requirements():
    attributes = Attributes()
    clss = classes.barbarian
    assert False == clss.requirements.possible(attributes)
    attributes.strengh = 13
    assert True == clss.requirements.possible(attributes)


def test_soft_requirements():
    attributes = Attributes()
    fighter = classes.fighter
    attributes.strengh = 13
    assert True == fighter.requirements.possible(attributes)
    attributes.strengh = 0
    assert False == fighter.requirements.possible(attributes)
    attributes.dexterity = 13
    assert True == fighter.requirements.possible(attributes)


def test_wizard_ranger():
    attributes = Attributes(12, 16, 15, 12, 14, 12)
    assert False == classes.wizard.requirements.possible(attributes)
    assert True == classes.ranger.requirements.possible(attributes)
