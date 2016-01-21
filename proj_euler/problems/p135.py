# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 07:47:00 2016

@author: mjcosta
"""


from collections import defaultdict

from proj_euler.utils.timing import timefunc


@timefunc
def solve_p135(limit, target):
    counts = defaultdict(int)
    f = lambda x, d: -(x - 5*d) * (x - d)
    d = 1
    # Iterate over the differences, stop if the least value exceeds limit.
    while f(d + 1, d) <= limit:
        x = d + 1
        # The max value is at 3d
        xlimit = 3 * d
        while x < xlimit:
            v = f(x, d)
            if v >= limit:
                break
            # Only consider the upper half (which is valid) for invalid values.
            if x < 2 * d + 1:
                counts[v] += 1
            # Can double count if both sets are valid.
            else:
                counts[v] += 2
            x += 1
        # If we did not stop prematurely before 3d, add the unique value at 3d.
        if x == xlimit:
            counts[f(x, d)] += 1
        d += 1
    return sum(1 for k in counts if counts[k] == target)

"""
Thoughts: Definitely more of a thinking problem than an optimization problem.
I probably could have just brute forced it, but I was under the impression that
it was going to be too big for some reason. Anyway, the problem was to come
up with the number of distinct solutions of n for x^2 - y^2 - z^2 = n where
x, y, and z are positive integers in an arithmetic progression.

I used a few ideas to solve this problem. First, given a difference of d, one
can expand the equation for n and re-factor it to get: n = -(x-d)(x-5d). This
form has a few implications. 

First, for a given d, we only need to consider the range d < x < 5d where the 
equation is positive. Next, the equation is quadratic, so the maximum occurs 
at 3d (in the middle of the range) and the values on each side of 3d are 
symmetric. Therefore, we only need to consider 2d + 1 of the values at most 
(we can stop prematurely if we pass the limit). 

However, if d < x <= 2d,  then the z term in x^2-y^2-z^2 is negative or zero.
Therefore, we have to ignore those values, but we still have to search 
2d + 1 values, since the range (4d, 5d) is actually valid. So, we count 
1 value in the range (d, 2d] and 2 values for the range (2d, 3d).

Then, we just need to iterate over the possible values of d and x within the
limit. We constrained x based on d (d < x <= 3d), and we can constrain d
by using the minimum possible x (d+1) for a given d. The performance of the
resulting code is fairly good (900ms for 1e6), so it isn't bad.
"""
if __name__ == "__main__":
    print solve_p135(1e6, 10)