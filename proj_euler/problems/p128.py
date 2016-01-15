# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:11:30 2016

@author: mjcosta
"""

from collections import namedtuple

from proj_euler.utils.timing import timefunc
from proj_euler.utils.primes import test_primality
from proj_euler.utils.memoize import memoize

Hexagon = namedtuple('Hexagon', 'number, neighbors')

# Returns a list containing the values for a given layer, requires the starting
# point (based from the previous layer or 1 if the first layer).
def generate_layer(index, start = 1):
    return xrange(start, start + index * 6)

# Given an index, wraps it to fit within a given bound.
def wrap_index(x, length):
    while x < 0:
        x += length
    while x >= length:
        x -= length
    return x

# Given the previous layer, the current layer, and the next layer, returns
# a generator of Hexagons describing the neighbor relations.
def get_neighbors(prev_layer, current_layer, next_layer):
    # For the first layer (which has no previous layer, just return the second
    # layer as the neighbors).
    if current_layer == [1]:
        yield Hexagon(1, range(2, 8))
        return
    # Need to calculate the "length" of each side (to determine corners)
    corner_len = len(current_layer)/6
    length = len(current_layer)
    # Only consider possible tuples.
    possible = [(0, current_layer[0]), (length-1, current_layer[-1])]
    for i, v in possible:
        cur_vals = [current_layer[i - 1], current_layer[wrap_index(i + 1, length)]] 
        # If on a corner, then 1 from previous, 2 from current, 3 from next.
        if i % corner_len == 0:
            prev_vals = [prev_layer[i * (corner_len - 1)/corner_len]]
            next_i = i * (corner_len + 1)/corner_len
            # Since index may be negative, can't just use a slice.
            next_vals = [next_layer[wrap_index(x, length + 6)] for x in 
                range(next_i-1, next_i+2)]
        # Not on corner, 2 from previous, 2 from current, 2 from next.
        else:
            corner_num = i / corner_len
            # Do separately because of slice behavior.
            prev_vals = [prev_layer[i - corner_num - 1], 
                         prev_layer[wrap_index(i - corner_num, length - 6)]]
            next_vals = [next_layer[i + corner_num],
                         next_layer[wrap_index(i + corner_num + 1, length + 6)]]
        yield Hexagon(v, prev_vals + cur_vals + next_vals)

# An infinite generator of hexagons.
def generate_hexagons():
    prev_layer = None
    curr_layer = [1]
    layer = 0
    while True:
        # Generate the next layer.
        next_layer = generate_layer(layer + 1, max(curr_layer) + 1)
        # Output all the hexagons in the current layer.
        for hexagon in get_neighbors(prev_layer, curr_layer, next_layer):
            yield hexagon
        # Prepare for the next layer
        prev_layer = curr_layer
        curr_layer = next_layer
        layer += 1

@memoize
def is_prime(x):
    return test_primality(x)


# Computes the n-th value defined by the sequence PD(x) = 3.     
@timefunc
def solve_p128(n):
    count = 0
    for hexagon in generate_hexagons():
        diffs = [abs(x - hexagon.number) for x in hexagon.neighbors]
        num_primes = sum(1 for x in diffs if is_prime(x))
        if num_primes == 3:
            count += 1
            if count == n:
                return hexagon.number

"""
Thoughts: The problem was a little interesting and somewhat difficult. I
initially thought that I could generate all values and simply check the
differences. One can generate the neighbors of a given row if one also has
the previous and the next rows. The code for this is a little messy (and I am
not proud of it), but it does work. However, after running my solution, I
discovered that it was finding numbers too slow at a decreasing rate.

Looking at which numbers were matching the criteria, I found that it was always
the values at the beginning and end of the row. This made sense because the
remaining numbers on the "sides" of the hexagons (not on the corners) would 
have two consecutive values from the same row. The values from the previous
and next rows could have a larger difference, but each row contributes values
of the form (v, v + 1). This means that the side hexagons can only have two
prime differences at max (since the other two can't be prime). 

I noticed in my logs that none of the corners were matching (except at the 
beginning), so I decided to just assume that they were the same as "sides" and
exclude them from consideration (if I was wrong, I could just include them
in a later run). As it turns out (looking at other's solutions after solving
the problem), this is provably true.

Therefore, for each row, I only had to consider the first and last value and
check the differences. Since I was lazy, I just kept my old code in and 
explicitly restricted my search to the first and last value. The result was
that it worked, but was slow (220 seconds). I could make it much faster and
cleaner by computing the two hexagons explicitly.
"""
if __name__ == "__main__":
    print "Example (10) (expect 271):"
    print solve_p128(10)
    print "Problem (2000):"
    print solve_p128(2000)