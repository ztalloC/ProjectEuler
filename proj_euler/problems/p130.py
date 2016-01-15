# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:35:13 2016

@author: mjcosta
"""

from proj_euler.utils.primes import test_primality
from proj_euler.utils.timing import timefunc

from proj_euler.problems.p129 import least_repunit

@timefunc
def solve_p130(num, verbose = True):
    s = 0
    count = 0
    # 9 is the first odd composite value.
    v = 9
    while count < num:
        # Check only composite values
        if not test_primality(v):
            digits = least_repunit(v)
            if (v - 1) % digits == 0:
                s += v
                count += 1
                if verbose:
                    print v
        # Only need to consider 1, 3, 7, and 9, so increment by two.
        v += 2
        # Skip multiples of 5 manually.
        if v % 5 == 0:
            v += 2
    return s

"""
Thoughts: Given an efficient implementation of problem 129, problem 130 is
trivial to solve. Simply iterate over composite values ending in 1, 3, 7, or 9
and sum the values with the desired property.
"""
if __name__ == "__main__":
    print solve_p130(25)