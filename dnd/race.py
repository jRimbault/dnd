from dataclasses import dataclass, field
from enum import Enum
from typing import Final, List

from .attributes import Attributes
from .languages import Languages


class RaceName(str, Enum):
    dragonborn = "dragonborn"
    dwarf = "dwarf"
    elf = "elf"
    gnome = "gnome"
    half_elf = "half_elf"
    halfling = "halfling"
    half_orc = "half_orc"
    human = "human"
    tiefling = "tiefling"
    aarakocra = "aarakocra"
    genasi = "genasi"
    goliath = "goliath"
    aasimar = "aasimar"
    bugbear = "bugbear"
    firbolg = "firbolg"
    goblin = "goblin"
    hobgoblin = "hobgoblin"
    kenku = "kenku"
    kobold = "kobold"
    lizardfold = "lizardfold"
    orc = "orc"
    tabaxi = "tabaxi"
    triton = "triton"
    yuan_ti_pureblood = "yuan_ti_pureblood"
    feral_tiefling = "feral_tiefling"
    tortle = "tortle"
    changeling = "changeling"
    kalashtar = "kalashtar"
    eberron_orc = "eberron_orc"
    shifter = "shifter"
    warforged = "warforged"
    gith = "gith"
    centaur = "centaur"
    loxodon = "loxodon"
    minotaur = "minotaur"
    simic_hybrid = "simic_hybrid"
    vedalken = "vedalken"


@dataclass
class Race:
    name: Final[RaceName] = field()
    bonuses: Final[Attributes] = field(repr=False)
    languages: Final[List[Languages]] = field(repr=False)
