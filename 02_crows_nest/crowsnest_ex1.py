#!/usr/bin/env python3
"""
Author : None
Date   : 2020-03-17
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Notifies the captain of any seen object in the sea',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Prints out the message for the Captain"""

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"
    article = article.upper() if word.isupper() else article
    article = article[0].upper() + article[1:] if word[0].isupper() else article
    print("Ahoy, Captain, {} {} off the larboard bow!".format(article, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
