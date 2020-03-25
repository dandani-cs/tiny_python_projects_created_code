#!/usr/bin/env python3
"""
Author : None
Date   : 2020-03-22
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    jumper = {
              '1': '9',
              '2': '8',
              '3': '7',
              '4': '6',
              '5': '0',
              '6': '4',
              '7': '3',
              '8': '2',
              '9': '1',
              '0': '5',
    }

    for char in args.text:
        print(jumper.get(char, char), end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
