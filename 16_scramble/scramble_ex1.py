#!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-15
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='File or text to be scrambled')

    parser.add_argument("-s",
                        "--seed",
                        help = "Choosing seed of randomness",
                        type = int,
                        default = None)

    args = parser.parse_args()
    random.seed(args.seed)
    args.text = open(args.text).read().strip() if os.path.isfile(args.text) else args.text\

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    final = []

    for word in re.split("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)", args.text):
        final.append(scramble(word))

    print("".join(final))



# --------------------------------------------------
def scramble(text):
    if len(text) > 3:
        mid = list(text[1:-1])
        sort(mid)
        text = text[0] + "".join(mid) + text[-1]

    return text





# --------------------------------------------------
if __name__ == '__main__':
    main()
