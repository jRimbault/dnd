from .attributes import Attributes
from .languages import Languages
from .race import Race, RaceName

dragonborn = Race(
    name=RaceName.dragonborn,
    bonuses=Attributes(strength=2, charisma=1),
    languages=[Languages.common, Languages.draconic],
)
dwarf = Race(
    name=RaceName.dwarf,
    bonuses=Attributes(constitution=2),
    languages=[Languages.common, Languages.dwarvish],
)
elf = Race(
    name=RaceName.elf,
    bonuses=Attributes(dexterity=2),
    languages=[Languages.common, Languages.elvish],
)
gnome = Race(
    name=RaceName.gnome,
    bonuses=Attributes(intelligence=2),
    languages=[Languages.common, Languages.gnomish],
)
half_elf = Race(
    name=RaceName.half_elf,
    bonuses=Attributes(charisma=2),
    languages=[Languages.common, Languages.elvish],
)
halfling = Race(
    name=RaceName.halfling,
    bonuses=Attributes(dexterity=2),
    languages=[Languages.common, Languages.halfling],
)
half_orc = Race(
    name=RaceName.half_orc,
    bonuses=Attributes(strength=2),
    languages=[Languages.common, Languages.orc],
)
human = Race(
    name=RaceName.human,
    bonuses=Attributes(1, 1, 1, 1, 1, 1),
    languages=[Languages.common],
)
tiefling = Race(
    name=RaceName.tiefling,
    bonuses=Attributes(charisma=2, intelligence=1),
    languages=[Languages.common, Languages.infernal],
)
aarakocra = Race(
    name=RaceName.aarakocra,
    bonuses=Attributes(dexterity=2, wisdom=1),
    languages=[Languages.common],
)
genasi = Race(
    name=RaceName.genasi,
    bonuses=Attributes(constitution=2),
    languages=[Languages.common],
)
goliath = Race(
    name=RaceName.goliath,
    bonuses=Attributes(strength=2, constitution=1),
    languages=[Languages.common],
)
aasimar = Race(
    name=RaceName.aasimar, bonuses=Attributes(charisma=2), languages=[Languages.common]
)
bugbear = Race(
    name=RaceName.bugbear,
    bonuses=Attributes(strength=2, dexterity=1),
    languages=[Languages.common],
)
firbolg = Race(
    name=RaceName.firbolg,
    bonuses=Attributes(wisdom=2, strength=1),
    languages=[Languages.common],
)
goblin = Race(
    name=RaceName.goblin,
    bonuses=Attributes(dexterity=2, constitution=1),
    languages=[Languages.common],
)
hobgoblin = Race(
    name=RaceName.hobgoblin,
    bonuses=Attributes(intelligence=1, constitution=2),
    languages=[Languages.common],
)
kenku = Race(
    name=RaceName.kenku,
    bonuses=Attributes(dexterity=2, wisdom=1),
    languages=[Languages.common],
)
kobold = Race(
    name=RaceName.kobold,
    bonuses=Attributes(dexterity=2, strength=-2),
    languages=[Languages.common],
)
lizardfold = Race(
    name=RaceName.lizardfold,
    bonuses=Attributes(constitution=2, wisdom=1),
    languages=[Languages.common],
)
orc = Race(
    name=RaceName.orc,
    bonuses=Attributes(strength=2, constitution=1, intelligence=-2),
    languages=[Languages.common],
)
tabaxi = Race(
    name=RaceName.tabaxi,
    bonuses=Attributes(dexterity=2, charisma=1),
    languages=[Languages.common],
)
triton = Race(
    name=RaceName.triton,
    bonuses=Attributes(strength=1, constitution=1, charisma=1),
    languages=[Languages.common],
)
yuan_ti_pureblood = Race(
    name=RaceName.yuan_ti_pureblood,
    bonuses=Attributes(charisma=2, intelligence=1),
    languages=[Languages.common],
)
feral_tiefling = Race(
    name=RaceName.feral_tiefling,
    bonuses=Attributes(dexterity=2, intelligence=1),
    languages=[Languages.common],
)
tortle = Race(
    name=RaceName.tortle,
    bonuses=Attributes(strength=2, wisdom=1),
    languages=[Languages.common],
)
changeling = Race(
    name=RaceName.changeling,
    bonuses=Attributes(charisma=2),
    languages=[Languages.common],
)
kalashtar = Race(
    name=RaceName.kalashtar,
    bonuses=Attributes(wisdom=2, charisma=1),
    languages=[Languages.common],
)
eberron_orc = Race(
    name=RaceName.eberron_orc,
    bonuses=Attributes(strength=2, constitution=1),
    languages=[Languages.common],
)
shifter = Race(
    name=RaceName.shifter, bonuses=Attributes(), languages=[Languages.common]
)
warforged = Race(
    name=RaceName.warforged,
    bonuses=Attributes(constitution=2),
    languages=[Languages.common],
)
gith = Race(
    name=RaceName.gith, bonuses=Attributes(intelligence=1), languages=[Languages.common]
)
centaur = Race(
    name=RaceName.centaur,
    bonuses=Attributes(strength=2, wisdom=1),
    languages=[Languages.common],
)
loxodon = Race(
    name=RaceName.loxodon,
    bonuses=Attributes(constitution=2, wisdom=1),
    languages=[Languages.common],
)
minotaur = Race(
    name=RaceName.minotaur,
    bonuses=Attributes(strength=2, constitution=1),
    languages=[Languages.common],
)
simic_hybrid = Race(
    name=RaceName.simic_hybrid,
    bonuses=Attributes(constitution=2),
    languages=[Languages.common],
)
vedalken = Race(
    name=RaceName.vedalken,
    bonuses=Attributes(intelligence=2, wisdom=1),
    languages=[Languages.common],
)

all_races = [v for v in locals().values() if isinstance(v, Race)]
