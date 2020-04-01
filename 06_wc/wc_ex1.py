#!/usr/bin/env python3
"""
Author : None
Date   : 2020-03-30
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

    parser.add_argument('FILE',
                        metavar='file',
                        type=argparse.FileType('r'),
                        nargs='*',
                        help='Input files (default: stdin)',
                        default=[sys.stdin]
                        )

    parser.add_argument("-l",
                        "--lines",
                        action="store_true")

    parser.add_argument("-w",
                        "--words",
                        action="store_true")

    parser.add_argument("-c",
                        "--chars",
                        action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total = {'lines': 0, 'words': 0, 'characters': 0}

    for file in args.FILE:
        current = {'lines': 0, 'words': 0, 'characters': 0}
        for line in file:
            current["lines"] += 1
            current["characters"] += len(line)
            current["words"] += len(line.split(" "))

        if args.lines or args.words or args.chars:
            print(f"{current['lines']:8}", end="") if args.lines else ""
            print(f"{current['words']:8}", end="") if args.words else ""
            print(f"{current['characters']:8}", end="") if args.chars else ""
            print(f" {file.name}")
        else:
            print(f'{current["lines"]:8}{current["words"]:8}{current["characters"]:8} {file.name}')
        total["lines"] += current["lines"]
        total["characters"] += current["characters"]
        total["words"] += current["words"]

    if len(args.FILE) > 1:
        if args.lines or args.words or args.chars:
            print(f"{total['lines']:8}", end="") if args.lines else ""
            print(f"{total['words']:8}", end="") if args.words else ""
            print(f"{total['characters']:8}", end="") if args.chars else ""
            print(f" {file.name}")
        else:
            print(f'{total["lines"]:8}{total["words"]:8}{total["characters"]:8} total') if len(args.FILE) > 1 else ""

# --------------------------------------------------
if __name__ == '__main__':
    main()