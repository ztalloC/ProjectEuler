# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:06:55 2015

@author: mjcosta
"""

import itertools
import numpy

from proj_euler.utils.timing import timefunc

# Given two points (numpy arrays), returns true if a right triangle
def is_right_triangle(a, b):
    return (numpy.dot(a, b) == 0) or (numpy.dot(a, b-a) == 0) or \
        (numpy.dot(b, a-b) == 0)

# Counts all triangle points by brute force
@timefunc
def count_triangle_coords(n):
    point_set = []
    count = 0
    # Generate all possible points
    for i in range(n+1):
        for j in range(n+1):
            if i != 0 or j != 0:
                point_set.append(numpy.array((i,j)))
    # Generate all possible combinations of points
    for i in itertools.combinations(point_set, 2):
        if is_right_triangle(i[0], i[1]):
            count += 1

    return count

"""
Thoughts: In the end I just brute forced this solution. The number of
possibilities was small enough where it wasn't a big deal to do so. I read
up on how other people solved this problem afterwards and found that the 
geometry was simple.
"""
if __name__ == "__main__":
    # The values of n to evaluate
    n_values = [2,50]
    for n in n_values:
        # Get the result and time it took
        result = count_triangle_coords(n)
        # Print the results
        print "The answer for (n = %d) is: %d" % (n, result)