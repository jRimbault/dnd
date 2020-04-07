from dnd import classes, races
from dnd.player_class import Class
from dnd.race import Race


def test_all_races():
    assert all(isinstance(race, Race) for race in races.all_races)


def test_all_classes():
    assert all(isinstance(clss, Class) for clss in classes.all_classes)
