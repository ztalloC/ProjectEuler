# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:25:49 2016

@author: mjcosta
"""

from fractions import gcd
from operator import mul

from proj_euler.utils.primes import factor_int_dict
from proj_euler.utils.timing import timefunc

# Computes the radical for a given value.
def radical(n):
    return reduce(mul, factor_int_dict(n).keys(), 1)

# Computes a sorted list and a dictionary of radicals less than the limit.
def radical_list(limit):
    srads = []
    drads = dict()
    for i in xrange(1, limit):
        rad = radical(i)
        srads.append((i, rad))
        drads[i] = rad
    srads.sort(key=lambda x: x[1])
    return srads, drads
        
# Given the sorted list of radicals and a dictionary of radicals, computes 
# whether a given c has an abc-hit.
def check_abc_hit(c, rad_list, rad_dict):    
    # For values with unique factorizations, simply skip them.
    if rad_dict[c] == c:
        return 0
    
    # Divide c by the radical of c to get a limit for a and b's radicals.
    cratio = c / rad_dict[c]
    result = 0
    # Check the radicals less than the cratio.
    i = 0
    while i < len(rad_list) and rad_list[i][1] < cratio:
        a, rad_a = rad_list[i]
        b = c - a
        # Skip if the relation isn't maintained.
        if not (a < b):
            i += 1
            continue
        rad_b = rad_dict[b]
        if gcd(a, c) == 1 and rad_a * rad_b < cratio:
            result += 1
        i += 1
    return result

@timefunc 
def solve_p127(limit):
    rad_list, rad_dict = radical_list(limit)
    return sum(x * check_abc_hit(x, rad_list, rad_dict) \
        for x in xrange(2, limit))

"""
Thoughts: After problem 125, the problems seem to be much harder. For this
problem, it was mostly about optimizing the brute force search to finish in
a reasonable amount of time. The first two optimizations were mathematical.
One, it is only necessary to check gcd(a, c) == 1 and not the other two checks
since those are actually implied. Two, if (a, b, c) are coprime then the
radical of abc is just the product of the individual radicals.

At this point, I was computing all values of a (and the related b) for each 
c and checking the properties. This approach would probably finish in minutes, 
but was not fast enough. So, I thought a little and decided to only consider
values where the radical condition could ever be met. By calculating a sorted
list of the radicals (i.e. problem 124), one can stop when the values are
no longer possible. As an additional optimization, I instead used the relation
rad(a) * rad(b) < c / rad(c) since "c" is fixed for a given check. This made
it faster to stop iterating over the sorted list.

The speed still isn't great (it takes about 10 seconds), but it is passable.
"""
if __name__ == "__main__":
    print "Example (c < 1000) (expect 12523):"
    print solve_p127(1000)
    print "Problem (c < 120000):"
    print solve_p127(120000)
        