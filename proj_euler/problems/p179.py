# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:50:31 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Computes the number of positive divisors for all values in the range [0, n].
def factor_sieve(n):
    # To simplify indexing, add an extra element at beginning.
    a = [1]*(n+1)
    a[0] = 0
    for i in xrange(2, n+1):
        # Prime entry.
        if a[i] == 1:
            curr_power = i
            power = 1
            # Iterate through each multiple of each prime power, a given power
            # contributes (power + 1) new possible values to combine with.
            while curr_power <= n:
                for j in xrange(curr_power, n+1, curr_power):
                    # Remove the influence of the lower power, add the new one.
                    a[j] /= power
                    a[j] *= (power + 1)
                power += 1
                curr_power *= i
    return a
    
# Computes the number of integers 1 < n < limit for which n and n+1 have the
# same number of positive divisors.
@timefunc
def solve_p179(limit):
    factors = factor_sieve(limit)
    # Start from n = 2, iterate until just before the limit.
    return sum(1 for i in xrange(2, limit) if factors[i] == factors[i+1])
    
"""
Thoughts: Relatively simple problem. One can write an Eratosthenes sieve
variant which computes the number of positive divisors. It may be possible
to write the sieve more efficiently, but the result is not bad. Then just
iterate through the list of values and compute the desired property. The entire 
problem takes 6 seconds to run, which is okay (could be faster in C/C++).
"""
if __name__ == "__main__":
    # Example has (2, 3) and (14, 15).
    print "Example (n < 15) (expect 2):"
    print solve_p179(15)
    print "Problem (n < 10^7):"
    print solve_p179(10**7)