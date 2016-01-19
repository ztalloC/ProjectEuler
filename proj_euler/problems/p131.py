# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 08:23:00 2016

@author: mjcosta
"""

from itertools import combinations

from proj_euler.utils.primes import test_primality
from proj_euler.utils.timing import timefunc

# Returns a generator to all cubes such that the difference between successive
# cubes is less than or equal to the limit.
def gen_cubes(limit):
    prev_cube = 1
    yield (1, prev_cube)
    i = 2
    curr_cube = i ** 3
    while curr_cube - prev_cube <= limit:
        yield (i, curr_cube)
        prev_cube = curr_cube
        i += 1
        curr_cube = i ** 3

@timefunc
def solve_p131(limit):
    result = 0
    cubes = gen_cubes(limit)
    # Check all combinations of cubes.
    for combo in combinations(cubes, 2):
        ((i, c_i), (j, c_j)) = combo
        if c_j - c_i > limit:
            continue
        if test_primality(c_j - c_i):
            result += 1
    return result

"""
Thoughts: Slightly tricky since I was initially thinking about how to brute
force it rather than the math behind it. The math is relatively simple, 
n^3 + n^2 * p = x^3 => n^3 (1 + p/n) = x^3 => n (1 + p\n)^(1/3) = x =>
(1 + p/n)^(1/3) = ((n + p)/n)^(1/3) must be an integer. Therefore n + p and
n must be perfect cubes. 

From this, we can simply test all combinations of 2 cubes (limiting the
maximum difference between cubes) and check if the difference is prime. Then,
just count the number of answers. The speed is quite good since we only have
to test all combinations of 577 cubes. I later found out in the solution thread
that one only needs to consider successive cubes, which isn't hard to realize,
but I was just in a hurry to get the answer.
"""
if __name__ == "__main__":
    print "Example (p < 100) (expect 4):"
    print solve_p131(100)
    print "Problem (p < 1,000,000):"
    print solve_p131(1e6)