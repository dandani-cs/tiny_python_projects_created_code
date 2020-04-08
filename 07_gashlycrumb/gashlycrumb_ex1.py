#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-02
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

    parser.add_argument('names',
                        metavar='str',
                        nargs="+",
                        help='letters searched for'
                        )

    parser.add_argument('-f',
                        '--file',
                        type=argparse.FileType('r'),
                        help="optional file",
                        default="phonebook.txt"
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    main_dict = { }

    for line in args.file:
        line = line.split(":")
        main_dict[line[0].lower()] = line[1].lower().rstrip()

    for name in args.names:
        print(main_dict[name.lower()]) if name.lower() in main_dict.keys() else print(f'I do not know "{name}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
