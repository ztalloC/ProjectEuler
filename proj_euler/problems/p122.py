# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:29:15 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Given a target exponent and the previous chains, computes all possible
# chains that can generate the target exponent. 
def compute_all_chains(target, prev_chains):
    candidates = []
    for chain_list in prev_chains:
        for chain in chain_list:
            for value in chain:
                # Need two elements that sum to the target.
                if value <= target/2 and (target - value) in chain:
                    candidates.append(chain.union([target]))
    return candidates

# Given a target and a list of previous chains, computes the optimal chain(s)
# for the given target exponent.    
def compute_optimal_chains(target, prev_chains):
    # Compute all possible chains that satisfy the given target.
    all_chains = compute_all_chains(target, prev_chains)
    # Get all chains with minimum length.
    min_length = len(min(all_chains, key=len))
    return filter(lambda x: len(x) == min_length, all_chains)
    
# Computes the sum of the optimal chains for a given range.
@timefunc
def solve_p122(high):
    # Chains are lists of sets containing the exponents comprising the largest 
    # value. We store lists of sets instead of sets since there may be more
    # than one optimal chain for a given exponent (which may be useful).
    chains = [[set([1])]]
    for k in xrange(2, high+1):
        new_chains = compute_optimal_chains(k, chains)
        chains.append(new_chains)
    # The result is the sum of the chain lengths (minus one since we do not
    # need to compute 1).
    return sum(len(x[0])-1 for x in chains)

"""
Thoughts: Fairly tricky problem. I searched how to find optimal exponents and
found the wikipedia page for "Addition-chain exponentiation". It seems that
this is actually an NP-complete problem, though for smaller values it is
reasonable to brute force it. It's actually quite a useful concept since it
saves computation for expensive multiplications (such as matrices) if the
exponent is known in advance (and the addition chain is pre-computed).

As for how I solved the problem, it is really just checking all possible chains
and returning the minimum. This took some thought on how to do in a reasonably
efficient manner, but wasn't that bad. The speed was about 1 second, so it
wasn't terrible performance-wise either.
"""
if __name__ == "__main__":
    print solve_p122(200)