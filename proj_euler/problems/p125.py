# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:41:07 2016

@author: mjcosta
"""

import math

from proj_euler.utils.timing import timefunc

# Returns true if a number is a palindrome, false otherwise.
def is_palindrome(x):
    s = str(x)
    low = 0
    high = len(s) - 1
    # Just use the two pointers method to check.
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True

# Counts the number of palindromes with the consecutive square sum property
# less than some value.
def count_palindromes(limit):
    # There are apparently duplicates in the result, so use a set.
    matches = set()
    # Need to consider up to the square root of the limit
    max_sq = int(math.sqrt(limit))
    # Precompute squares.
    bases = [x*x for x in xrange(1, max_sq)]
    # Check all combinations of values, avoid re-computation.
    for start in xrange(len(bases)):
        current = bases[start]
        # Note: This construction is a bit awkward, this is because the problem
        # does not allow single squares to be counted.
        for end in xrange(start+1, len(bases)):
            current += bases[end]
            if current < limit and is_palindrome(current):
                matches.add(current)
            elif current >= limit:
                break
    return sum(matches)

@timefunc
def solve_p125(limit):
    return count_palindromes(limit)

"""
Thoughts: Very easy. Obviously it would be difficult to tell if a number was
the sum of consecutive squares, so it made sense to just generate all possible
values and check for palindromes. I did make the mistake of initially assuming
that all matches were unique, but this was easy to fix.
"""
if __name__ == "__main__":
    print "Example (< 1000) (expect 4164):"
    print solve_p125(1e3)
    print "Problem (< 10^8):"
    print solve_p125(1e8)