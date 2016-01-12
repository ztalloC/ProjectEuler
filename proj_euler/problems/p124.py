# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:27:37 2016

@author: mjcosta
"""

from operator import mul

from proj_euler.utils.primes import factor_int_dict
from proj_euler.utils.timing import timefunc

# Computes the radical of n (the product of distinct prime factors).
def compute_radical(n):
    return reduce(mul, factor_int_dict(n).keys(), 1)
    
# Computes the kth element in the sorted list of radicals from low to high.
@timefunc
def solve_p124(k, low, high):
    values = []
    # Simply brute force the values.
    for i in xrange(low, high+1):
        values.append((i, compute_radical(i)))
    # Sort by the radical in ascending order, we use the fact that timsort
    # is a stable sort (and is already sorted by n) in order to break ties.
    values.sort(key=lambda x: x[1])
    return values[k-1][0]

"""
Thoughts: The problem was a trivial brute force. I simply factored all the
values from 1 to 100,000, computed the radicals, sorted and computed the
result. The factoring is the only slow section, but it would not be hard to
replace with some method that generates numbers from prime factors. However,
it's not worth the trouble since it already runs in under a second.
"""
if __name__ == "__main__":
    print "Example (k = 4) (expect 8):"
    print solve_p124(4, 1, 10)
    print "Example (k = 6) (expect 9):"
    print solve_p124(6, 1, 10)
    print "Problem (k = 10000):"
    print solve_p124(10000, 1, 100000)
