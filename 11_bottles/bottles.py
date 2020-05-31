#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-18
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

    parser.add_argument("-n",
                        "--num",
                        help = "Number of bottles",
                        type=int,
                        default = 10)

    args = parser.parse_args()

    parser.error(f'--num "{args.num}" must be greater than 0') if args.num <= 0 else ""

    return args


# --------------------------------------------------
def test_verse():
    """Test verse function"""

    one = verse(1)
    assert one == "\n".join([
                             "1 bottle of beer on the wall,", "1 bottle of beer,",
                             "Take one down, pass it around,", "No more bottles of beer on the wall!"
    ])

    two = verse(2)
    assert two == "\n".join([
                             "2 bottles of beer on the wall,", "2 bottles of beer,",
                             "Take one down, pass it around,", "1 bottle of beer on the wall!"
    ])


# -----------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for i in range(args.num, 0, -1):
        print(verse(i))


# -----------------------------------------------------
def verse(bottles):
    return "\n".join([f'{bottles} bottle{"s" if bottles > 1 else ""} of beer on the wall,',
                     f'{bottles} bottle{"s" if bottles > 1 else ""} of beer,',
                     "Take one down, pass it around,",
                     f'{bottles - 1} bottle{"s" if bottles - 1 > 1 else ""} of beer on the wall!' if bottles - 1 > 0 else "No more bottles of beer on the wall!"
                     ])





# --------------------------------------------------
if __name__ == '__main__':
    main()
