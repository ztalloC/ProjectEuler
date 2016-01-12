# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:40:13 2016

@author: mjcosta
"""

from proj_euler.utils.primes import generate_infinite_primes
from proj_euler.utils.timing import timefunc

# Computes the remainder according to the formula given in problem 123.
def compute_remainder(n, p):
    return ((p-1)**n + (p+1)**n) % (p * p)
    
# Computes the remainder using a smarter formula.
def compute_remainder_fast(n, p):
    if n % 2 == 0:
        return 2
    else:
        return (2 * n * p) % (p * p)

# Given a target, computes the least value of n which exceeds a target.
# One may optionally specify a value of n to start from.
@timefunc
def solve_p123(target, start = 1):
    for (n, p) in enumerate(generate_infinite_primes(start), start):        
        if compute_remainder_fast(n, p) > target:
            return n

"""
Thoughts: This was simple to brute force, but my initial solutions was a little
slow (took over a minute). I decided to look at the solution thread for 120
(a related question which I had solved previously), and found there was a 
faster way of computing the remainder. If I had spent more time on 120, I
probably would have come across this on my own, but it isn't a huge deal. 

The faster way of computing the remainder is to return 2 if n is even or
the product 2np (divided by p^2) for odd n. The reason this works is because
most of the terms in (p-1)^n and (p+1)^n have exponents >= 2 and thus
reduce to zero mod p^2. When n is even, the two components cancel out to two,
while for n odd, the two terms add up to 2*n*p (simply because of how the
polynomials expand).

Using the fast remainder method, the code executes in a reasonable amount of
time (~68 ms). I added a new infinite prime generator which is slightly slower
if only small primes are needed, but is useful for large primes (where the
bound is unknown).
"""
if __name__ == "__main__":
    print "Example (> 10^9) (expect 7037):"
    print solve_p123(10**9)
    print "Problem (> 10^10):"
    print solve_p123(10**10)