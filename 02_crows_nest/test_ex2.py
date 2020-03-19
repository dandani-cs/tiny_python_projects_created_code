#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = '.\\crowsnest_ex2.py'
consonant_words = [
    'brigatine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigatine -> a brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# ----------------------------------------------------
def test_match_consonant_case():
    """Brigatine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word[0].upper()}{word[1:]}')
        assert out.strip() == template.format("A",  word[0].upper() + word[1:])


# ----------------------------------------------------
def test_match_vowel_case():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word[0].upper()}{word[1:]}')
        assert out.strip() == template.format("An",  word[0].upper() + word[1:])


# ---------------------------------------------------
def test_match_vowel_upper():
    """OCTOPUS -> AN OCTOPUS"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word.upper()}")
        assert out.strip() == template.format("AN", word.upper())


# -----------------------------------------------------
def test_side_option():
    """changes larboard -> starboard"""

    for flag in ["--starboard", "-s right"]:
        for word in vowel_words:
            out = getoutput(f"{prg} {word} {flag}")
            assert out.strip() == template.format("an", word).replace("larboard", "starboard")

# -----------------------------------------------------
def test_side_quit():
    """quits if the wrong arguments were passed"""

    rv, out = getstatusoutput(f"{prg} word -s wrong")
    assert rv == 0
    assert out.strip() == "'side' argument invalid. Type -h for help. Exiting application..."
