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
                        help='The object seen')

    parser.add_argument('-s',
                        '--side',
                        metavar = "side",
                        help = "side on which the object is seen",
                        default = "left"
                        )

    parser.add_argument("--starboard",
                        help = "says the object is in the right side",
                        action = "store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Prints out the message for the Captain"""

    args = get_args()
    word = args.word
    if word[0] in string.punctuation:
        print("word cannot start with punctuation. Type -h for help. Exiting application...")

    side = args.side
    if side.lower() not in ["right", "left", "starboard", "larboard"]:
        print("'side' argument invalid. Type -h for help. Exiting application...")
        sys.exit()

    article = "an" if word[0].lower() in "aeiou" else "a"
    article = article.upper() if word.isupper() else article
    article = article[0].upper() + article[1:] if word[0].isupper() else article
    side_str = "starboard" if side == "right" or side == "starboard" or args.starboard else "larboard"
    print("Ahoy, Captain, {} {} off the {} bow!".format(article, word, side_str))


# --------------------------------------------------
if __name__ == '__main__':
    main()
