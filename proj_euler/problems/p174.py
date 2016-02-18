# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:58:00 2016

@author: mjcosta
"""

from collections import Counter

from proj_euler.utils.timing import timefunc

def sieve_tiles(limit):
    tiles = [0] * (limit+1)
    hole = 1
    while (hole + 2)**2 - hole**2 < limit:
        outer = hole + 2
        hole_area = hole**2
        while outer**2 - hole_area <= limit:
            tiles[outer**2 - hole_area] += 1
            outer += 2
        hole += 1
    return Counter(tiles)

@timefunc
def solve_p174(lower, upper, limit):
    counts = sieve_tiles(limit)
    return sum(counts[x] for x in xrange(lower, upper+1))

"""
Thoughts: Fairly straightforward question, simply sieve the number of
arrangements by varying the outer and hole dimensions. Then count the values
and return the answer. It takes ~500 ms to run, so the performance is not
bad either.
"""
if __name__ == "__main__":
    print "Example (n = 15) (expect 832):"
    print solve_p174(15, 15, 10**6)
    print "Problem (1 <= n <= 10):"
    print solve_p174(1, 10, 10**6)
