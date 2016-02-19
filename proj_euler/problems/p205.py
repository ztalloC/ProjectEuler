# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:43:04 2016

@author: mjcosta
"""

from collections import Counter
from itertools import product
from fractions import Fraction

from proj_euler.utils.timing import timefunc

@timefunc
def solve_p205():
    count6 = Counter(sum(x) for x in product(range(1, 7), repeat=6))
    count4 = Counter(sum(x) for x in product(range(1, 5), repeat=9))
    wins = sum(count6[x] * count4[y] for x in count6 for y in count4 if y > x)
    total = sum(count6.values()) * sum(count4.values())
    return Fraction(wins, total)

"""
Thoughts: Very easy question. One can just count the values for each player
and compute the number of winning and total possibilities. With counters and
itertools, it takes very little code to solve and finishes in ~100 ms.
"""
if __name__ == "__main__":
    print "%.7f" % float(solve_p205())