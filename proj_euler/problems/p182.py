# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:54:12 2016

@author: mjcosta
"""

from fractions import gcd

from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import factor_int_dict

# Computes the sum of all values of e, 1 < e < phi(p, q) and gcd(e, phi) = 1
# which minimizes the number of unconcealed messages.
@timefunc
def solve_p182(phi):
    ps = factor_int_dict(phi).keys()
    # If gcd(e, phi) = 1, then e-1|2. To prevent multiples of 2, use 4 instead.
    ps.remove(2)
    ps.append(4)
    result = 0
    # Simply iterate over e, filtering by gcd.
    for e in xrange(2, phi):
        if gcd(e, phi) != 1:
            continue
        # Since 2 divides e-1, no other factor of phi should be present (or 4).
        if all((e-1) % p != 0 for p in ps):
            result += e
    return result

"""
Thoughts: This problem was rated at a reasonable difficulty, but it was simple
for me since I have seen RSA so many times. The idea is quite simple, for
m^e = m mod n, then m^(e-1) = 1 mod n = m^(ord(m)_n * d) = 1 mod n. In other
words, e-1 has to be a multiple of the multiplicative order of m mod n. The
order of elements m must divide phi(n), thus we can factor phi(n) to get
possible orders of m. Since gcd(e, phi) = 1, it must be the case that e-1 is
divisible by 2 (and 2 appears at least twice in phi = (p-1)(q-1) if p and q
are not 2). Thus, for e-1 to minimize the number of repeated numbers, it must
not have any factors from phi besides 2 (and no multiples of 2 like 4).

From here, we can simply iterate over the possible e, filter by gcd, and check
the divisibility of the factors. This gives me in the answer in 3.3 seconds,
which is fairly reasonable. While writing the code, I thought that there
might be a closed form solution to this problem, and sure enough there
was (posted in the solution thread). Overall, not a bad problem, it was made
much easier (than the rated difficulty) with my knowledge of RSA.
"""
if __name__ == "__main__":
    print solve_p182((1009-1)*(3643-1))