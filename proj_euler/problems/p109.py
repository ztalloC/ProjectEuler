# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:22:02 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

@timefunc
def solve_p109(limit = None):
    # Get all the moves 1-20 (inclusive) (mark non-doubles)
    moves = [x for x in range(1, 21)]
    # Multiply by two and three
    moves += [2*x for x in moves] + [3*x for x in moves]
    # Add the bullseye
    moves += [25, 50]
    # Create doubles list
    doubles = [2*x for x in range(1, 21)] + [50]
    count = 0
    # Count hitting twice then a double, note that for the first two hits
    # that (a, b) is considered by the problem to be equal to (b, a).
    for i in range(len(moves)):
        for b in moves[i:]:
            for c in doubles:
                if limit is None or moves[i] + b + c < limit:
                    count += 1        
    # Hit once then a double
    for a in moves:
        for b in doubles:
            if limit is None or a + b < limit:
                count += 1
    # Only a double
    count += sum(1 for x in doubles if limit is None or x < limit)
    return count

"""
Thoughts: Very easy problem. My first thought was to do a coin collector's
problem setup (i.e. where you count combinations to make change). However,
the size is small enough that you can just iterate through all possibilities.
For some reason, the problem has a medium difficulty rating?
"""
if __name__ == "__main__":
    print "Total (should equal 42336)"
    print solve_p109()
    print "Solution (< 100)"
    print solve_p109(100)