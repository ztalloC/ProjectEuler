# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:24:24 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
from proj_euler.utils.exponent import perfect_square

# Computes the sum of the first num smallest special isoceles triangles.
@timefunc
def solve_p138(num, verbose = True):
    b = 2
    result = 0
    count = 0
    while count < num:
        # The formula is L^2 = 5b^2/4 +/- 2b + 1, so compute each separately.
        L2_partial = 5 * b * b / 4 + 1
        L2_minus = L2_partial - 2 * b
        L2_plus = L2_partial + 2 * b
        # Check if either is a square, never need to worry about both.
        if perfect_square(L2_minus):
            L = int(L2_minus ** 0.5)
            result += L
            count += 1
            if verbose:
                print count, b, "-", L
        if perfect_square(L2_plus):
            L = int(L2_plus ** 0.5)
            result += L
            count += 1
            if verbose:
                print count, b, "+", L
        # Increment b, only even bases.
        b += 2
    return result

if __name__ == "__main__":
    print "Example (2 lowest) (expect 322 = 17 + 305):"
    print solve_p138(2, verbose = False)
    print "Problem (12 lowest):"
    print solve_p138(12)
                