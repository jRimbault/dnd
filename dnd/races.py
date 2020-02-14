from .attributes import Attributes
from .languages import Languages
from .race import Race

dragonborn = Race(
    Attributes(strengh=2, charisma=1), [Languages.common, Languages.draconic]
)
dwarf = Race(Attributes(constitution=2), [Languages.common, Languages.dwarvish])
elf = Race(Attributes(dexterity=2), [Languages.common, Languages.elvish])
gnome = Race(Attributes(intelligence=2), [Languages.common, Languages.gnomish])
half_elf = Race(Attributes(charisma=2), [Languages.common, Languages.elvish])
halfling = Race(Attributes(dexterity=2), [Languages.common, Languages.halfling])
half_orc = Race(Attributes(strengh=2), [Languages.common, Languages.orc])
human = Race(Attributes(1, 1, 1, 1, 1, 1), [Languages.common])
tiefling = Race(
    Attributes(charisma=2, intelligence=1), [Languages.common, Languages.infernal]
)
aarakocra = Race(Attributes(dexterity=2, wisdom=1), [Languages.common])
genasi = Race(Attributes(constitution=2), [Languages.common])
goliath = Race(Attributes(strengh=2, constitution=1), [Languages.common])
aasimar = Race(Attributes(charisma=2), [Languages.common])
bugbear = Race(Attributes(strengh=2, dexterity=1), [Languages.common])
firbolg = Race(Attributes(wisdom=2, strengh=1), [Languages.common])
goblin = Race(Attributes(dexterity=2, constitution=1), [Languages.common])
hobgoblin = Race(Attributes(intelligence=1, constitution=2), [Languages.common])
kenku = Race(Attributes(dexterity=2, wisdom=1), [Languages.common])
kobold = Race(Attributes(dexterity=2, strengh=-2), [Languages.common])
lizardfold = Race(Attributes(constitution=2, wisdom=1), [Languages.common])
orc = Race(Attributes(strengh=2, constitution=1, intelligence=-2), [Languages.common])
tabaxi = Race(Attributes(dexterity=2, charisma=1), [Languages.common])
triton = Race(Attributes(strengh=1, constitution=1, charisma=1), [Languages.common])
yuan_ti_pureblood = Race(Attributes(charisma=2, intelligence=1), [Languages.common])
feral_tiefling = Race(Attributes(dexterity=2, intelligence=1), [Languages.common])
tortle = Race(Attributes(strengh=2, wisdom=1), [Languages.common])
changeling = Race(Attributes(charisma=2), [Languages.common])
kalashtar = Race(Attributes(wisdom=2, charisma=1), [Languages.common])
eberron_orc = Race(Attributes(strengh=2, constitution=1), [Languages.common])
shifter = Race(Attributes(), [Languages.common])
warforged = Race(Attributes(constitution=2), [Languages.common])
gith = Race(Attributes(intelligence=1), [Languages.common])
centaur = Race(Attributes(strengh=2, wisdom=1), [Languages.common])
loxodon = Race(Attributes(constitution=2, wisdom=1), [Languages.common])
minotaur = Race(Attributes(strengh=2, constitution=1), [Languages.common])
simic_hybrid = Race(Attributes(constitution=2), [Languages.common])
vedalken = Race(Attributes(intelligence=2, wisdom=1), [Languages.common])

_locals = locals()
all_races = [v for k, v in _locals.items() if k != "_" and k[0] != k[0].upper()]
