from dnd import races
from dnd.race import Race


def test_all_races():
    assert all(isinstance(race, Race) for race in races.all_races)
