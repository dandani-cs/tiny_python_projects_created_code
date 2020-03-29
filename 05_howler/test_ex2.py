#!/usr/bin/env python3
"""tests for howler.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = '.\\howler_ex2.py'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o or --outfile"""

    return '-o' if random.randint(0, 1) else '--outfile'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text_stdout():
    """Test STDIN/STDOUT"""

    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == 'FOO BAR BAZ'


# -------------------------------------------------
def test_text_lowercase():
    """ tests if lowercase works on text """
    out = getoutput(f'{prg} -e "FOO BAR BAZ"')
    assert out.strip() == "foo bar baz"


# --------------------------------------------------
def test_text_outfile():
    """Test STDIN/outfile"""

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        out = getoutput(f'{prg} {out_flag()} {out_file} "foo bar baz"')
        assert out.strip() == ''
        assert os.path.isfile(out_file)
        text = open(out_file).read().rstrip()
        assert text == 'FOO BAR BAZ'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# -------------------------------------------------
def test_multiple_input():
    """Tests multiple output lines"""

    out = getoutput(f'{prg} "foo bar baz" ..\\input_test\\fox.txt')
    assert out.strip() == "FOO BAR BAZ THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
