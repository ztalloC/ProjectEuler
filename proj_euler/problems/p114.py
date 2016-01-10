# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 21:23:14 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Computes the number of block combinations given a minimum block length,
# the number of spaces available, and a dictionary to memoize results. It would
# be very simple to do bottom-up (non-recursively), but this makes it easier
# to re-use results while separating the recurrence relation from a specific
# instance of the problem. 
def block_combos(block_len, length, mem):
    # Use the stored result if available.
    if length in mem:
        return mem[length]
    # Not enough blocks, so all must be unset.
    if length < block_len:
        result = 1
    else:
        # Can either leave the new block unset and use the previous solution.
        result = block_combos(block_len, length - 1, mem)
        # Or we can set it along with other blocks, then an unset block and
        # any combination of previous lengths.
        for remain in xrange(length - block_len):
            result += block_combos(block_len, remain, mem)
        # Also, we can set everything as a block, which is a new possibility.
        result += 1
    mem[length] = result
    return result
    
@timefunc
def solve_p114(min_len, spaces):
    return block_combos(min_len, spaces, dict())

"""
Fairly straightforward problem, I over thought it a little bit though. This is
just a dynamic programming problem, the challenge is in finding the exact
decomposition. My solution was to consider the possibility where a new square
was empty or if it was filled. If it is filled, one must take into account the
minimum length as well as multiple lengths.

The part I overthought was the statement that any two red blocks must be
separated by at least one black square. I had realized that the black square
does not actually matter since if two blocks are separated by zero black
squares, then it is actually one big block. However, this was meant as a hint
for the recurrence relation, where you can use the unset block to separate
the possibilities into cases and prevent double counting. After realizing that
I could use the unset block to my advantage, it was easy to finish.

The overall run time is good (< 1 ms), which is expected. I wrote my code such
that the next problem could be solved by re-using this code. 
"""
if __name__ == "__main__":
    print "Example (n = 7) (Expect 17):"
    print solve_p114(3, 7)
    print "Problem (n = 50):"
    print solve_p114(3, 50)