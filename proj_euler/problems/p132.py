# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:02:58 2016

@author: mjcosta
"""

from proj_euler.utils.base import dec_to_bin
from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import generate_infinite_primes

# Given the digits in a repunit and a value, computes R(d) % n.
def repunit_mod(d, n):
    mem = dict()
    mem[1] = 1
    # Need to also simultaneously compute 10^x % n
    digits = dict()
    digits[1] = 10 % n
    # Compute the binary representation of d.
    b = dec_to_bin(d)
    max_exp = 2 ** (len(b) - 1)
    i = 1
    # Compute the powers of two up to the max exponent.
    while i < max_exp:
        digits[2 * i] = (digits[i] * digits[i]) % n
        # Shift R(i) to the left by i values and add R(i)
        mem[2 * i] = (mem[i] * digits[i] + mem[i]) % n
        i *= 2
    # Create the actual value d.
    result = 0
    exp = max_exp
    for v in b:
        if v == '1':
            result = (result * digits[exp] + mem[exp]) % n
        exp /= 2
    return result

# Given the number of digits in a repunit, returns the sum of the first
# num_factor prime factors.
@timefunc
def solve_p132(digits, num_factors):
    found = 0
    result = 0
    for p in generate_infinite_primes():
        if repunit_mod(digits, p) == 0:
            found += 1
            result += p
            if found >= num_factors:
                return result
               
"""
Thoughts: This was a good problem. It's nice to have problems where the answer
is not just optimized brute forcing (but not too hard). Obviously, just trying
to fit a number with 10^9 digits in memory and performing divisions on it would
be too slow. Therefore, it is necessary to use some method that manipulates
exponents. 

The method I came up with is to build up the moduli (for a candidate
prime) for the repunits with binary exponents (2^1, 2^2, 2^4) and then combine
the moduli for the actual number of digits (using the binary representation).
If we can generate large repunits from smaller repunits quickly, then we can
do the same for the moduli. Suppose we have a repunit with n digits, if we
want to generate the repunit with 2n digits, we can simply multiply the repunit
by 10^n (shifting to the left by n places) and then add the repunit. We can do
the same for moduli to compute the moduli values. Note that I also build up
the values of 10^n recursively (represented as a moduli).

The code is reasonably fast, taking about 300ms to run. So, I am satisfied with
the performance of this solution. I did look at problem 133 (which also 
considers factors for repunits with power of 10 digits). While I cannot
reuse the code, I can use the insights from this problem to solve it.
"""
if __name__ == "__main__":
    print "Example (d = 10, 4 factors) (expect 9414):"
    print solve_p132(10, 4)
    print "Problem (d = 10^9, 40 factors):"
    print solve_p132(10**9, 40)
        