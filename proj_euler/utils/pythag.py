# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:07:48 2016

@author: mjcosta
"""

from fractions import gcd

# Generates all primitive pythagorean triples where the perimeter is under
# a limit. Triples are not presented in any given order.
def primitive_pythag_perim(plimit):
    # Euclid's method for generating Pythagorean triples given m > n > 0.
    triples = lambda m, n: (m**2 - n**2, 2 * m * n, m**2 + n**2)
    m = 2
    # For a given m, n = 1 is the smallest perimeter (but may not be valid).
    while sum(triples(m, 1)) < plimit:
        # One of m and n must be even and the other odd.
        n = 1 if m % 2 == 0 else 2
        while n < m:
            t = triples(m, n)
            if sum(t) >= plimit:
                break
            # m and n must be coprime for the triple to be primitive.
            if gcd(m, n) == 1:
                # Values may not be presented in order a < b < c.
                yield tuple(sorted(t))
            n += 2
        m += 1

# Generates all pythagorean triples where the perimeter is under a limit.
# Triples are not presented in any given order.
def pythag_perim(plimit):
    # Simply generate the primitive triples and multiply by a constant.
    for primitive in primitive_pythag_perim(plimit):
        pperim = perim = sum(primitive)
        current = primitive
        while perim < plimit:
            yield current
            # Add a multiple of the primitive to the current.
            current = tuple(sum(x) for x in zip(current, primitive))
            perim += pperim