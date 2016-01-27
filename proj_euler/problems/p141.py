# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:05:18 2016

@author: mjcosta
"""

from fractions import gcd

from proj_euler.utils.timing import timefunc

@timefunc
def solve_p141(limit):
    result = set()
    # Precompute squares for fast checking.
    squares = set(x*x for x in xrange(1, int(limit**0.5)))
    # f(x, y, z) = x^3yz^2 + y^2z = yz(x^3z + y)
    f = lambda x, y, z: y * z * (x**3 * z + y)
    # x^3 term implies x <= limit^(1/3).
    xlimit = round(limit**(1.0/3)) 
    for x in xrange(2, int(xlimit+1)):
        # y < x, as a very minor optimization, don't iterate over even y
        # if x is even.
        if x % 2 == 0:
            ygen = xrange(1, x, 2)
        else:
            ygen = xrange(1, x)
        for y in ygen:
            if gcd(x, y) != 1:
                continue
            z = 1
            v = f(x, y, z)
            while v < limit:
                if v in squares:
                    result.add(v)
                z += 1
                v = f(x, y, z)
    return sum(result)

"""
Thoughts: Definitely a tricky problem, which is unsurprising since it is the
hardest problem I have solved so far (according to the site). It was hard
to find a direction initially, but it was relatively straightforward after
figuring out the equation for progressive numbers. 

For n = qd + r, clearly r < d and since d < sqrt(n), then d < q. So, we know
that d = rk and q = dk = rk^2 where k is the common ratio. Then, we can 
substitute n = r^2k^3 + r. Since k is a rational number, it can be expressed
as k = x/y where gcd(x, y) = 1. Since q = rk^2 = rx^2/y^2, x and y are coprime,
and q is an integer, y^2 must divide r, so r = zy^2. Thus, we can substitute
to get n = x^3yz^2 + y^2z, where n is a perfect square.

At this point, we can simply iterate over the possible values of x, y, and z
and test if n is a perfect square. The initial version took around 55 seconds
and with a few trivial optimizations, it takes about 28 seconds. The
performance could be better, but is about average compared to other solutions
(in the solutions thread). I could (and probably should) use Farey sequences
to generate coprimes instead of iterating over all pairs and filtering by gcd.
"""
if __name__ == "__main__":
    print "Example (< 1e5) (expect 124657):"
    print solve_p141(1e5)
    print "Problem (< 1e12):"
    print solve_p141(1e12)