#!/usr/bin/python

x = { "a": 1, "b": 2 }
y = { "c": 3, "d": 4 }

z = { **x, **y }

print( "z = %s" % z)

# l127914@pn1249300.lanl.gov:dictionaries $ python merge.py
# z = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# l127914@pn1249300.lanl.gov:dictionaries $ python --version
# Python 3.7.0

# l127914@pn1249300.lanl.gov:dictionaries $ date
# Thu Dec  6 12:45:55 MST 2018

# l127914@pn1249300.lanl.gov:dictionaries $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/dictionaries
