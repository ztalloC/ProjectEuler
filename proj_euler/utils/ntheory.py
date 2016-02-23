# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:54:34 2016

@author: mjcosta
"""

# Computes all values of the mobius function for the interval [1, n]. The 
# mobius function is defined as: 1 if n = 1, 0 if n has a squared prime factor,
# and (-1)^k if n is a square-free positive integer with k prime factors.
# The algorithm is essentially a modified Eratosthenes sieve.
#
# Credit for basic idea: http://mathoverflow.net/q/99473
def generate_mobius(n):
    n = int(n)      # Convert to int if float (common to pass float values).
    a = [1] * (n+1) # Add a zero value to simplify indexing.
    a[0] = 0
    for i in xrange(2, n+1):
        # A value that hasn't been visited before is a prime.
        if a[i] == 1:
            # Change the parity for multiples of i.
            for j in xrange(i, n+1, i):
                a[j] *= -i
            # Squares of i are set to 0.
            for j in xrange(i*i, n+1, i*i):
                a[j] = 0
    # The mobius function is just the sign, omit the zero value.
    return [cmp(x, 0) for x in a[1:]]
    
# Computes all values of the totient function for the interval [1, n]. The
# totient function is defined as the number of positive values less than n that
# are coprime to n. The algorithm is essentially a modified Eratosthenes sieve.
def generate_totient(n):
    n = int(n)      # Convert to int if float (common to pass float values).
    a = [1] * (n+1) # Add a zero value to simplify indexing.
    for i in xrange(2, n+1):
        # A value that hasn't been visited before is a prime.
        if a[i] == 1:
            power = i
            # Update the multiples of prime powers.
            while power <= n:
                for j in xrange(power, n+1, power):
                    # A prime contributes p-1 values for p^1 and p values for
                    # each prime power after.
                    a[j] *= i-1 if power == i else i
                power *= i
    return a[1:]