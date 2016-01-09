# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:36:42 2016

@author: mjcosta
"""

from itertools import combinations

from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import test_primality

# Given a digit and a hypothetical number of digits (and the total digits to
# search through), returns the count and sum of the found primes..
def test_prime_digits(value, test_digits, total_digits):
    base = [value] * total_digits
    indices = range(total_digits)
    all_counts = 0
    all_sum = 0
    # Test all combinations, swapping out digits.
    for combo in combinations(indices, test_digits):
        partial_count, partial_sum = test_positions(base[:], combo)
        all_counts += partial_count
        all_sum += partial_sum
    return all_counts, all_sum

# Given a base list number, tests all possible combinations for primality. 
def test_positions(base, swap_digits):
    # No digits left to test, simply test primality
    if len(swap_digits) == 0:
        # If 0 is in the first digit, reject it since it no longer counts.
        if base[0] == 0:
            return 0, 0
        # Convert from a list of digits to a number of values.
        val = convert_list_number(base)
        if test_primality(val):
            return 1, val
        else:
            return 0, 0
    # Test all values for the first digit, recursively try the rest.
    first = swap_digits[0]
    remain = swap_digits[1:]
    count = 0
    sum_vals = 0
    for possible in range(10):
        base[first] = possible
        partial_count, partial_sum = test_positions(base, remain)
        count += partial_count
        sum_vals += partial_sum
    return count, sum_vals
                
        
# Given a list of digits, converts back to an actual number.
def convert_list_number(digits):
    return reduce(lambda x, y: 10*x + y, digits, 0)

@timefunc
def solve_p111(num_digits, verbose=True):
    result = 0
    # Search for primes for all digits
    for digit in range(10):
        # Except for single digit primes (which we'll skip), no prime can
        # consist of all of the same digit, so start at 1.
        curr_test = 1
        # Search until we find a match (abort if we have to try all of them).
        match_count = 0
        match_sum = 0
        while curr_test < num_digits and match_count == 0:
            match_count, match_sum = test_prime_digits(digit, curr_test, 
                                                       num_digits)
            curr_test += 1
        if verbose:
            print "Digit %d, Max %d, Count %d, Sum %d" % \
                (digit, num_digits - (curr_test - 1), match_count, match_sum)
        result += match_sum
    return result

"""
Thoughts: The problem was a little easy, but overall reasonable. My initial
approach was simply to try generating the primes and gathering the statistics.
But, there were simply too many primes (even if you can obtain them efficiently
) and most of them are useless.

My second attempt was to generate all possible values for numbers with a
given number of repeated digits (testing all positions and digits) and then
test for primality. This was much more reasonable and is what I ended up
going with. The speed of this approach was quite good, as generally only one
or two digits needed to be tested, taking about 56 ms.
"""  
if __name__ == "__main__":
    print "Example (n = 4):"
    print solve_p111(4)
    print "Problem (n = 10):"
    print solve_p111(10)