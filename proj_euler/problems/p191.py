# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:38:02 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Computes the number of ternary prize strings of length n.
@timefunc
def solve_p191(n):
    prizes = dict()
    # Initialize a string of length 1. Store the tuple (length, num late,
    # num consecutive absents) as key, and the number as values.
    prizes[(1, 0, 0)] = 1   # 1 on time.
    prizes[(1, 0, 1)] = 1   # 1 late.
    prizes[(1, 1, 0)] = 1   # 1 absent.
    prizes[(1, 1, 1)] = 0
    prizes[(1, 2, 0)] = 0
    prizes[(1, 2, 1)] = 0
    # For each possibility of length i-1, consider the effect of adding one of
    # three outcomes and sum all valid possibilities.
    for i in xrange(2, n+1):
        # An on time day resets all absent streaks.
        prizes[(i, 0, 0)] = sum(prizes[(i-1, j, 0)] for j in range(3))
        # Late days reset all absent streaks (both late and not late).
        prizes[(i, 0, 1)] = sum(prizes[(i-1, j, 0)] + prizes[(i-1, j, 1)] \
            for j in range(3))
        # Absent days add to a streak.
        prizes[(i, 1, 0)] = prizes[(i-1, 0, 0)]
        prizes[(i, 2, 0)] = prizes[(i-1, 1, 0)]
        prizes[(i, 1, 1)] = prizes[(i-1, 0, 1)]
        prizes[(i, 2, 1)] = prizes[(i-1, 1, 1)]
    # Sum up all the prize strings for length n.
    return sum(prizes[(n, a, l)] for a in range(3) for l in range(2))
        
"""
Thoughts: Another relatively easy problem (I'm also currently going after the
decimator achievement). This was a straightforward dynamic programming problem
where you consider the sum of all prize strings of length n and then extend
that to the prize strings of length n+1. The exact recurrence can be seen
in the code (with comments explaining why). I could have written much less
code, but I feel that this makes it more readable, which is worthwile. The
speed is predictably < 1ms, so there is no issue there.
"""
if __name__ == "__main__":
    print "Example (length 4) (expect 43):"
    print solve_p191(4)
    print "Problem (length 30):"
    print solve_p191(30)