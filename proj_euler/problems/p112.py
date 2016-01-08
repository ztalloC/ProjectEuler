# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:20:52 2016

@author: mjcosta
"""

import numpy as np

from proj_euler.utils.timing import timefunc

# Tests if a number is neither increasing or decreasing i.e. "bouncy".
# Credit to: http://stackoverflow.com/a/4983495
def is_bouncy(n):
    cs = str(n)
    diff = np.diff([int(x) for x in cs])
    return not(all(diff <= 0) or all(diff >= 0))
    
@timefunc
def solve_p112(ratio):
    bouncy = 0
    total = 1
    # Keep going until the ratio reaches the target.
    while True:
        if is_bouncy(total):
            bouncy += 1
        # Check it here to associate it with the current value
        if float(bouncy)/total == ratio:
            break
        total += 1
    return total

"""
Thoughts: Simple problem. I only really looked up a question on stack overflow
for an elegant solution. I did this before problem 111 to get an easy
achievement.
"""
if __name__ == "__main__":
    print "Example (0.9):"
    print solve_p112(0.9)
    print "Problem (0.99)"
    print solve_p112(0.99)
    