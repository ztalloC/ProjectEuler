# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:19:15 2016

@author: mjcosta
"""

from proj_euler.problems.p135 import solve_p135

"""
Thoughts: I just reused the code I had for 135 with different parameters.
Originally I tried writing a modified version where I only counted the
range d < x <= 2d and x = 3d, but it turns out to be necessary to consider
the range 2d < x < 3d since it invalidates some of the candidate values. The
performance isn't good (70 seconds), but if I really wanted to get the time
down, I could trivially parallelize it (in addition to other tricks).
"""
if __name__ == "__main__":
    print "Example (n < 100) (expect 25):"
    print solve_p135(100, 1)
    print "Problem (n < 50e6):"
    print solve_p135(50e6, 1)