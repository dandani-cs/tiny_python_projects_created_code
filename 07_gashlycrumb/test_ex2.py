#!/usr/bin/env python3
"""tests for gashlycrumb.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = 'gashlycrumb_ex2.py'


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
    rv, out = getstatusoutput(f'{prg} -f {bad}')
    assert rv != 0
    expected = f"No such file or directory: '{bad}'"
    assert re.search(expected, out)


# --------------------------------------------------
def test_number_of_words():
    """Tests for counting word occurences"""

    rv, out = getstatusoutput(f"{prg}")
    assert rv == 0
    expected = ["you: 4", "time: 4", "if: 2", "will: 2", "after: 2", "you're: 1", "lost: 1", "can: 1", "look: 1", "and: 1", "find: 1", "me: 1", "fall: 1", "i: 1", "catch: 1", "i'll: 1", "be: 1", "waiting: 1"]
    for word in expected:
        assert word in out.strip()


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
