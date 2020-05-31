 #!/usr/bin/env python3
"""
Author : None
Date   : 2020-05-25
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

    parser.add_argument('FILE',
                        metavar='str',
                        help="File name argument",
                        type = argparse.FileType('r'),
                        )

    parser.add_argument('-i',
                        '--inputs',
                        help = "optional inputs for placeholders",
                        nargs = "*",
                        default = [])

    return parser.parse_args()




# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.FILE.read()

    matches = re.findall('<([^<>]+)>', text)


    if not matches:
        print(f"\"{args.FILE.name}\" has no placeholders.", file=sys.stderr)
        sys.exit(1)
    else:
        input_list = [input(f"Give me {match}: ") for match in matches] if not args.inputs else args.inputs

        for i in input_list:
            text = re.sub('<([^<>]+)>', i, text, 1)

        print(text)




# --------------------------------------------------
if __name__ == '__main__':
    main()
