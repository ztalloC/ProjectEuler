# -*- coding: utf-8 -*-

import sympy
import sympy.ntheory.generate
import sympy.ntheory.primetest

from sympy.ntheory.generate import Sieve

# Given a number, returns a list of integer prime factors
def factor_int(n):
    factors = sympy.factorint(n)
    return reduce(list.__add__, map(lambda x: [x] * factors[x], factors))

# Given a number, returns a dictionary containing the prime factorization of n.
def factor_int_dict(n):
    return sympy.factorint(n)

# Given an integer limit, returns a generator for primes <= limit
def generate_primes(n):
    return sympy.ntheory.generate.primerange(1,n+1)
    
# Returns a generator for primes within the range [a, b).
def generate_primerange(a, b):
    return sympy.ntheory.generate.primerange(a, b)

# Returns an infinite generator of primes, can optionally specify from which
# value prime to start from.
def generate_infinite_primes(start = 1):
    s = Sieve()
    while True:
        yield s[start]
        start += 1

# Tests whether a number is prime.
def test_primality(n):
    return sympy.ntheory.primetest.isprime(n)

# Given the dictionary prime factorization, computes the number of factors.
def num_factors(pfact):
    result = 1
    # Simply multiply the exponents + 1
    for p in pfact:
        result *= pfact[p] + 1
    return result