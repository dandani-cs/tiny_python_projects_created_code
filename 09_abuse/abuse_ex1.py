#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-12
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        type = int,
                        help = "number of adjectives per sentence",
                        default = 2
                        )

    parser.add_argument("-n",
                        "--number",
                        type = int,
                        help = "number of insults to be generated",
                        default = 3
                        )

    parser.add_argument("-s",
                        "--seed",
                        type = int,
                        help = "selects seed of randomness",
                        default = None
                        )

    parser.add_argument("--fileadj",
                        metavar = "str",
                        help = "optional file for adjectives",
                        default = ""
                        )

    parser.add_argument("--filenn",
                        metavar = "str",
                        help = "optional file for nouns",
                        default = ""
                        )

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.fileadj):
        adjectives = open(args.fileadj).read().strip().split()
    else:
        adjectives = """
        bankrupt base caterwauling corrupt cullionly detestable dishonest false
        filthsome filthy foolish foul gross heedless indistinguishable infected
        insatiate irksome lascivious lecherous loathsome lubbery old peevish
        rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
        thin-faced toad-spotted unmannered vile wall-eyed
        """.strip().split()


    if os.path.isfile(args.filenn):
        adjectives = open(args.filenn).read().strip().split()
    else:
        nouns = """
        Judas Satan ape ass barbermonger beggar block boy braggart butt
        carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
        gull harpy jack jolthead knave liar lunatic maw milksop minion
        ratcatcher recreant rogue scold slave swine traitor varlet villain worm
        """.strip().split()

    random.seed(args.seed)
    for n in range(args.number):
        print(f"You {', '.join(random.sample(adjectives, args.adjectives))} {random.choice(nouns)}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
