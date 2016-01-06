# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:24:38 2016

@author: mjcosta
"""
from proj_euler.utils.timing import timefunc

# Returns an infinite generator for fibonacci numbers.
def generate_fibo():
    # n - 1
    fa = 1L
    # n
    fb = 1L
    yield fa
    yield fb
    while True:
        fc = fa + fb
        fa = fb
        fb = fc
        yield fc
        
# Checks if a number is 1-9 pandigital (contains the values 1-9 in any order)
# at the beginning and end of the number.
def is_pandigital(val):
    # First check the last 9 digits, convert to string (expensive) if possible.
    last = val % 1000000000L
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Partial string conversion
    if sorted(str(last)) != digits:
        return False
    # Do the full string conversion
    sval = str(val)
    return sorted(sval[:9]) == digits
    
# Solves problem 104.
@timefunc
def solve_p104():
    # Just get the first index that meets the predicate.
    return next((i+1 for (i, x) in enumerate(generate_fibo()) 
        if is_pandigital(x)), None)

"""
Thoughts: Overall the problem was fairly trivial. I simply wrote an infinite
generator and returned the first number that met the property. However, I did
have to optimize the predicate function since the naive attempt was too slow.
Originally I converted all numbers to strings, but this was slow. Instead, I
computed the last 9 digits (with modulus which is faster) and checked half the
property. In the rare cases where it was true, I would do the full conversion.
"""        
if __name__ == "__main__":
    print solve_p104()