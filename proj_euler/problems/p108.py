# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:14:59 2016

@author: mjcosta
"""

from itertools import combinations
from operator import div
from operator import mul

from proj_euler.utils.primes import factor_int_dict
from proj_euler.utils.primes import num_factors

from proj_euler.utils.timing import timefunc

# Given the prime factorization of a number, computes the number of distinct
# solutions n for the Diophantine equation. The prime factorization input 
# should be a dictionary where the key is the prime and the value the exponent.
def diophantine_solutions_fact(ps):
    result = 0
    
    # Compute the number of factors.
    factors = num_factors(ps)    
    
    # 1 appears with each factor once and a second time in (1,1)
    result += factors + 1    
    
    # Next, add for each combination of exponents
    for i in range(1, len(ps)+1):
        for combo in combinations(ps, i):
            exponents = [ps[x]+1 for x in combo]
            # Each prime factor limits the pairing that can be done.
            pairs = reduce(div, exponents, factors)
            # But also causes it to appear in more times.
            pairs *= reduce(mul, [ps[x] for x in combo], 1)
            result += pairs
        
    # So far we have computed the number of times each factor has appeared
    # but we want the number of pairs, so just divide by 2
    return result/2
        
# Given a number, computes the number of distinct solutions n to the 
# Diophantine equation 1/x + 1/y = 1/n where x, y, and n are positive integers.
def distinct_diophantine_solutions(n):
    factors = factor_int_dict(n)
    return diophantine_solutions_fact(factors)

@timefunc
# Returns the least value of n which has more than target distinct solutions.
def solve_p108(target):
    i = 2
    while True:
        sols = distinct_diophantine_solutions(i)
        if sols > target:
            return i
        i += 1
"""
Thoughts: Interesting problem. When I first saw the problem, I tried to look
for a pattern. If you convert the fractional equations given in the problem to
integers, you get the equations 4 + 1 = 5, 2 + 1 = 3, and 1 + 1 = 2. Looking
at other numbers, I found a pattern such that a pair would always exist if both
numbers were factors of n and coprime to each other. For a given n, one could
calculate the value by factoring n to get the prime factorization and then
compute the number of solutions (it took a little bit of trial and error to get
right).

After looking at the answers that other people came up with, it seems that my
method of calculating the number of distinct solutions was overly complicated.
One could simply take the exponents of the factorization and compute
sols # = product_i(2*e_i + 1) + 1 / 2 . I do acknowledge that my knowledge of number
theory is limited, so my approach wasn't too bad. It might be useful to know
for problem 110 (a harder version of this problem).
"""    
if __name__ == "__main__":
    print solve_p108(1000)