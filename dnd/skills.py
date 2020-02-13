from enum import Enum

from .attributes import Attribute, Modifiers


class Skill(Enum):
    # Strength skills
    athletics = Attribute.strength
    # Dexterity skills
    acrobatics = Attribute.dexterity
    sleight_of_hand = Attribute.dexterity
    stealth = Attribute.dexterity
    # Intelligence skills
    arcana = Attribute.intelligence
    history = Attribute.intelligence
    investigation = Attribute.intelligence
    nature = Attribute.intelligence
    religion = Attribute.intelligence
    # Wisdom skills
    animal_handling = Attribute.wisdom
    insight = Attribute.wisdom
    medicine = Attribute.wisdom
    perception = Attribute.wisdom
    survival = Attribute.wisdom
    # Charisma skills
    deception = Attribute.charisma
    intimidation = Attribute.charisma
    performance = Attribute.charisma
    persuasion = Attribute.charisma
