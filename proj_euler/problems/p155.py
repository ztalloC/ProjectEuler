# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:22:13 2016

@author: mjcosta
"""

from collections import defaultdict
from itertools import product
from fractions import gcd

from proj_euler.utils.timing import timefunc

# Computes the number of distinct capacitances using up to n capacitors.
def gen_capacitances(limit):
    # Keep track of capacitances using exactly n capacitors.
    cs = defaultdict(set)
    cs[1].add((1,1))
    # Also keep track of all combos overall.
    all_cs = set(cs[1])
    for k in xrange(2, limit+1):
        # For k capacitors, we can combine combos from i and k-i combos.
        i = 1
        while i <= k-i:
            # Distinct capacitances are represented as fractions of the start
            # capacitance. One could use the Fraction class, but it is faster
            # to just use a pair and do the math yourself.
            for (a, b), (c, d) in product(cs[i], cs[k-i]):
                # Given two fractions a/b and c/d, parallel is the sum or
                # (a*d + b*c)/b*d (normalized by gcd). Series is
                # a*c/(b*c + a*d) (normalized by gcd).
                comb = a*d + b*c
                nprod = a*c
                dprod = b*d
                ngcd = gcd(comb, nprod)
                dgcd = gcd(comb, dprod)
                # Parallel
                cs[k].add((comb / dgcd,  dprod / dgcd))
                # Series
                cs[k].add((nprod / ngcd, comb / ngcd))
            i += 1
        all_cs.update(cs[k])
    return len(all_cs)

@timefunc
def solve_p155(n):
    return gen_capacitances(n)

"""
Thoughts: Looking at the problem is slightly intimidating, but it actually is
not "that" hard. The idea is to build up combinations for k capacitors using
previous combinations. One can combine within (1, k-1), (2, k-2), ... as either
series or parallel circuits. One optimization I found from searching is that
it is faster to use pairs to represent fractions than to use the built-in 
Fraction class. I did not time a full run using the Fraction class as I stopped
it after several minutes.

As for performance, it takes 30 seconds to complete, which is on the high
side compared to usual solutions. However, from the solutions thread, there
was no super efficient method to do it, so this is actually quite reasonable.
The code uses a fair amount of memory (several hundred megabytes), so that is
also something to consider.
"""
if __name__ == "__main__":
    print "Example (n = 3) (expect 7):"
    print solve_p155(3)
    print "Problem (n = 18):"
    print solve_p155(18)