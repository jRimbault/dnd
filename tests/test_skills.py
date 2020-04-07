from dnd import classes, races
from dnd.attributes import Attributes
from dnd.character import Character
from dnd.hitpoints import HitPoints
from dnd.level import Level
from dnd.skills import Skill


def test_character_skill_roll():
    character = (
        Character.builder()
        .attributes(Attributes(16, 20, 16, 4, 8, 12))
        .race(races.goliath)
        .classes([classes.barbarian(level=12)])
        .proficiencies([Skill.athletics, Skill.intimidation, Skill.nature])
        .hitpoints(HitPoints(100))
        .build()
    )
    proficiency = Level(12).proficiency
    mod = character.modifiers
    for _ in range(100):
        assert (
            1 + mod.strength + proficiency
            <= character.roll(Skill.athletics)
            <= 20 + mod.strength + proficiency
        )
        assert 1 + mod.wisdom <= character.roll(Skill.insight) <= 20 + mod.wisdom
        assert (
            1 + mod.intelligence + proficiency
            <= character.roll(Skill.nature)
            <= 20 + mod.intelligence + proficiency
        )
