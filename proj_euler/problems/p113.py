# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:15:04 2016

@author: mjcosta
"""

from collections import defaultdict

from proj_euler.utils.timing import timefunc

# Calculates the number of decreasing values with at most a number of digits.
def calculate_decreasing(digits):
    stats = defaultdict(int)
    # Initialise all 1 digit values to 1.
    for v in range(10):
        stats[(1, v)] = 1
    # Use all the previous digit stats to compute the current.
    for d in range(2, digits+1):
        for v in range(10):
            # Note: for v = 0, v - 1 doesn't exist, so that component is 0.
            stats[(d, v)] = stats[(d-1, v)] + stats[(d, v-1)]
    # Return the sum of all values. 
    result = 0
    for (d, v) in stats:
        # Exclude values starting with 0, except the one digit value.
        if d == 1 or v != 0:
            result += stats[(d, v)]
    return result

# Calculates the number of "non-bouncy" values below an amount of digits.
@timefunc 
def calculate_non_bouncy(digits):
    # Calculate the decreasing number of values
    decrease = calculate_decreasing(digits)
    # Could compute both values at once (in the previous call), but calling
    # separately makes the code simpler.
    diff = calculate_decreasing(digits - 1)
    # There are slightly less increasing values than decreasing values. To
    # calculate the non-bouncy values, we can multiply the decreasing by two
    # and subtract the shared values (10 for 1 digit numbers and 9 per each
    # additional digits) and subtract the missing values. The amount of missing
    # values is actually the number of decreasing values for one less digit,
    # this is because 0 is used in decreasing but not in increasing (and the
    # difference propagates in a way similar to decreasing values).
    return 2 * decrease - 10 - (digits - 1) * 9 - diff

"""
Thoughts: Overall the problem was easy, but there was a gotcha to it. In my
case, I had assumed that the number of increasing and decreasing values was
the same (and I could simply multiply decreasing by 2). Afer simply iterating
through values for 100 and 1000, I realised this was not the case and adjusted
accordingly. The code is quite fast (< 1 ms), it could be faster but I wanted
to make the code simple. There may be a closed-form equation for it, but it's
not really that important for now.
"""
if __name__ == "__main__":
    print "Example (n = 10^6) (should equal 12951):"
    print calculate_non_bouncy(6)
    print "Example (n = 10^10) (should equal 277032):"
    print calculate_non_bouncy(10)
    print "Problem (n = 10^100):"
    print calculate_non_bouncy(100)