# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:52:59 2016

@author: mjcosta
"""

from itertools import permutations

from proj_euler.utils.memoize import memoize
from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import test_primality

# Returns a generator for all possible partitions of a list.
# Only generates partitions that are in sorted order.
def generate_partitions(xs, best = 0):
    if len(xs) == 0:
        yield []
    else:
        i = 0
        v = 0
        while i < len(xs):
            v = 10 * v + xs[i]
            # Only generate if this is the largest current value.
            if v > best:
                for part in generate_partitions(xs[i+1:], v):
                    part.insert(0, v)
                    yield part
            i += 1

@memoize
# Tests if a value is prime, uses memoization for a slight speedup.
def is_prime(v):
    return test_primality(v)

# Given a permutation of values, counts the number of valid partitions.
def count_valid_partitions(perm):
    count = 0
    for part in generate_partitions(perm):
        # All the values need to be prime as well.
        if all(is_prime(x) for x in part):
            count += 1
    return count
    
@timefunc
def solve_p118():
    result = 0
    # Generate all permutations and count the number of valid partitions for
    # each permutation. Only use the digits 1-9.
    for perm in permutations(range(1, 10)):
        result += count_valid_partitions(perm)
    return result
   
"""
Thoughts: This was a reasonable problem. My first thought was to generate
all the primes, filter, and then combine. However, just generating the primes
(up to 8 digits since 9 digits aren't relevant) was slow, so I decided not to.
The later approach (remniscent of previous problems) was just to generate
all possible values with the given digits and filter based on primality. In
this case, I also had to transform the permutations into ordered sets by
partitioning them. 

The speed was okay, but not great (around 19 seconds). For this problem I also
created a memoization decorator (using the classical recipe). It made sense for
this problem, but I might not always use it since I like having flexibility
with memoization (by doing it manually).
"""
if __name__ == "__main__":
    print solve_p118()