# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:15:17 2015

@author: mjcosta
"""

import itertools

from proj_euler.utils.timing import timefunc

# Given a tuple of numbers, returns a set where 6 and 9 are both in the set
# if either one is available in the original tuple
def convert_six_nine_set(combo):
    c = set(combo)
    if 6 in c:
        c.add(9)
    elif 9 in c:
        c.add(6)
    return c

@timefunc
def cube_digit_pairs():
    # Get the digits to choose from, 7 is not needed but it contributes
    # to the count nonetheless
    digits = range(10)
    # Get all the square numbers, fill with a zero if needed
    squares = [str(x*x).zfill(2) for x in range(1,10)]
    # Convert the strings to lists of integers
    squares = [[int(y) for y in list(x)] for x in squares]
    # Only need to keep a count
    result = 0
    # Generate all viable combinations for both dice
    for combo1 in itertools.combinations(digits, 6):
        # Convert to sets and add 6/9 if the other is available
        combo1 = convert_six_nine_set(combo1)
        for combo2 in itertools.combinations(digits, 6):
            combo2 = convert_six_nine_set(combo2)
            is_viable = True
            for square in squares:
                if not ((square[0] in combo1 and square[1] in combo2) or
                    (square[1] in combo1 and square[0] in combo2)):
                        is_viable = False
                        break
            if is_viable:
                result += 1
    # Divide by two since we have duplicates of each order
    return result/2

"""
Thoughts: Given the difficulty rating of the problem, I'm disappointed with
this problem. Using itertools.combinations, it was just a matter of checking
the combinations, I guess it might be more difficult in other languages but
the algorithm for generating combinations is well known. As a side note, I
did mess up once because I excluded 7s from the count (since 7 appears in
no square number), but they do in fact contribute to the count. 
"""
if __name__ == "__main__":
    # Simply perform the computation and time it
    result = cube_digit_pairs()
    # Print the results
    print "The answer is: %d" % (result)