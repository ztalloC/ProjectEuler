# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:57:32 2016

@author: mjcosta
"""

from collections import defaultdict

from proj_euler.utils.primes import test_primality
from proj_euler.utils.primes import generate_primes
from proj_euler.utils.timing import timefunc

# Generates a dictionary of sets, restricting the set of values mod p if
# a value is to be prime. xs contains a list of values where n^2+x is desired
# to be prime. 
def compute_prime_mods(xs):
    # All primes less than the max value are relevant.
    ps = generate_primes(max(xs))
    mods = defaultdict(set)
    for p in ps:
        # Compute all the xs mod p.
        xsp = set(x % p for x in xs)
        # A value can be added if does not become 0 mod p for some x.
        for i in xrange(p):
            if (p - i*i) % p not in xsp:
                mods[p].add(i)
    return mods        

# Tests that all values of the form n^2 + x are consecutive primes.
def test_consecutive_primes(n2, xs):
    # First the values themselves should be primes.
    if not all(test_primality(n2 + x) for x in xs):
        return False
    # There should be no other primes besides those specified in x.
    max_x = max(xs)
    for x in xrange(xs[0] + 2, max_x, 2):
        if x in xs:
            continue
        if test_primality(n2 + x):
            return False
    return True

# Computes the sum of all n below limit where n^2+x for each x in [1, 3, 7, 9,
# 13, 27].
@timefunc
def solve_p146(limit, verbose=True):
    result = 0
    xs = [1, 3, 7, 9, 13, 27]
    pmods = compute_prime_mods(xs)
    # Start at 10 and only consider multiples of 10.
    for n in xrange(10, int(limit), 10):
        # All n must be certain modulos mod p.
        if not all((n % p) in pmods[p] for p in pmods):
            continue
        n2 = n * n
        # If all are prime, then add to the result.
        if test_consecutive_primes(n2, xs):
            result += n
            if verbose:
                print n
    return result

"""
Thoughts: Not that hard of a problem. I originally tried to brute force it by
incrementing n and doing the primality tests, but that was too slow. I then
looked at n^2 + 1 to see if I could find when n^2 + 1 is prime. However, this
is actually an unsolved problem. 

But, I noticed that for n^2 + 1 mod 2, that n^2 + 1 = 0 mod 2 if n = 1 mod p, 
thus n = 0 mod p (cutting the search space in half). I looked through my brute 
force partial output and saw that all the matching n were multiples of 10. So,
I computed all possible values of n^2 mod 5 and looked at n^2+x mod 5 for each 
of the x in [1, 3, 7, 9, 13, 27] and found that except for n = 0 mod 5, all
the other n's result in n^2 + x = 0 mod 5 for at least one x. I then proceeded
to test p = 3, which restricted n to n = 1 or 2 mod 3. For larger n, it was
quite tedious to compute the valid moduli, so I wrote a function that
calculates the valid n. 

Then, it was just a matter of iterating over n, checking the moduli, and then
testing for primality for each x in n^2 + x. This was fine, taking around
30 seconds to run. However, in my initial version I got the wrong answer. I
was only testing if the given values were prime and not if they were actually
consecutive primes. While we can ignore n = 2 (where the congruence test is
invalid since n^2+x mod p = 0 because n^2+x = p), n = 144774340 was a value
of n where all n^2 + x were primes but not consecutive primes. Adding the
additional test, I got the correct answer as expected.
"""
if __name__ == "__main__":
    print "Example (< 1e6) (expect 1242490):"
    print solve_p146(1e6)
    print "Problem (< 150e6):"
    print solve_p146(150e6)