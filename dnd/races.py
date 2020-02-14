from .attributes import Attributes
from .languages import Languages
from .race import Race

dragonborn = Race(
    "dragonborn",
    Attributes(strengh=2, charisma=1),
    [Languages.common, Languages.draconic],
)
dwarf = Race(
    "dwarf", Attributes(constitution=2), [Languages.common, Languages.dwarvish]
)
elf = Race("elf", Attributes(dexterity=2), [Languages.common, Languages.elvish])
gnome = Race("gnome", Attributes(intelligence=2), [Languages.common, Languages.gnomish])
half_elf = Race(
    "half_elf", Attributes(charisma=2), [Languages.common, Languages.elvish]
)
halfling = Race(
    "halfling", Attributes(dexterity=2), [Languages.common, Languages.halfling]
)
half_orc = Race("half_orc", Attributes(strengh=2), [Languages.common, Languages.orc])
human = Race("human", Attributes(1, 1, 1, 1, 1, 1), [Languages.common])
tiefling = Race(
    "tiefling",
    Attributes(charisma=2, intelligence=1),
    [Languages.common, Languages.infernal],
)
aarakocra = Race("aarakocra", Attributes(dexterity=2, wisdom=1), [Languages.common])
genasi = Race("genasi", Attributes(constitution=2), [Languages.common])
goliath = Race("goliath", Attributes(strengh=2, constitution=1), [Languages.common])
aasimar = Race("aasimar", Attributes(charisma=2), [Languages.common])
bugbear = Race("bugbear", Attributes(strengh=2, dexterity=1), [Languages.common])
firbolg = Race("firbolg", Attributes(wisdom=2, strengh=1), [Languages.common])
goblin = Race("goblin", Attributes(dexterity=2, constitution=1), [Languages.common])
hobgoblin = Race(
    "hobgoblin", Attributes(intelligence=1, constitution=2), [Languages.common]
)
kenku = Race("kenku", Attributes(dexterity=2, wisdom=1), [Languages.common])
kobold = Race("kobold", Attributes(dexterity=2, strengh=-2), [Languages.common])
lizardfold = Race(
    "lizardfold", Attributes(constitution=2, wisdom=1), [Languages.common]
)
orc = Race(
    "orc", Attributes(strengh=2, constitution=1, intelligence=-2), [Languages.common]
)
tabaxi = Race("tabaxi", Attributes(dexterity=2, charisma=1), [Languages.common])
triton = Race(
    "triton", Attributes(strengh=1, constitution=1, charisma=1), [Languages.common]
)
yuan_ti_pureblood = Race(
    "yuan_ti_pureblood", Attributes(charisma=2, intelligence=1), [Languages.common]
)
feral_tiefling = Race(
    "feral_tiefling", Attributes(dexterity=2, intelligence=1), [Languages.common]
)
tortle = Race("tortle", Attributes(strengh=2, wisdom=1), [Languages.common])
changeling = Race("changeling", Attributes(charisma=2), [Languages.common])
kalashtar = Race("kalashtar", Attributes(wisdom=2, charisma=1), [Languages.common])
eberron_orc = Race(
    "eberron_orc", Attributes(strengh=2, constitution=1), [Languages.common]
)
shifter = Race("shifter", Attributes(), [Languages.common])
warforged = Race("warforged", Attributes(constitution=2), [Languages.common])
gith = Race("gith", Attributes(intelligence=1), [Languages.common])
centaur = Race("centaur", Attributes(strengh=2, wisdom=1), [Languages.common])
loxodon = Race("loxodon", Attributes(constitution=2, wisdom=1), [Languages.common])
minotaur = Race("minotaur", Attributes(strengh=2, constitution=1), [Languages.common])
simic_hybrid = Race("simic_hybrid", Attributes(constitution=2), [Languages.common])
vedalken = Race("vedalken", Attributes(intelligence=2, wisdom=1), [Languages.common])

_locals = locals()
all_races = [v for k, v in _locals.items() if k != "_" and k[0] != k[0].upper()]
