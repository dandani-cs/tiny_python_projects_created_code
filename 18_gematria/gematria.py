#!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-30
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A positional argument')

    args = parser.parse_args()

    args.text = open(args.text).read() if os.path.isfile(args.text) else args.text

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(' '.join(map(lambda x: str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', x)))), line.split())))



# --------------------------------------------------
if __name__ == '__main__':
    main()
