"""Script to quickly generate some classic TTRPG character's attributes"""

import argparse
import random
import textwrap
from dataclasses import dataclass
from typing import Iterator


def rolling_methods():
    """
    3d6  : roll 3 6-sided dice and add them up
    4d6  : roll 4 6-sided dice, remove the lowest
    5d6  : roll 5 6-sided dice, remove the 2 lowest
    1d20 : roll 1 20-sided die
    2d20 : roll 2 20-sided die, remove the lowest
    """
    return {
        "3d6": [3, 0, 6],
        "4d6": [4, 1, 6],
        "5d6": [5, 2, 6],
        "1d20": [1, 0, 20],
        "2d20": [2, 1, 20],
    }


METHODS = rolling_methods()


@dataclass
class Attributes:
    strengh: int = 0
    constitution: int = 0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0


def main(args):
    attributes = roll_attributes(*METHODS[args.method])
    print(Attributes(*attributes) if args.in_order else " ".join(map(str, attributes)))


def roll_attributes(dices: int, skipped_dices: int, dice_type: int) -> Iterator[int]:
    yield from (roll_attribute(dices, skipped_dices, dice_type) for _ in range(6))


def roll_attribute(dices: int, skipped_dices: int, dice_type: int) -> int:
    return sum(
        sorted(random.randint(1, dice_type) for _ in range(dices))[skipped_dices:]
    )


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter, description=__doc__.strip()
    )
    parser.add_argument(
        "method",
        choices=METHODS.keys(),
        help=textwrap.dedent(rolling_methods.__doc__).strip(),
    )
    parser.add_argument(
        "--in-order",
        "-o",
        action="store_true",
        help="You don't get to choose which value goes where.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
