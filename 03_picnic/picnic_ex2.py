#!/usr/bin/env python3
"""
Author : None
Date   : 2020-03-20
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Prints out list of things to bring on the picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("item",
                        metavar="str",
                        help="item(s)",
                        nargs="+"
                        )

    parser.add_argument("-s",
                        "--sorted",
                        help="Sorts the items",
                        action="store_true"
                        )

    parser.add_argument("--off",
                        help = "Turn off Oxford Comma",
                        action = "store_false"
                        )

    parser.add_argument("--parser",
                        help = "Changes comma to specified characters",
                        metavar = "parser",
                        default = ","
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Processes the input to output the list of things needed to bring for the picnic"""

    args = get_args()
    separator = args.parser + " "
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ""

    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        bringing = separator.join(items) if args.off else separator.join(items[:-1]) + " " + items[-1]


    print("You are bringing {}.".format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
