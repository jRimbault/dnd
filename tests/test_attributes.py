from dnd.attributes import Attributes


def test_addition():
    a1 = Attributes()
    a2 = Attributes(strength=1)
    assert 1 == (a1 + a2).strength
