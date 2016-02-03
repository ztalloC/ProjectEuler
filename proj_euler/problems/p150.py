# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:49:14 2016

@author: mjcosta
"""

from numpy import cumsum

from proj_euler.utils.timing import timefunc

# The random number generator specified by problem 150.
def triangle_sequence(upper=500500):
    t = 0
    mod = 2**20
    diff = 2**19
    for k in xrange(upper):
        t = (615949*t + 797807) % mod
        yield (t - diff)

# Builds a list of lists representing the triangle where each entry represents
# a row of the triangle. 
def create_triangle(nrows=1000):
    result = []
    tgen = triangle_sequence(nrows*(nrows + 1)/2)
    for row in xrange(nrows):
        result.append([next(tgen) for x in xrange(row+1)])
    return result


# Finds the smallest possible sub-triangle sum within a triangle where the data
# is a list of lists representing each row of the triangle.    
@timefunc
def solve_p150(data):
    # Calculate cumulative sums for each row, prepend a sentinel 0.
    sums = [[0] + list(cumsum(x)) for x in data]
    best_min = float('inf')
    # Iterate over the top point of the triangle.
    for row in xrange(len(data)):
        for col in xrange(row+1):
            tri_sum = 0
            # Iterate over the levels.
            for level in xrange(row, len(sums)):
                # The sentinel 0 lets us just subtract the element before the 
                # column position (we add 1 to the end position also).
                tri_sum += sums[level][level - row + 1 + col] - sums[level][col]
                best_min = min(best_min, tri_sum)
    return best_min

"""
Thoughts: I definitely over thought this problem. It turns out that brute force
was sufficient. Originally I tried to use some dynamic programming solution
that "merged" the optimal solutions together, but it returned the wrong answer.
The main trick used for this problem was to calculate cumulative sums for each
row and then one can just take the difference of two numbers to compute the sum
of a given range. This is often used in image processing as a 2-D grid (called
an "integral image"). Another one of my attempts was to try to come up with
a triangle version of the integral image, but that didn't work out. Anyway, the
performance isn't great at 69 seconds, but there are faster versions of python
than what I'm using (the default) and I could have easily did a 
multiprocessing.pool.map over the top points of each triangle.
"""
if __name__ == "__main__":
    example = [[15], [-14, -7], [20, -13, -5], [-3, 8, 23, -26], 
               [1, -4, -5, -18, 5], [-16, 31, 2, 9, 28, 3]]
    print "Example (expect -42):"
    print solve_p150(example)
    print "Problem:"
    print solve_p150(create_triangle())    