# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:38:19 2016

@author: mjcosta
"""

from proj_euler.utils.memoize import memoize
from proj_euler.utils.exponent import perfect_square
from proj_euler.utils.timing import timefunc

"""

a^2 = x + y
b^2 = x - y
c^2 = y + z
d^2 = y - z
e^2 = x + z
f^2 = x - z

# a % 2 = b % 2
# x > y > z > 0 implies
# a > b implies minimum a >= 9 (b = 1, c = 1)

x = (a + b)/2
y = (a - b)/2
z = c - y = c - (a - b)/2
z = y - d = (a - b)/2 - d
"""
@memoize
def is_square(x):
    return perfect_square(x)

import math

@timefunc
def solve_p142():
    a = 3
    # Increment a^2.
    while True:
        a2 = a ** 2
        # b has the same parity (mod 2) as a
        bstart = 1 if a % 2 == 1 else 2
        for b in xrange(bstart, a, 2):
            b2 = b ** 2
            x = (a2 + b2)/2
            y = (a2 - b2)/2
            c = int(math.ceil(y ** 0.5))
            c2 = c * c
            while c2 < 2*y:
                z = c2 - y
                if is_square(y - z) and is_square(x + z) and is_square(x - z):
                    return (x, y, z), (x + y + z)
                c += 1
                c2 = c * c
        a += 1
       
"""
Thoughts: This was just a brute force solution with some optimizations. It
takes 24 seconds to run. It isn't great but it works. The main idea is to 
change the search space into something reasonable. Clearly, searching all x, 
y, and z is infeasible. Instead, we can constrain our space, to consider only 
square values for some of the relations. We can write:

a^2 = x + y
b^2 = x - y
c^2 = y + z
d^2 = y - z
e^2 = x + z
f^2 = x - z

If we know a^2 and b^2, we can get x and y with: x = (a^2 + b^2)/2 and
y = (a^2 - b^2)/2. Note that since x and y are integers, this adds a constraint
that x mod 2 = y mod 2. Then, to get z, we can plug in x or y in any of the
remaining relations (if we know the other value). So, we can iterate over
the squares of a^2 and b^2 as well as another one of the squares, compute
(x, y, z), and test the remaining squares.

To decide the value of z, I chose to iterate over c^2. Iterating over c^2 for
z (z = c^2 - y), adds a lower bound (c^2 > y since z > 0) and an upper bound
(c^2 < 2y since z < y). Testing the remaining constraints, this approach
allows us to find the answer.
"""         
if __name__ == "__main__":
    print solve_p142()