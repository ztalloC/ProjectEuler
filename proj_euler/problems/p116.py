# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:33:21 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

def tile_combos(length, color_lens):
    mem = dict()
    color_lens = sorted(color_lens)
    # Sentinel
    mem[0] = 1
    # Add an extra tile to the right...
    for i in xrange(1, length + 1):
        # All colors too big, just leave alone.
        if i < color_lens[0]:
            combos = 1
        # At least one color can replace.
        else:
            # Can always leave the new tile as is.
            combos = mem[i - 1]
            # Try replacing colors (assuming previous are unused)
            j = 0
            while j < len(color_lens) and color_lens[j] <= i:
                combos += mem[i - color_lens[j]]
                j += 1
        mem[i] = combos
    return mem[length]

@timefunc    
# Individually computes tile combos for each color.
def solve_p116(length, color_lens):
    result = 0
    for c_len in color_lens:
        result += tile_combos(length, [c_len])
        # Tile combos includes the possibility of all black tiles, remove this.
        result -= 1
    return result
    
"""
Thoughts: Very simple, especially right after solving problem 114 + 115.
The recurrence relation is almost identical, just allow for multiple fixed
sized tiles instead. I solved problem 116 and 117 simultaneously.
"""
if __name__ == "__main__":
    print "Example (5, [2, 3, 4]) (Expect 12):"
    print solve_p116(5, [2, 3, 4])
    print "Problem (50, [2, 3, 4]):"
    print solve_p116(50, [2, 3, 4])