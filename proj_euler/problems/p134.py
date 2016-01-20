# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 01:27:52 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
from proj_euler.utils.modulo import modinv
from proj_euler.utils.primes import generate_infinite_primes

# Computes the minimum value ending with the digits p1 that is divisible by p2.
def min_digits(p1, p2):
    # We want to solve the equation 10^d * x + p1 = 0 mod p2.
    base = 10 ** len(str(p1))
    modulo = p2 - p1
    inv = modinv(base, p2)
    x = inv * modulo % p2
    return base * x + p1
    
# Computes the sum of s for every prime pair between start and end (inclusive).
@timefunc
def solve_p134(start, end):
    result = 0
    p_gen = generate_infinite_primes()
    p_prev = None
    # Iterate until we pass the lower bound.
    while p_prev is None or p_prev < start:
        p_prev = next(p_gen)
    # Iterate until we pass the upper bound.
    while p_prev <= end:
        p_curr = next(p_gen)
        result += min_digits(p_prev, p_curr)
        p_prev = p_curr
    return result

"""
Thoughts: A fairly easy problem if you apply basic modulo arithmetic. The only
issue I had with this problem was that I misread the range for p1. The basic
idea is that we can find the smallest value that satisfies the equation
10^d * x + p1 = 0 mod p2 where d is the number of digits in p1. Solving this
congruence is trivial, so it's a simple matter of iterating over the primes.
The program runs in 700ms, so the performance isn't bad either.
"""
if __name__ == "__main__":
    print "Example (19) (expect 1219):"
    print solve_p134(19, 19)
    print "Problem (5, 1000000):"
    print solve_p134(5, 1000000)