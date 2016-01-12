# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:19:19 2016

@author: mjcosta
"""

from operator import mul
from itertools import combinations

from proj_euler.utils.timing import timefunc

# Computes n!
def factorial(n):
    return reduce(mul, xrange(1, n+1), 1)
    
# Given the number of turns, computes the denominator of the probability.
def disc_prob_denominator(turns):
    return factorial(turns+1)
    
# Given the number of turns, computes the probability of winning. Returns the
# value as a pair in the form (numerator, denominator).
def compute_disc_win_prob(turns):
    # Note: We compute the losing probability and then subtract from total.
    denom = disc_prob_denominator(turns)
    # Need to have at least this many reds to lose. (Over half, round up).
    min_reds = (turns+1)/2
    indices = range(turns)
    # For a given index, computes the number of red discs.
    num_red = lambda x: x+1
    numer = 0
    # Compute all possible losing configurations for each number of reds.
    for num_reds in xrange(min_reds, turns+1):
        for red_indices in combinations(indices, num_reds):
            # Compute the probability of getting reds for the given combo
            # and the rest blue (numerator of 1).
            numer+= reduce(mul, (num_red(x) for x in red_indices), 1)
    # Convert to winning probability.
    numer = denom - numer
    return (numer, denom)
    
# Computes the maximum prize fund for a game with a given amount of turns.
@timefunc
def solve_p121(turns, verbose=True):
    (n, d) = compute_disc_win_prob(turns)
    if verbose:
        print "There are %d winning outcomes out of %d" % (n, d)
    # Result is simply the expected number of games before a win, rounded down.
    return int(d/n)
    
if __name__ == "__main__":
    print "Example (n = 4) (Expect 10):"
    print solve_p121(4)
    print "Problem (n = 15):"
    print solve_p121(15)