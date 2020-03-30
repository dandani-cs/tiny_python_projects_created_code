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
                        nargs="*",
                        help='Input files (default: stdin)',
                        default=sys.stdin
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines = 0
    total_characters = 0
    total_words = 0


    for file in args.file:
        current_file = open(file, 'r')
        current_lines = 0
        current_words = 0
        current_characters = 0
        for line in current_file:
            current_lines++;
            current_characters += len(line)
            current_words = len(line.split(" "))
            print(f"{current_lines:8} {current_words:8} {current_characters:8} {file}")
        total_lines += current_lines
        total_characters += current_characters
        total_words += current_words

    print(f"{total_lines:8} {total_words:8} {total_characters:8} total") if len(args.file) > 1 else ""




# --------------------------------------------------
if __name__ == '__main__':
    main()
