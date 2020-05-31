#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-21
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

    parser.add_argument('text',
                        metavar='str',
                        help='Input')

    parser.add_argument('-s',
                        "--seed",
                        type=int,
                        default = None)

    args = parser.parse_args()

    args.text = open(args.text).read().strip() if os.path.isfile(args.text) else args.text

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    list_text = list(args.text)
    random.seed(args.seed)

    new_text = map(lambda x: random.choice([x.lower(), x.upper()]), list_text)

    print(f'{"".join(new_text)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
