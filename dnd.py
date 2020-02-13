"""
3d6  : roll 3 6-sided dice and add them up
4d6  : roll 4 6-sided dice, remove the lowest
5d6  : roll 5 6-sided dice, remove the 2 lowest
1d20 : roll 1 20-sided die
2d20 : roll 2 20-sided die, remove the lowest
"""
import argparse
import random
from typing import Iterator


METHODS = {
    "3d6": [3, 0, 6],
    "4d6": [4, 1, 6],
    "5d6": [5, 2, 6],
    "1d20": [1, 0, 20],
    "2d20": [2, 1, 20],
}

ATTRIBUTES = [
    "Strength",
    "Constitution",
    "Dexterity",
    "Intelligence",
    "Wisdom",
    "Charisma",
]


def main(args):
    attributes = roll_attributes(*METHODS[args.method])
    print(
        *(f"{name:<12} -> {value:>2}" for name, value in zip(ATTRIBUTES, attributes))
        if args.in_order
        else map(str, attributes),
        sep="\n",
    )


def roll_attributes(dices: int, skipped_dices: int, dice_type: int) -> Iterator[int]:
    yield from (roll_attribute(dices, skipped_dices, dice_type) for _ in range(6))


def roll_attribute(dices: int, skipped_dices: int, dice_type: int) -> int:
    return sum(
        sorted(random.randint(1, dice_type) for _ in range(dices))[skipped_dices:]
    )


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("method", choices=METHODS.keys(), help=__doc__[1:])
    parser.add_argument(
        "--in-order",
        "-o",
        action="store_true",
        help="You don't get to choose which value goes where.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
