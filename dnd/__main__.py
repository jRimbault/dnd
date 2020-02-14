import argparse
from . import races
from . import classes
from .attributes import Attributes
from .character import Character


def main(args):
    attributes = None
    race = None
    player_class = None
    if args.attributes and len(args.attributes) == 6:
        attributes = Attributes(*args.attributes)
    if args.race and args.race in races.__dict__:
        race = races.__dict__[args.race]
    if args.player_class and args.player_class in classes.__dict__:
        player_class = [classes.__dict__[args.player_class]]

    print(Character.random(attributes=attributes, race=race, player_class=player_class))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--race", "-r", choices=[race.name for race in races.all_races])
    parser.add_argument(
        "--player-class", "-c", choices=[clss.name for clss in classes.all_classes]
    )
    parser.add_argument("--attributes", "-a", nargs="+", type=int)
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
