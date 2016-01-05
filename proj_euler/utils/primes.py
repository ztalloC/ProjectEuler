# -*- coding: utf-8 -*-

import sympy
import sympy.ntheory.generate

# Given a number, returns a list of integer prime factors
def factor_int(n):
    factors = sympy.factorint(n)
    return reduce(list.__add__, map(lambda x: [x] * factors[x], factors))
    
# Given an integer limit, returns a list of primes <= limit
def generate_primes(n):
    return list(sympy.ntheory.generate.primerange(1,n+1))