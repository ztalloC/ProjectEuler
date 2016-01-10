# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:44:14 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Given a number, computes the sum of its digits.
def sum_digits(v):
    return sum(int(x) for x in str(v))

# Finds a given value in the digital power sequence. Searches by raising
# exponents to a certain power (until it passes a threshold) and trying
# different bases. At the end, simply indexes all the results that it
# received (may need to adjust parameters).
@timefunc
def solve_p119(index, max_base, max_value):
    matches = []
    for i in xrange(2, max_base+1):
        current = i
        while current < max_value:
            # Check if the sum of the digits equals the base but exclude
            # single digit numbers.
            if sum_digits(current) == i and current >= 10:
                matches.append(current)
            current *= i
    # After generating them all, simply sort and index the results.
    if index < len(matches):
        matches.sort()
        return matches[index]
    else:
        print "Not enough values found!"
        return None

"""
Thoughts: Not a bad problem. I originally tried a brute force solution by
generating all values and checking the property. I was able to get some results
with some optimization, but after index 13, it was really slow. Then, I tried
the approach that the other recent problems used (try to generate only the
possibly relevant values based on some constraint). This worked quite well and
I was able to solve the problem quickly (27 ms).
"""         
if __name__ == "__main__":
    # Note: indices displayed are one-based, actual are zero-based.
    print "Example (n = 2) (Expect 512):"
    print solve_p119(1, 10, 1e6)
    print "Example (n = 10) (Expect 614656):"
    print solve_p119(9, 50, 1e9)
    print "Problem (n = 30):"
    print solve_p119(29, 1000, 1e20)