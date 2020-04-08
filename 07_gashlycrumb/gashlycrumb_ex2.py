#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-02
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        type=argparse.FileType('r'),
                        help="optional file",
                        default="word_frequency.txt"
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    main_dict = { }

    for line in args.file:
        words = line.split(" ")
        for word in words:
            if word[-1] in string.punctuation:
                word = word.replace(word[-1], "")
            word = word.lower().rstrip()
            if word in main_dict.keys():
                main_dict[word] += 1
            else:
                main_dict[word] = 1

    for key in main_dict.keys():
        print(f" {key}: {main_dict[key]} ")



# --------------------------------------------------
if __name__ == '__main__':
    main()
