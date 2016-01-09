# -*- coding: utf-8 -*-

import sympy
import sympy.ntheory.generate

# Given a number, returns a list of integer prime factors
def factor_int(n):
    factors = sympy.factorint(n)
    return reduce(list.__add__, map(lambda x: [x] * factors[x], factors))

# Given a number, returns a dictionary containing the prime factorization of n.
def factor_int_dict(n):
    return sympy.factorint(n)

# Given an integer limit, returns a list of primes <= limit
def generate_primes(n):
    return sympy.ntheory.generate.primerange(1,n+1)
    
# Given the dictionary prime factorization, computes the number of factors.
def num_factors(pfact):
    result = 1
    # Simply multiply the exponents + 1
    for p in pfact:
        result *= pfact[p] + 1
    return result