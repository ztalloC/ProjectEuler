# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:05:34 2016

@author: mjcosta
"""

from itertools import islice

from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import factor_int_dict

# An infinite generator of rows of pascal's triangle.
def pascal_triangle():
    state = [1]
    yield state
    while True:
        state = [1] + [state[i] + state[i+1] for i in xrange(len(state)-1)] + [1]
        yield state

# Computes the sum of the distinct square free numbers in the first nrows rows
# of Pascal's triangle (binomial coefficients).
@timefunc 
def solve_p203(nrows=51):
    rows = islice(pascal_triangle(), 0, nrows)
    # Get the distinct values from the rows.
    distinct = reduce(lambda s, l: s.union(l), rows, set())
    # Factor each integer and test if all prime powers are equal to 1.
    return sum(v for v in distinct if \
        all(x == 1 for x in factor_int_dict(v).values()))

"""
Thoughts: Very simple problem. Just generate the rows of Pascal's triangle,
factor them, and test the square free property. This strategy is very
reasonable since we only want the first 51 rows, so the magnitude and number
of values to factor is small (though some of the values in the last row can get
fairly big). A faster way would be to check the product in the factorials in
the term (n choose k) = n!/k!(n-k)!. But, the method above is faster to write.
It also only takes 13ms to run, so the performance isn't bad either.
"""
if __name__ == "__main__":
    print "Example (8 rows) (expect 105):"
    print solve_p203(8)
    print "Problem (51 rows):"
    print solve_p203(51)