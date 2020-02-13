import argparse
import sys

from . import classes, races
from .attributes import Attributes
from .character import Character


def main(args):
    attributes = None
    race = None
    player_class = None
    level = None
    if args.level:
        level = args.level
    if args.attributes and len(args.attributes) == 6:
        attributes = Attributes(*args.attributes)
    if args.race and args.race in races.__dict__:
        race = races.__dict__[args.race]
    if args.player_class and args.player_class in classes.__dict__:
        player_class = classes.__dict__[args.player_class]

    print(
        Character.random(
            attributes=attributes, race=race, classes=player_class, level=level
        )
    )


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--race", "-r", choices=[race.name for race in races.all_races])
    parser.add_argument(
        "--player-class", "-c", choices=[clss.name for clss in classes.all_classes]
    )
    parser.add_argument("--attributes", "-a", nargs="+", type=int)
    parser.add_argument("--level", "-l", type=int)
    return parser.parse_args(argv)


if __name__ == "__main__":
    try:
        main(parse_args(sys.argv[1:]))
    except KeyboardInterrupt:
        print()
