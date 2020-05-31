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


# -------------------------------------------------
def test_alpha():
    """Test if number changes from numeric to word"""
    one = verse(1)
    assert one == "\n".join([
                             "one bottle of beer on the wall,", "one bottle of beer,",
                             "Take one down, pass it around,", "No more bottles of beer on the wall!"
    ])

    two = verse(2)
    assert two == "\n".join([
                             "two bottles of beer on the wall,", "two bottles of beer,",
                             "Take one down, pass it around,", "one bottle of beer on the wall!"
    ])



# -----------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for i in range(args.num, 0, -1):
        print(verse(i))


# -----------------------------------------------------
def verse(bottles):
    alpha = {1: "one",
             2: "two",
             3: "three",
             4: "four",
             5: "five",
             6: "six",
             7: "seven",
             8: "eight",
             9: "nine",
             10: "ten"}
    return "\n".join([f'{alpha[bottles]} bottle{"s" if bottles > 1 else ""} of beer on the wall,',
                     f'{alpha[bottles]} bottle{"s" if bottles > 1 else ""} of beer,',
                     "Take one down, pass it around,",
                     f'{alpha[bottles - 1]} bottle{"s" if bottles - 1 > 1 else ""} of beer on the wall!' if bottles - 1 > 0 else "No more bottles of beer on the wall!"
                     ])





# --------------------------------------------------
if __name__ == '__main__':
    main()
