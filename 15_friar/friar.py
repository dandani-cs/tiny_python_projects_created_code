#!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-09
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

    args.text = re.split('(\W+)', args.text)

    final = []

    for text in args.text:
        final.append(fry(text))

    print("".join(final))


# -------------------------------------------------
def fry(text):
    if re.match('[Yy]ou$', text):
        return text[0] + "'all"
    match = re.match('(.+)ing', text)
    if match and re.search('[aeiouy]', match.group(1)):
        return text[0:-1] + "'"
    return text


# --------------------------------------------------
if __name__ == '__main__':
    main()
