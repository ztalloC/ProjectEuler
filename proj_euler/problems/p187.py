# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:15:55 2016

@author: mjcosta
"""

from bisect import bisect_right

from proj_euler.utils.primes import generate_primes
from proj_euler.utils.timing import timefunc

@timefunc
def solve_p187(limit, verbose=True):
    if verbose:
        print "Generating primes..."
    primes = list(generate_primes(limit/2))
    if verbose:
        print "Computing value..."
    hi = len(primes)
    result = 0
    i = 0
    while hi > 0 and i < len(primes):
        hi = bisect_right(primes, limit/primes[i], lo=i, hi=hi)
        result += hi - i
        i += 1
    return result

"""
Thoughts: Easy problem. I skipped around to 187 because I was just looking
for something easy. The problems after 150 are much harder and I kind of want
to take a break from project euler (at least from harder problems) since I
want more practical experience. 

Anyway, the problem is pretty simple, just generate all primes under half the
limit, and count the number of prime pairs (x, y) where x*y < limit. I learned
of the bisect module which is handy for doing binary range searches on sorted 
lists (I know how to write it but I don't really want to). 

Besides that, I swapped out the algorithm for generate_primes with a fresh 
sieve of Eratosthenes. I profiled the times and sympy's algorithm is an order 
of magnitude slower than the replacement algorithm (which could be better). 
This doesn't really come as a surprise since sympy's algorithms for prime 
factorization are also slow (I just can't be bothered to rewrite my quadratic
sieve). For now, I have left the other prime generating functions the same
since sympy's interface is very convenient as it lets you create an infinite
generator (but this uses a growing Eratosthenes sieve, so the memory usage
isn't great, but okay if you don't want to set an upper bound and if you think
the actual upper bound is reasonable).

The performance is okay, taking around 10 seconds. Most of that time is in the
prime generation function (again, I am aware of better algorithms) and could
also be put into a lower level language.
"""
if __name__ == "__main__":
    print "Example (< 30) (expect 10):"
    print solve_p187(30, False)
    print "Problem (< 1e8):"
    print solve_p187(1e8)