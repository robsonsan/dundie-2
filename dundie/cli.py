import argparse
from dundie.core import load


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog = "Enjoy and use with cautious."
    )
    parser.add_argument(
        'subcommand',
        type=str,
        help='This subcommand to run',
        choices=('load', 'show', 'send')
    )
    parser.add_argument(
        'filepath',
        type=str,
        help='File path to load'
    )
    args = parser.parse_args()
    globals()[args.subcommand](args.filepath)
