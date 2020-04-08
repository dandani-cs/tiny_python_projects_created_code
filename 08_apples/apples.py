#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-08
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
                        help='Input for text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='a')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = open(args.text, 'r').read().rstrip() if os.path.isfile(args.text) else args.text
    for char in text:
        args.vowel = args.vowel.upper() if char.isupper() else args.vowel.lower()
        text = text.replace(char, args.vowel) if char in "aeiouAEIOU" else text

    print(text)




# --------------------------------------------------
if __name__ == '__main__':
    main()
