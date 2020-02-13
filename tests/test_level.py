from dataclasses import dataclass

import pytest

from dnd import classes
from dnd.decorators.arithmetic import arithmetic
from dnd.level import Level


def test_proficiency_level_1_through_20():
    levels = [Level(n) for n in range(1, 21)]
    # level 1 through 4
    assert levels[0].proficiency == 2
    assert levels[1].proficiency == 2
    assert levels[2].proficiency == 2
    assert levels[3].proficiency == 2
    # level 5 through 8
    assert levels[4].proficiency == 3
    assert levels[5].proficiency == 3
    assert levels[6].proficiency == 3
    assert levels[7].proficiency == 3
    # level 9 through 12
    assert levels[8].proficiency == 4
    assert levels[9].proficiency == 4
    assert levels[10].proficiency == 4
    assert levels[11].proficiency == 4
    # level 13 through 16
    assert levels[12].proficiency == 5
    assert levels[13].proficiency == 5
    assert levels[14].proficiency == 5
    assert levels[15].proficiency == 5
    # level 17 through 20
    assert levels[16].proficiency == 6
    assert levels[17].proficiency == 6
    assert levels[18].proficiency == 6
    assert levels[19].proficiency == 6


def test_level_from_list_of_classes():
    level = Level([classes.paladin(level=8), classes.wizard(level=3)])
    assert level.proficiency == 4
    assert level.value == 11
    assert level == Level(11)


@dataclass
@arithmetic(field="__name_of_the_numeric_field__")
class T:
    __name_of_the_numeric_field__: int


def test_incompatible_types():
    with pytest.raises(TypeError, match="unsupported operand type"):
        1 + T(1)


def test_operations():
    assert 2 == T(1) + T(1)
    assert T(3) == T(3)
