# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:57:13 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Calculates the number of hollow square laminae using at most limit tiles.
@timefunc
def solve_p173(limit):
    # Varying d (the difference between the outer and inner square), we can 
    # compute the number of possible values with (x+d)^2-x^2 = 2xd + d^2.
    d = 2
    result = 0
    while 2*d + d*d < limit:
        result += int((limit - d*d)/(2*d))
        # Note that d must be even by construction of laminae.
        d += 2
    return result

"""
Thoughts: Another really easy problem while I'm deciding on another project.

The number of tiles in a hollow laminae is simply x^2 - y^2 where x is the side
length of the tiled square and y is the dimension of the hole in the square.
Note that y cannot be zero (clarified if you check the 100 tile example). 
Alternatively, one can express the relation in terms of the difference in 
dimensions, I chose: (x+d)^2 - x^2 = 2xd + d^2. If you set the expression
equal to the tile limit and solve for x, you get the number of laminae possible
for a given d. Then just iterate over the possible d (which must be even)
and sum the results.

There is only about 500 values of d to iterate (which perform only constant
time operations), so the performance is predictably good (< 1ms). I probably
could have written a one-liner for it, but the logic is easier to understand
like this. As an aside, this problem is probably suitable for general
programming competitions since it doesn't require that much math.
""" 
if __name__ == "__main__":
    print "Example (100 tiles) (expect 41):"
    print solve_p173(100)
    print "Problem (1e6 tiles):"
    print solve_p173(1e6)