#!/usr/bin/env python3
"""
Author : None
Date   : 2020-03-24
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
                        help='Input of text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Optional output file',
                        metavar='str')

    parser.add_argument('-e',
                        '--ee',
                        action="store_true",
                        help="Make text lowercase"
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = open(args.text).read().rstrip() if os.path.isfile(args.text) else args.text
    sys.stdout = open(args.outfile, "wt") if args.outfile else sys.stdout
    print(text.lower() if args.ee else text.upper(), end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
