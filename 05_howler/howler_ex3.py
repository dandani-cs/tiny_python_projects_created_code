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
                        nargs = "+",
                        help='Input of text or file')

    parser.add_argument('-o',
                        '--outdir',
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



    text = ""

    for item in args.text:
        text += open(item).read().rstrip() if os.path.isfile(item) else item
        text += " "

    filename = text[:-1] + ".txt";
    path = os.path.join(os.getcwd(), args.outdir) if args.outdir else ""

    if not os.path.exists(path) and path != "":
        os.mkdir(args.outdir)

    # print(os.path.join(path, filename))
    sys.stdout = open(os.path.join(path, filename), "wt") if args.outdir else sys.stdout

    print(text.lower() if args.ee else text.upper(), end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
