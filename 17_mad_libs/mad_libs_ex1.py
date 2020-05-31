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
import pprint


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

   return parser.parse_args()




# --------------------------------------------------
def main():
   """Make a jazz noise here"""

   args = get_args()
   text = args.FILE.read()

   matches = re.findall('(</?([^<>/]+)[ /]?>)', text)

   if not matches:
       print(f"\"{args.FILE.name}\" has no tags.", file=sys.stderr)
       sys.exit(1)

   else:
       for match in matches:
           print(match[1])



# --------------------------------------------------
if __name__ == '__main__':
   main()
