# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:19:41 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

from proj_euler.problems.p114 import block_combos

# Finds the minimum number of spaces for a given minimum block size where the
# number of possibilities exceeds the target.
@timefunc
def solve_p115(min_len, target):
    i = min_len
    # Store the memoization data across calls.
    mem = dict()
    sols = block_combos(min_len, i, mem)
    while sols <= target:
        i += 1
        sols = block_combos(min_len, i, mem)
    return i

"""
Thoughts: Extremely simple since I wrote the code for problem 114 with this
problem in mind. See probem 114 for details.
"""
if __name__ == "__main__":
    print "Example (m = 3) (Expect 30):"
    print solve_p115(3, 1e6)
    print "Example (m = 10) (Expect 57):"
    print solve_p115(10, 1e6)
    print "Problem (m = 50):"
    print solve_p115(50, 1e6)