# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:13:22 2016

@author: mjcosta
"""

from collections import defaultdict

from proj_euler.utils.timing import timefunc
from proj_euler.utils.memoize import memoize
from proj_euler.utils.exponent import perfect_square

@memoize
def is_square(x):
    return perfect_square(x)

@timefunc
def precompute_pairs(limit):
    matches = defaultdict(set)
    squares = dict((x, x*x) for x in xrange(1, limit))
    svalues = set(squares.values())
    for x in xrange(1, limit):
        for y in xrange(1, min(x, limit - x + 1)):
            v = squares[x] + squares[y] + x * y
            if v in svalues:
                matches[y].add(x)
    return matches
    
if __name__ == "__main__":
    precompute_pairs(120000)