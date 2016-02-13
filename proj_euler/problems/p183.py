# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 09:30:53 2016

@author: mjcosta
"""

import math
from fractions import gcd

from proj_euler.utils.timing import timefunc

@timefunc
def solve_p183(low, high):
    result = 0
    for i in xrange(low, high+1):
        # Optimal k has N/k approximate e, so optimal k is N/e.
        best_k = round(i/math.e)
        # Reduce the fraction to simplest form.
        best_k /= gcd(best_k, i)
        # Remove the 2 and 5 factors.
        while best_k % 2 == 0:
            best_k /= 2
        while best_k % 5 == 0:
            best_k /= 5
        # If remaining factors, then non-terminating, otherwise terminating.
        result += i if best_k != 1 else -i
    return result

"""
Thoughts: Really simple problem. I computed the derivative of (N/k)^k with
respect to k and found that the optimal k is when log(N/k) - 1 = 0, so N/k = e.
So, one can just round N/e to the nearest integer for each N, simplify the
fraction to simplest term, and check k for factors other than 2 and 5. Since
we have just ~10000 values to check, it only took 12ms to finish.
"""    
if __name__ == "__main__":
    print "Example (5 to 100) (expect 2438):"
    print solve_p183(5, 100)
    print "Problem (5 to 10,000):"
    print solve_p183(5, 10000)