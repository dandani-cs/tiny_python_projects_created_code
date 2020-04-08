#!/usr/bin/env python3
"""tests for gashlycrumb.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = 'gashlycrumb_ex1.py'


# --------------------------------------------------
def file_flag():
    """Either -f or --file"""

    return '-f' if random.randint(0, 1) else '--file'


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
def test_bad_file():
    """Test for bad --file"""

    bad = random_string()
    letter = random.choice(string.ascii_lowercase)
    rv, out = getstatusoutput(f'{prg} {letter} -f {bad}')
    assert rv != 0
    expected = f"No such file or directory: '{bad}'"
    assert re.search(expected, out)


# --------------------------------------------------
def test_percy():
    """Tests for calling 1 valid name"""
    rv, out = getstatusoutput(f'{prg} "percy jackson"')
    assert rv == 0
    expected = "percyjackson@gmail.com"
    assert out.strip() == expected


# -------------------------------------------------
def test_multiple_names():
    """Tests multiple names"""

    rv, out = getstatusoutput(f'{prg} "annabeth chase" "hermoine granger"')
    assert rv == 0
    expected = "09887687543\nhgweasley@ministry.com"
    assert out.strip() == expected


# --------------------------------------------------
def test_bad_letter():
    """Test for bad input"""

    rv, out = getstatusoutput(f'{prg} 5 CH')
    assert rv == 0
    expected = ('I do not know "5".\n' 'I do not know "CH".')
    assert out.strip() == expected


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
