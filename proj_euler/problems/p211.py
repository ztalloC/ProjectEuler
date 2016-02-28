# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:42:10 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
from proj_euler.utils.exponent import perfect_square

def sieve_square_sums(n):
    a = [1] * (n+1) # Add a zero value to simplify indexing.
    for i in xrange(2, n+1):
        # A value that hasn't been visited before is a prime.
        if a[i] == 1:
            power = i
            psum = 1
            # Build up the sums of the multiples of prime powers.
            while power <= n:
                nsum = psum + power * power
                for j in xrange(power, n+1, power):
                    a[j] = (a[j] / psum) * nsum
                psum += power * power
                power *= i
    return a

@timefunc
def solve_p211(limit):
    square_sums = sieve_square_sums(limit)
    return sum(i for i, v in enumerate(square_sums) if perfect_square(v))

"""
Thoughts: I just brute forced this problem. Given n = p_1^e_1 * p_2^e_2 * ...,
o_2(n) = (1 + p_1^2 + p_1^4 + ... + p_1^(e_1*2)) * (1 + p_2^2 + ... + p_2^(e_2*2)) * ...
So, using a simple sieve, one can compute primes and multiply in the sum of
prime powers squared for a given prime. Then it's just a matter of summing the
perfect squares. Originally I wanted to precompute the squares and just use
a set, but the maximum value is too large for this, so I just used my fast
perfect square checker. 

The performance is not that great, taking 221 seconds to finish. As always,
sieving code is a lot more efficient in lower level languages like C/C++, so
that's one area of improvement. Most of the time is actually spent doing the
perfect square checks, so that's another area that can be improved. Besides the
slow time, it also uses a fair amount of memory to store 64 million values
(again since python vs lower level language), but this approach will always use
a decent chunk of memory. There are strategies where one can evaluate windows
of the sieve (needing sqrt(N) memory), but I'm too lazy for this problem. One
could also use multi-threading, but again it's not worth it for this problem.

As an aside, it seems that many solutions in the problem thread were similar to
my approach, some taking much longer than mine. Thus, the performance can't
be considered a disaster. There is a mathematical approach that allows for
a much faster solution, but it's not immediately obvious without a mathematical
background.
"""
if __name__ == "__main__":
    print solve_p211(64*10**6)
