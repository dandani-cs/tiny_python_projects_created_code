#!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-03
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("word",
                        help = "String to be rhymed")

    args = parser.parse_args()

    args.word = list(open(args.word, "r").read().split()) if os.path.isfile(args.word) else [args.word]

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    start = sorted([c for c in string.ascii_lowercase if c not in 'aeiou'] + "bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr".split())

    for w in args.word:
        separated = stemmer(w.lower())
        rhyme_list = [c + separated[1] for c in start if c + separated[1] != w.lower()] if separated[1] != "" else [f'Cannot rhyme "{w}"']
        sys.stdout = open(w + ".txt", "w")
        print("\n".join(rhyme_list))

# --------------------------------------------------
def stemmer(word):
    consonants = "".join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    match = re.match(f'([{consonants}]+)?([aeiou].*)?', word)
    return (match.group(1) or '', match.group(2) or '') if match else ("", "")


# --------------------------------------------------
if __name__ == '__main__':
    main()
