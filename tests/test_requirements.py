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
    clss = classes.fighter
    attributes.strengh = 13
    assert True == clss.requirements.possible(attributes)
    attributes.strengh = 0
    assert False == clss.requirements.possible(attributes)
    attributes.dexterity = 13
    assert True == clss.requirements.possible(attributes)
