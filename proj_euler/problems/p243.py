# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:14:42 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import generate_primes
from proj_euler.utils.primes import factor_int_dict

@timefunc    
def solve_p243(plimit, ratio):
    # First compute the primorial which has resilience less than the ratio.
    ps = list(generate_primes(plimit))
    totient = 1
    prod = 2
    index = 1
    last_p = 2
    while index < len(ps) and totient/(prod-1.0) >= ratio:
        totient *= ps[index] - 1
        prod *= ps[index]
        last_p = ps[index]
        index += 1
    # Now compare the primorial value against multiples of the previous
    # primorial which are also less than the ratio.
    best = prod
    start_totient = totient/(last_p - 1)
    start_prod = prod/(last_p)
    for i in xrange(2, last_p):
        mul_fact = factor_int_dict(i)
        new_totient = reduce(lambda a, p: a * p**mul_fact[p], mul_fact, start_totient)
        new_prod = start_prod * i
        if new_totient/(new_prod - 1.0) < ratio and new_prod < best:
            best = new_prod
    return best    

"""
Thoughts: I solved this problem to finish the ternary achievement. From the
problem statement, it is clear that the resilience of n can be calculated as
totient(n)/(n-1) by definition of the totient function. My first attempt was
to sieve totients and compute the min value, but this was too slow.

My second attempt was to only compute candidate values which minimize the
resilience. The ratio of the totient and n is typically minimized when n is
a product of distinct prime factors. This is because the first prime power of p
contributes (p-1) to the ratio and the later powers contribute p instead. If
one adds more than one of the same prime, it does slightly decrease the ratio,
but not as much as a new prime.

Thus, my second attempt involved computing the first primorial (product of
distinct consecutive primes) below the ratio. This answer is wrong by itself,
but we can check against all multiples of the previous primorial (but less than
the valid primorial). This works because adding repeat primes also decreases
the ratio, so it is possible for a smaller value to exist than the primorial
which meets the condition.

This solution comes up with the correct answer in <1 ms, which is fairly
reasonable. It's also a problem that one could potentially do by hand if one
knows the key ideas behind it.
"""
if __name__ == "__main__":    
    print "Example (< 4/10) (expect 12):"
    print solve_p243(5, 4/10.0)
    print "Problem (< 15499/94744):"
    print solve_p243(30, 15499/94744.0)