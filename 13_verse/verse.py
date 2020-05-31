#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-24
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
                        help = "Optional number of days",
                        type = int,
                        default = 1)

    parser.add_argument("-o",
                        "--outfile",
                        help = "Optional text output file",
                        default = None
                        )

    args = parser.parse_args()

    sys.stdout = open(args.outfile, "w") if args.outfile != None else sys.stdout
    parser.error(f'--num "{n}" must be between 1 and 12') if args.num > 12 or args.num < 1 else ""

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for day in range(1, args.num + 1):
        verse(day)


# --------------------------------------------------
def verse(num):
    ordinal = {1: "first",
               2:"second",
               3:"third",
               4:"fourth",
               5:"fifth",
               6:"sixth",
               7:"seventh",
               8:"eighth",
               9:"ninth",
               10:"tenth",
               11:"eleventh",
               12:"twelveth"}

    days = [' partridge in a pear tree.',
            'Two turtle doves,',
            'Three french hens,',
            'Four calling birds,',
            'Five golden rings,',
            'Six geese a-laying,',
            'Seven swans a-swimming,',
            'Eight maids a-milking,',
            'Nine ladies dancing,',
            'Ten lords a-leaping,',
            'Eleven pipers piping,',
            'Twelve drummers drumming,']

    selected = days[:num]
    selected[0] = "And a" + days[0] if num > 1 else "A" + days[0]
    selected.reverse()
    final = "\n\n".join(selected)

    print(f"On the {ordinal[num]} day of Christmas,\nMy true love gave to me,")
    print(final)

# --------------------------------------------------
if __name__ == '__main__':
    main()
