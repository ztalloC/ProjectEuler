# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:26:52 2016

@author: mjcosta
"""

import math

from proj_euler.utils.timing import timefunc

# An infinite generator of the recursive sequence.
def gen_sequence(init=-1):
    f = lambda x: math.floor(2**(30.403243784-x*x))/(10**9)
    while True:
        yield init
        init = f(init)
        
# Finds a cycle in the recursive generator.
def find_cycle():
    values = []
    index_map = dict()
    # Keep track of what we have seen until we have seen something twice.
    for i, v in enumerate(gen_sequence()):
        if v in index_map:
            break
        index_map[v] = i
        values.append(v)
    # The cycle is a certain offset from the initial position and has a length.
    start_i = index_map[v]
    return start_i, i - start_i, values[start_i:] 

@timefunc
def solve_p197(n):
    # Find the cycle parameters.
    start_i, length, values = find_cycle()
    # Figure out u_n and u_n+1 from these.
    cycle_n = (n - start_i) % length
    return values[cycle_n] + values[(cycle_n + 1) % length]

"""
Thoughts: My initial reaction to this problem was that there was no way that
we had to do 10^12 exponentiations. Additionally, unless the value given was
special, there would inevitably be a point where a cycle would appear because
of the floor. So, I followed my gut reaction and found the cycle. The cycle
could be represented as an index from the starting point + the values of the
cycle. Then, I simply mapped 10^12 to a position in the cycle and computed the
result.

The cycle started at index 516, so I did not need to look for very long. The
code took < 1 ms to run since it needed to check so few values. As I found
in previous problems, one needs to be careful when using 1e9 vs 10**9, as it 
could cause an error to propagate (I did not try 1e9). 
"""    
if __name__ == "__main__":
    print solve_p197(10**12)