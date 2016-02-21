# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:25:47 2016

@author: mjcosta
"""

import numpy

from itertools import combinations
from itertools import islice
from numpy import cross
from fractions import gcd

from proj_euler.utils.timing import timefunc

# An infinite generator for the Blum-Blum-Shub PRNG.
def blum_blum_shub(init=290797, mod_iter=50515093, mod_out=500):
    state = init
    while True:
        state = (state * state) % mod_iter
        yield state % mod_out

# An infinite generator of line segments (where points are represented as
# numpy array for ease of manipulation) with the blum-blum-shub PRNG.
def line_gen():
    bbs = blum_blum_shub()
    while True:
        t1, t2, t3, t4 = [next(bbs) for i in xrange(4)]
        yield (numpy.array([t1, t2]), numpy.array([t3, t4]))

# Tests if two line segments (p1A, p2A) and (p1B, p2B) have a true intersection
# point and returns it if so. Assumes all points are numpy arrays.
# Credit to: http://stackoverflow.com/a/565282
def compute_true_intersection(p1A, p2A, p1B, p2B):
    # Represent one line as p + tr and another as q + us
    p = p1A
    r = p2A - p1A
    q = p1B
    s = p2B - p1B
    rs = int(cross(r, s))
    if rs == 0:
        return None
    # t = cross((q - p), s)/rs
    # u = cross((q - p), r)/rs
    qps = int(cross(q-p, s))
    qpr = int(cross(q-p, r))    
    tr = qps/float(rs)
    ur = qpr/float(rs)
    # Test the ranges of u and t, can use a float representation of u and t
    # for testing ranges (which is slightly faster than calculating exactly).
    if ur > 0 and ur < 1 and tr > 0 and tr < 1:
        # For the actual coordinate, represent as a fraction tuple. The
        # code using the Fraction class is much simpler but also slower.
        gcd_s = gcd(qps, rs)
        t = (qps / gcd_s, rs / gcd_s)
        # p + t * r
        intersect = ((p[0] * t[1] + r[0] * t[0], t[1]),
                     (p[1] * t[1] + r[1] * t[0], t[1]))
        gcd_x = gcd(intersect[0][0], intersect[0][1])
        gcd_y = gcd(intersect[1][0], intersect[1][1])
        return ((intersect[0][0] / gcd_x, intersect[0][1] / gcd_x),
                (intersect[1][0] / gcd_y, intersect[1][1] / gcd_y))
    else:
        return None

@timefunc        
def solve_p165(num_lines=5000):
    # Generate the lines.
    lines = islice(line_gen(), 0, num_lines)
    # Get the distinct intersection points.
    intersections = set(compute_true_intersection(p1[0], p1[1], p2[0], p2[1]) \
        for p1, p2 in combinations(lines, 2))
    # Remember not to include None if present.
    return len(intersections) - 1 if None in intersections else len(intersections)
    
"""
Thoughts: For this problem I just used a simple brute force approach by testing
all combinations of line segments and computing the distinct points of
intersection. To test whether two line segments intersect, one can use cross
products (I referenced a stackoverflow answer for the formula). Since this
is where a lot of time is spent in the code, I tried to make this fast. The
resulting performance is not good, taking 265 seconds to finish. The main
optimization I could do is to check the bounding boxes of the line segments
(which is fast compared to computing cross products). In this manner, one
could omit many of the comparisons. However, I'm tired, so I'll leave it as is
since it isn't that important.
"""
if __name__ == "__main__":
    print solve_p165()