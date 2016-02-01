# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:13:22 2016

@author: mjcosta
"""

from collections import defaultdict
from itertools import combinations

from proj_euler.utils.timing import timefunc

# Computes all pairs such that x^2 + xy + y^2 = z^2 for some z with integer
# solutions. Returns a dictionary of sets where the key is less than all of
# the values in the set.
def precompute_pairs(limit):
    matches = defaultdict(set)
    m = 1
    fx = lambda m, n: n*n + 2*m*n
    fy = lambda m, n: m*m - n*n
    # The value x + y must be less than the limit, it's possible that x + y + z
    # is above the limit, but don't worry about it here.
    while fx(m, 0) + fy(m, 0) < limit:
        # y > 0 implies n < m. 
        for n in xrange(1, m):
            x, y = fx(m, n), fy(m, n)
            small, big = min(x, y), max(x, y)
            k = 1
            while k*(small+big) < limit:
                matches[small*k].add(big*k)
                k += 1                
        m += 1
    return matches

# Computes the sum of all unique p + q + r < limit for Toricelli triangles.
@timefunc
def solve_p143(limit):
    # Keep track of all unique sums p + q + r.
    sums = set()
    pairs = precompute_pairs(limit)
    # Find 3 pairs that creates the triple (p, q, r).
    for p in pairs:
        # All valid triples must have two pairs containing (p, q) and (p, r),
        # so just check if (q, r) is a triple.
        for (q, r) in combinations(pairs[p], 2):
            small, big = min(q, r), max(q, r)
            if small in pairs and big in pairs[small]:
                sums.add(p + q + r) 
    return sum(filter(lambda x: x < limit, sums))

"""
Thoughts: Tough problem that took me a while to solve (also my hardest problem 
solved at the time of writing this). It took a reasonable amount of math to
get an efficient solution to the problem.

The first useful idea I found while searching for properties of Fermat points.
Let F be the Fermat point and and ABC be a triangle with all interior angles
less than 120 degrees. Then, the angles AFB, AFC, and BFC are all equal to 120
degrees (proved at http://jwilson.coe.uga.edu/EMAT6680Fa07/Shih/AS06/WU06.htm).
This property is very useful as we can use the cosine law to relate the size
of (p, q, r) with (a, b, c). The general cosine law is:

c^2 = a^2 + b^2 - 2*a*b*cos(alpha)

Since the angle (alpha) is known to be 120 degrees, we have the equations:

a^2 = q^2 + r^2 + qr
b^2 = q^2 + p^2 + pq
c^2 = p^2 + r^2 + pr

So, if we can find integer solutions to the Diophantine equations above, then
the triangle is a Toricelli triangle. Thus, we have a general Diophantine
equation x^2 + xy + y^2 = z^2. Searching online, I found two methods of finding
solutions efficiently. One is to convert the equation to an ellipse equation
(divide by z^2) and find all rational solutions to the equation. The second
method is to use equation 9 in this paper: 
http://www.emis.de/journals/GM/vol13nr2/andrica/andrica.pdf

I actually tried both methods and found them to be equivalent, so I just used
the second method. 

After coming up with all relevant pairs (x, y), it was just a matter of finding
all pairs (p, q), (p, r), and (q, r) to form the triple (p, q, and r). To save
space, I stored pairs in the format (a, b) where a < b. The solution worked 
quite well, only taking around 400 milliseconds to run.
"""
if __name__ == "__main__":
    print solve_p143(120000)