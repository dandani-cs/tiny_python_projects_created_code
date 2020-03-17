#!/usr/bin/env python
"""
Author: Danielle
Purpose: Says hello to user if run with parameters, 'Hello, World!' if none.
"""

import argparse


def get_args():
    """Getting command-line arguments"""

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n", "--name", metavar="name",
                        default="World", help="Name to greet")
    return parser.parse_args()


def main():
    """Says hello to user or to the world."""
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
