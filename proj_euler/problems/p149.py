# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:38:13 2016

@author: mjcosta
"""

import numpy

from proj_euler.utils.timing import timefunc

# Computes the largest sum of a sub sequence within the sequence "seq".
def max_sum_subsequence(seq):
    curr_max = overall_max = 0
    for x in seq:
        curr_max = max(0, curr_max + x)
        overall_max = max(overall_max, curr_max)
    return curr_max

# Generates the sequence defined in project euler 149.
def sequence(upper=4000000):
    result = []
    for k in xrange(1, 56):
        result.append((100003 - 200003*k + 300007*(k**3)) % 1000000 - 500000)
    for k in xrange(56, upper+1):
        result.append((result[k-25] + result[k-56] + 1000000) % 1000000 - 500000)
    return result
    
@timefunc
def solve_p149(data, width, height):
    grid = numpy.reshape(data, (width, height))
    # Simply check all possible lines for the maximum subsequence.
    best_horiz = best_vert = best_diag = best_antidiag = 0
    for i in xrange(height):
        best_horiz = max(best_horiz, max_sum_subsequence(grid[i, :]))
    for i in xrange(width):
        best_vert = max(best_vert, max_sum_subsequence(grid[:, i]))
    for i in xrange(-height+1, width):
        best_diag = max(best_diag, max_sum_subsequence(grid.diagonal(i)))
        best_antidiag = max(best_antidiag, \
            max_sum_subsequence(numpy.fliplr(grid).diagonal(i)))
    return max(best_horiz, best_vert, best_diag, best_antidiag)
    
"""
Thoughts: Pretty simple problem, no real math involved in my solution. The
solution for a 1-D array is a well-known (and well taught) problem. There
may be faster solutions for 2-D, but I just applied the 1-D solution to all
possible horizontals, columns, and diagonals. The performance isn't bad either,
taking about 6 seconds to run. I could probably make it faster if I worked
in a lower level language. There is obviously no real math (that I am aware) of
that can be used (it is similar to a linear congruential random number 
generator in fact).
"""
if __name__ == "__main__":
    example = [-2, 5, 3, 2, 9, -6, 5, 1, 3, 2, 7, 3, -1, 8, -4, 8]
    print "Example (given 4x4) (expect 16):"
    print solve_p149(example, 4, 4)
    print "Problem (2000x2000):"
    print solve_p149(sequence(), 2000, 2000)