from .attributes import Attributes
from .languages import Languages
from .race import Race, RaceName

dragonborn = Race(
    RaceName.dragonborn,
    Attributes(strength=2, charisma=1),
    [Languages.common, Languages.draconic],
)
dwarf = Race(
    RaceName.dwarf, Attributes(constitution=2), [Languages.common, Languages.dwarvish]
)
elf = Race(RaceName.elf, Attributes(dexterity=2), [Languages.common, Languages.elvish])
gnome = Race(
    RaceName.gnome, Attributes(intelligence=2), [Languages.common, Languages.gnomish]
)
half_elf = Race(
    RaceName.half_elf, Attributes(charisma=2), [Languages.common, Languages.elvish]
)
halfling = Race(
    RaceName.halfling, Attributes(dexterity=2), [Languages.common, Languages.halfling]
)
half_orc = Race(
    RaceName.half_orc, Attributes(strength=2), [Languages.common, Languages.orc]
)
human = Race(RaceName.human, Attributes(1, 1, 1, 1, 1, 1), [Languages.common])
tiefling = Race(
    RaceName.tiefling,
    Attributes(charisma=2, intelligence=1),
    [Languages.common, Languages.infernal],
)
aarakocra = Race(
    RaceName.aarakocra, Attributes(dexterity=2, wisdom=1), [Languages.common]
)
genasi = Race(RaceName.genasi, Attributes(constitution=2), [Languages.common])
goliath = Race(
    RaceName.goliath, Attributes(strength=2, constitution=1), [Languages.common]
)
aasimar = Race(RaceName.aasimar, Attributes(charisma=2), [Languages.common])
bugbear = Race(
    RaceName.bugbear, Attributes(strength=2, dexterity=1), [Languages.common]
)
firbolg = Race(RaceName.firbolg, Attributes(wisdom=2, strength=1), [Languages.common])
goblin = Race(
    RaceName.goblin, Attributes(dexterity=2, constitution=1), [Languages.common]
)
hobgoblin = Race(
    RaceName.hobgoblin, Attributes(intelligence=1, constitution=2), [Languages.common]
)
kenku = Race(RaceName.kenku, Attributes(dexterity=2, wisdom=1), [Languages.common])
kobold = Race(RaceName.kobold, Attributes(dexterity=2, strength=-2), [Languages.common])
lizardfold = Race(
    RaceName.lizardfold, Attributes(constitution=2, wisdom=1), [Languages.common]
)
orc = Race(
    RaceName.orc,
    Attributes(strength=2, constitution=1, intelligence=-2),
    [Languages.common],
)
tabaxi = Race(RaceName.tabaxi, Attributes(dexterity=2, charisma=1), [Languages.common])
triton = Race(
    RaceName.triton,
    Attributes(strength=1, constitution=1, charisma=1),
    [Languages.common],
)
yuan_ti_pureblood = Race(
    RaceName.yuan_ti_pureblood,
    Attributes(charisma=2, intelligence=1),
    [Languages.common],
)
feral_tiefling = Race(
    RaceName.feral_tiefling, Attributes(dexterity=2, intelligence=1), [Languages.common]
)
tortle = Race(RaceName.tortle, Attributes(strength=2, wisdom=1), [Languages.common])
changeling = Race(RaceName.changeling, Attributes(charisma=2), [Languages.common])
kalashtar = Race(
    RaceName.kalashtar, Attributes(wisdom=2, charisma=1), [Languages.common]
)
eberron_orc = Race(
    RaceName.eberron_orc, Attributes(strength=2, constitution=1), [Languages.common]
)
shifter = Race(RaceName.shifter, Attributes(), [Languages.common])
warforged = Race(RaceName.warforged, Attributes(constitution=2), [Languages.common])
gith = Race(RaceName.gith, Attributes(intelligence=1), [Languages.common])
centaur = Race(RaceName.centaur, Attributes(strength=2, wisdom=1), [Languages.common])
loxodon = Race(
    RaceName.loxodon, Attributes(constitution=2, wisdom=1), [Languages.common]
)
minotaur = Race(
    RaceName.minotaur, Attributes(strength=2, constitution=1), [Languages.common]
)
simic_hybrid = Race(
    RaceName.simic_hybrid, Attributes(constitution=2), [Languages.common]
)
vedalken = Race(
    RaceName.vedalken, Attributes(intelligence=2, wisdom=1), [Languages.common]
)

all_races = [v for v in locals().values() if isinstance(v, Race)]
