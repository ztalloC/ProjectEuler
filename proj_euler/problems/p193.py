# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:36:46 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
from proj_euler.utils.ntheory import generate_mobius

# Computes the number of square free values less than limit.
@timefunc
def solve_p193(limit):
    # Credit for formula: http://math.stackexchange.com/a/932762
    # Formula computes inclusive range, want exclusive range.
    limit = limit - 1
    sqrt = int(limit**0.5)
    return sum(v*(limit/(i*i)) for (i, v) in enumerate(generate_mobius(sqrt), 1))

"""
Thoughts: Relatively simple problem if you know the formula. I did not know
the formula offhand, so I looked it up (credited in the function). The formula
uses the mobius function, which I was able to compute using a modified sieve
of Eratosthenes. The solution takes about 23 seconds to solve, which is
primarily dominated by the sieving time (which is more suited for a lower
level language like C/C++).
"""
if __name__ == "__main__":
    # Example from: http://math.stackexchange.com/q/534076
    print "Example (< 2014) (expect 1223):"
    print solve_p193(2014)
    print "Problem (< 2^50):"
    print solve_p193(2**50)