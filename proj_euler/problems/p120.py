# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:53:52 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

@timefunc
def solve_p120(start, end):
    f = lambda a: lambda n: ((a-1)**n + (a+1)**n) % (a*a)
    result = 0
    for a in xrange(start, end+1):
        result += max(f(a)(n) for n in xrange(2*a))
    return result

"""
Thoughts: Just a brute force problem. One can observe that for a given "a",
the cycle has a period of 2a. It takes ~30 seconds, so it could be better, but
it isn't really worth it. One could trivially just build the exponents
incrementally rather than recomputing them.
"""
if __name__ == "__main__":
    print "Example (a = 7) (Expect 42):"
    print solve_p120(7, 7)
    print "Problem (3 <= a <= 1000):"
    print solve_p120(3, 1000)
        