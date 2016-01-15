# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:45:14 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
        
# Given a value n, computes the number of digits in the least repunit 
# which is divisible by n.
def least_repunit(n):
    # Check gcd(n, 10) = 1, if not return 0.
    if n % 5 == 0 or n % 2 == 0:
        return 0
    digits = 1
    rep = 1
    while rep != 0:
        rep = (rep * 10 + 1) % n
        digits += 1
    return digits
            
@timefunc
def solve_p129(target):
    # Start at the first valid number greater than or equal to the target.
    n = target
    while n % 2 == 0 or n % 2 == 5:
        n += 1
    while least_repunit(n) <= target:
        # Increment by two since only need to consider odd values.        
        n += 2
    return n

"""
Thoughts: This was truly a problem where having an understanding of the math
behind the problem is useful. Initially, it might seem that brute forcing the
problem is impractical. The naive way is certainly too slow (test each value
starting from 1 and doing quadratic work on increasingly large numbers). But,
it's actually quite fast with a few optimizations.

The first optimization is trivial based off the gcd requirement. Since
gcd(n, 10) = 1, we only need to consider values ending with 1, 3, 7, and 9.
This saves us around 60% of the needed work if we were to consider all values,
but this is nowhere near enough to solve the problem.

The second optimization is to reduce the size of the division (rather than
working with million digit numbers). This can be done by computing the modulus
while generating the repunits and only working with the modulus. Thus, the
size of the value we work with is bounded by n.

The last optimization is to only consider values of n greater than or equal
to the target (i.e. start the target instead of 1). The reason is that the
maximum value of A(n) must be less than or equal to n. When computing the
number of digits in the least repunit, we work with a value modulo n. The only
way for A(n) > n is if there was a cycle in the modulo sequence (by the
pigeonhole principle), but then it would repeat forever and there would be
no solution (which the problem states can't happen). Therefore, A(n) <= n, and
we can start at the target instead of 1.
"""
if __name__ == "__main__":
    print "Example (10) (expect 17):"
    print solve_p129(10)
    print "Example (1e6):"
    print solve_p129(int(1e6))