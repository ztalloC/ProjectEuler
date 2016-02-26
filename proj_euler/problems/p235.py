# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:34:32 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

def binary_search_series(low, high, f, target, eps = 0.1):
    # Note: We never have to worry about a base case since the value does exist
    # and we are working with decimals not integers.
    mid = (low + high)/2
    y = f(mid)
    if abs(y - target) < eps:
        return mid
    # Note: the range is descending, so the halves we inspect are reversed.
    elif y < target:
        # target is greater, so look in left half.
        return binary_search_series(low, mid, f, target)
    else:
        return binary_search_series(mid, high, f, target)

@timefunc
def solve_p235(n, target, eps = 0.1):
    f = lambda r: sum((900-3*k)*r**(k-1) for k in xrange(1, n+1))
    return binary_search_series(1.0, 1.1, f, target, eps)
    
"""
Thoughts: Not a very difficult problem, but interesting (at least for me). I
searched briefly on the topic of series and there may be a closed form solution
to this problem, but I didn't want to work it out. Anyway, the main method I
used was the bisection method (or binary search) to look for a solution to
the equation (at least within a certain number of decimal places). Since the
function is monotone decreasing, the binary search method works fine. 

The program finishes in 0.4 seconds, which is reasonable. Since I never really
studied optimization (related to mathematical functions), it was slightly
interesting and a nice refresher on search methods. 
"""
if __name__ == "__main__":
    print "%.12f" % solve_p235(5000, -6*10**11, 0.1)