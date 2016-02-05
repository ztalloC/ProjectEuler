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

# Given a number, returns a partial factorization of n, considering primes
# up to the given limit.
def partial_factor(n, limit):
    return sympy.factorint(n, limit=limit)

# Given an integer limit, returns a generator for primes <= limit. Uses the
# sieve of Eratosthenes. Credit to: http://stackoverflow.com/a/3941967
# It turns out that sympy is a lot slower.
def generate_primes(limit):
    limit = int(limit)                          # Need to convert to int.
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    
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