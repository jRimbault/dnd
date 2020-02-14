import random


def roll_attribute(dices: int = 4, skipped_dices: int = 1, dice_type: int = 6) -> int:
    return sum(
        sorted(random.randint(1, dice_type) for _ in range(dices))[skipped_dices:]
    )
