# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 00:12:45 2015

@author: mjcosta
"""

from operator import mul
from collections import defaultdict

from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import generate_primes

# Calculates the sum of the proper divisors given n
def calc_div_sum(n, factors, mem):
    comps = []
    if n in factors:
        return None
    for k in factors:
        if (k, factors[k]) in mem:
            comps.append(mem[(k, factors[k])])
            continue
        v = 0
        p = 1
        for i in range(0,factors[k]+1):
            v += p
            p *= k
        comps.append(v)
        mem[(k, factors[k])] = v
    if len(comps) == 0:
        print comps, n, factors
    # For proper divisors need to subtract n itself
    return reduce(mul, comps) - n

# Generates all composite numbers under limit and returns a dict where
# the key is n and the value is the factor list.
def gen_composite(limit):
    result = dict()
    result[1] = defaultdict(int)
    ps = list(generate_primes(limit/2))
    def rec_composite(n, ps, fact):
        p = ps[0]
        curr = n * p
        i = 1
        while curr <= limit:
            fact[curr] = fact[n].copy()
            fact[curr][p] = i
            if len(ps) > 1:
                for j in xrange(len(ps)-1):
                    if curr * ps[j+1] > limit:
                        break
                    rec_composite(curr, ps[j+1:], fact)
            i += 1
            curr *= p
    for i in xrange(len(ps)):
        rec_composite(1, ps[i:], result)
    return result

# Create a lookup table of values less than the limit
def calc_sum_table(limit):
    i = 2
    divsum = dict()
    mem = dict()
    print "Generating composites"
    comps = gen_composite(limit)
    print "Calc sum"
    while i <= limit:
        if i in comps:
            t = calc_div_sum(i, comps[i], mem)
            if t is not None and t <= limit:
                divsum[i] = t
        i += 1
    return divsum

# Calculates a list of chains given a table of values
def calc_chains(table):    
    chains = dict()
    for k in table:
        c = set()
        c.add(k)
        curr = table[k]
        while curr not in c:
            if curr in chains:
                # Entered a cycle that k is not part of
                if k not in chains[curr]:
                    break
                # Seen this number before and it is a part of the cycle
                else:
                    c = set(chains[curr])
                    curr = k
                    break
            c.add(curr)
            if curr in table:
                curr = table[curr]
        if curr == k:
            chains[k] = c
    return chains

@timefunc
def solve_p95(limit):
    divsum = calc_sum_table(limit)
    print "Calculating chains"
    chains = calc_chains(divsum)
    longest_k = max(chains, key=lambda x: len(chains[x]))
    result = min(chains[longest_k])
    return result

"""
Thoughts: In the end I simply brute forced this problem. I generated all the
composite numbers less than 1 million by generating all combinations of primes
with products less than 1 million. Then given the prime factorization, I
simply calculate the sum of the proper divisors which has a well defined
formula and calculated the chains. Took 140s.

Looking at the answers posted on the forum, other people just used a modified
sieve of eratosthenes which was a lot faster and used less memory. I think
I was slightly tricked by the formula, but I might also be too used to thinking
in high level concepts. 
"""
if __name__ == "__main__":
    limit = int(1e6)
    result = solve_p95(limit)
    print result