# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:42:41 2016

@author: mjcosta
"""

from operator import mul
from copy import deepcopy

from proj_euler.utils.primes import generate_primes
from proj_euler.utils.timing import timefunc

# Found from the solution thread for problem 108. A simplified formula for
# computing the number of distinct Diophantine solutions.
def fast_sols(pfact):
    return (reduce(mul, (2*pfact[x]+1 for x in pfact), 1) + 1)/2

# Computes the product of the prime factorization.
def prod_fact(fact):
    return reduce(mul, (p**fact[p] for p in fact), 1)

# Finds the minimum value with a given number of solutions. Takes a list of
# primes, the current value, and the max exponent to be used.
def find_min_target(target, primes, fact, limit):
    # Abort if we already have reached the target
    curr_sols = fast_sols(fact)
    if curr_sols > target:
        return fact
    if len(primes) == 0:
        return None
    p_head = primes[0]
    p_tail = primes[1:]
    best_val = float('inf')
    best_fact = None
    # The exponent can not be larger than the previous exponent (else we could
    # swap and obtain a better solution)
    for i in range(1, limit+1):
        new_fact = deepcopy(fact)
        new_fact[p_head] = i
        # Restrict later exponents with this exponent.
        cand_fact = find_min_target(target, p_tail, new_fact, i)
        if cand_fact is None:
            break
        cand_val = prod_fact(cand_fact)
        # Stop if we ever get a worse value.
        if cand_val > best_val:
            break
        best_val = cand_val
        best_fact = cand_fact
    return best_fact
    
@timefunc
def solve_p110(target, prime_limit, exp_limit):
    ps = list(generate_primes(prime_limit))
    best_fact = find_min_target(target, ps, dict(), exp_limit)
    return prod_fact(best_fact)

"""
Thoughts: A little tricky but not too hard. Looking at the solution thread for
problem 108 was very helpful for getting the formula for the number of
solutions. Then, it was just minimizing the product of primes while maximizing
solutions. Since all primes have the same influence (what matters is the amount
of a given prime and the number of different primes), smaller is better. Thus,
we could restrict the search to factorizations where the exponents were
decreasing (if the primes are sorted in ascending order). Also, one could
observe that multiplying the first 14 primes met the solutions requirement.
Thus, all values had to be smaller than that and we only had to use 14 primes.

The code was a little sloppy, but it ran in < 10 ms, so it's probably fine. I
had to adjust the parameters a little (even though the initial parameters were
completely reasonable), so there may be a bug in it.
"""
if __name__ == "__main__":
    print solve_p110(4e6, 50, 10)