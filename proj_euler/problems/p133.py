# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:24:40 2016

@author: mjcosta
"""

from proj_euler.utils.base import dec_to_bin
from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import generate_primes

# Given the digits in a repunit and a value, computes R(d) % n.
# This is a modification of the function from problem 132 which now allows
# for re-using some of the work.
def repunit_mod(d, n, mem, digits):
    # If digits has not been initialized (implying mem is not either), then
    # set the appropriate values for 1.
    if len(digits) == 0:
        digits[1] = 10 % n
        mem[1] = 1
        i = 1
    # If resuming from previous call, use the max value present.
    else:
        i = max(mem)
    # Compute the binary representation of d.
    b = dec_to_bin(d)
    max_exp = 2 ** (len(b) - 1)
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
    
# Tests whether a value is a factor of any repunit . Also, takes a limit of
# when to stop considering factors (may not be 100% accurate, but speeds up
# considerably and can be tuned if needed).
def test_repunit_factor(n, limit = None):
    mem = dict()
    digits = dict()
    num_digits = 1
    # Keep track of the moduli we have seen, a repeat means it is not possible.
    seen = set()
    while True:
        modulus = repunit_mod(num_digits, n, mem, digits)
        # Found a factor.
        if modulus == 0:
            return True
        # Seen the same moduli twice, thus there is a cycle, impossible for
        # it to be a factor.
        elif modulus in seen or (limit is not None and len(seen) >= limit):
            return False
        # Track the moduli we have seen and update the number of digits.
        seen.add(modulus)
        num_digits *= 10

# Computes the sum of all repunit nonfactors below a limit.
@timefunc
def solve_p133(limit, test_limit = None):
    result = 0
    for p in generate_primes(limit):
        if not test_repunit_factor(p, test_limit):
            result += p
    return result

"""
Thoughts: Not a hard problem once you have solved 132. My initial thought was
to take problem 132's code and modify it slightly so that one can re-use work
between invocations (for the same prime). Then, one can test values of 10^n
until the modulus is either 0 (is a factor) or the modulus repeats (a cycle,
so impossible to be a factor).

However, I tried running it but it seemed to be too slow. I then tried running
it again, outputting the number of moduli tested before coming to a conclusion.
I found that for impossible factors, the number of values to test before
finding a cycle varied greatly (some over 1000), while factors were found 
within 10 values (at least within the minute or so that I ran it). Therefore,
I decided to try limiting the max number of moduli to test (substantially
improving the worse case) with a configurable parameter. 

Although, I never observed a factor taking over 10 tests, I used a limit of 20 
to be safe (I also tried larger values, seeing if there was a difference). The
solution I got was correct and the performance was reasonable (1.7s). However,
this was ultimately an approximation as it may be possible for factors to
require a larger number of tests.

After getting the solution correct, I checked the solutions thread. Other
people had found that a prime is not a factor if and only if A(p) has a prime
factor other than 2 or 5 (where A(p) is the function from problem 129). This
is much more precise than my solution (though there were some people who
used a similar strategy as me), and should be used in future problems if
relevant. 
"""
if __name__ == "__main__":
    # Note: Manually computed 918. The sum of the primes under 100 is 1060
    # and only 11, 17, 41, and 73 are factors. Thus, 1060-11-17-41-73 = 918.
    print "Example (< 100) (expect 918):"
    print solve_p133(100)
    print "Problem (< 100,000):"
    print solve_p133(1e5, 20)
