#!/usr/bin/env python3
"""tests for howler.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = '.\\howler_ex1.py'


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


# ---------------------------------------------------
def test_file_lowercase():
    """Tests the lowercase option on files"""

    for expected_file in os.listdir('..\\input_test'):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join('true_test_outs', basename)
            out = getoutput(f'{prg} {out_flag()} {out_file} {in_file} -e')
            assert out.strip() == ''
            produced = open(out_file).read().rstrip()
            expected = open(os.path.join('..\\input_test',
                                         expected_file)).read().rstrip()
            assert expected == produced
        finally:
            # if os.path.isfile(out_file):
            #     os.remove(out_file)
            print("done")



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


# --------------------------------------------------
def test_file():
    """Test file in/out"""

    for expected_file in os.listdir('true_test_outs'):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join('..\\input_test', basename)
            out = getoutput(f'{prg} {out_flag()} {out_file} {in_file}')
            assert out.strip() == ''
            produced = open(out_file).read().rstrip()
            expected = open(os.path.join('true_test_outs',
                                         expected_file)).read().strip()
            assert expected == produced
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)
