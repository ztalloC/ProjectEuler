# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:47:48 2016

@author: mjcosta
"""

from math import ceil

from proj_euler.utils.timing import timefunc

# Returns the unique positive integer whose square has the form 
# "1_2_3_4_5_6_7_8_9_0".
@timefunc
def solve_p206():
    sq = "1_2_3_4_5_6_7_8_9_0"
    sq_digits = [(i, x) for (i, x) in enumerate(sq) if x != '_']
    # Get the bounds of possible values.
    i = int(sq.replace('_', '0'))**0.5
    # Small optimization, only consider multiples of 10.
    i = int(10 * ceil(float(i)/10))
    # Furthermore, n/10 must end in 3 or 7 because the third to last digit
    # in the square is 9 (the last blank must be 0).
    while i % 100 != 70 and i % 70 != 30:
        i += 10
    upper = int(sq.replace('_', '9'))**0.5
    while i < upper:
        # Compute the string and check against the digits.
        vs = str(i*i)
        if all(vs[i] == x for (i, x) in sq_digits):
            return i
        # Only consider values ending with 30 or 70.
        if i % 100 == 30:
            i += 40
        else:
            i += 60
    return None

"""
Thoughts: Quick question I solved because I was bored. This is actually the
easiest problem outside the first 100 problems. The problem is a very
straightforward brute force. One can speed up the search by observing that
the square ends with 0, so the value must be a multiple of 10. Also, the
second to last known digit is a 9, so the value n/10 must end in 3 or 7
(the blank in between must be 0 since n is a multiple of 10). 

The code takes about 6 seconds to run. It's not really worth doing more 
to speed up the code. I originally did it because I thought it would give me
the decimator achievement, but I guess I need to solve 200 (which looks like
a pain).
"""
if __name__ == "__main__":
    print solve_p206()
    