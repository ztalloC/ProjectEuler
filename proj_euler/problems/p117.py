# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:23:55 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc
from proj_euler.problems.p116 import tile_combos

# Computes the total number of ways a row can be tiled with different lengths.
@timefunc
def solve_p117(length, color_lens):
    return tile_combos(length, color_lens)
    
"""
Thoughts: Trivial to solve since I solved both 116 and 117 at the same time.
"""
if __name__ == "__main__":
    print "Example (5, [2, 3, 4]) (Expect 15):"
    print solve_p117(5, [2, 3, 4])
    print "Problem (50, [2, 3, 4]):"
    print solve_p117(50, [2, 3, 4])