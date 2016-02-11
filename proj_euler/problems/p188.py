# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:23:17 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Computes the x^^y % mod.
def tetrate(x, y, mod):
    return reduce(lambda a,_: pow(x, a, mod), xrange(y), 1)

solve_p188 = timefunc(tetrate)

"""
Thoughts: Simple one-liner. Looking at the solution thread, I put way less
thought into this problem than I probably should have (though it worked).
""" 
if __name__ == "__main__":
    print "Example (3^^3 mod 100) (expect 87):"
    print solve_p188(3, 3, 100)
    print "Problem (1777^^1855 mod 10^8):"
    print solve_p188(1777, 1855, 10**8)