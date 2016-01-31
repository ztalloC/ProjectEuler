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
    
@timefunc
def exp_pairs(limit):
    matches = defaultdict(set)
    m = 0
    fx = lambda m, n: n*n + 2*m*n
    fy = lambda m, n: m*m - n*n
    while fx(m, 0) + fy(m, 0) < limit:
        # if y > 0 then n < m.
        for n in xrange(m):
            x, y = fx(m, n), fy(m, n)
            if m == 7 and n == 6:
                print x, y, "???"
            if y < x:
                k = 1
                while k*(x+y) < limit:
                    matches[y*k].add(x*k)
                    k += 1
        m += 1
    return matches
                
            
        
if __name__ == "__main__":
    precompute_pairs(120000)