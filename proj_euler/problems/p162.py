# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:28:24 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Computes the number of possible hexadecimal values with at most "digits"
# digits with the digits 0, 1, and A present at least once.
@timefunc
def solve_p162(digits):
    return sum(15*16**(n-1) - 43*15**(n-1) + 41*14**(n-1) - 13**n \
        for n in xrange(3, digits+1))

"""
Thoughts: This was a tricky problem for me because I do not have that much
experience with combinatoric questions and I was trying to do it all in my
head at once. The basic idea is to use the inclusion-exclusion principle (i.e.
sum the individual terms, subtract all combinations of intersections if an
even number of terms in the intersection and add if odd number of terms). I
was able to solve it relatively quickly once I actually wrote the equations
down and worked out the pieces individually. My work is as follows: 

N = Number of possibilities for an exactly n-digit number.

Result = N(A and 0 and 1)
N(A or 0 or 1) = N(A) + N(0) + N(1) - N(A and 0) - N(A and 1) - N(0 and 1)
    + N(A and 0 and 1)
=>
N(A and 0 and 1) = N(A or 0 or 1) - N(A) - N(0) - N(1) + N(A and 0) + N(A and 1)
    + N(0 and 1)
    
    
N(X and Y) = N(X) + N(Y) - N(X or Y)

N(X) = N(All) - N(not X)

N(All) = 15*16^(n-1)

N(not 1) = 14*15^(n-1)
N(not A) = 14*15^(n-1)
N(not 0) = 15^n

N(X or Y) = N(All) - N(not X and not Y)

N(not 0 and not 1) = 14^n
N(not 0 and not A) = 14^n
N(not A and not 1) = 13*14^(n-1)

N(A or 0 or 1) = N(All) - N(not A and not 0 and not 1)
N(not A and not 0 and not 1) = 13^n

Result = (15*16^(n-1) - 13^n) + 2*(15*16^(n-1) - 14*15^(n-1)) + (15*16^(n-1) - 15^n)
    - 2*(15*16^(n-1) + 14^n) - (15*16^(n-1) - 13*14^(n-1))
= 15*16^(n-1) - 13^n - 2*14*15^(n-1) - 15^n + 2*14^n + 13*14^(n-1)
= 15*16^(n-1) - 43*15^(n-1) + 41*14^(n-1) - 13^n


Once I had this final equation, it was just a matter of summing up the values
for the different values of n (1 and 2 have no values). Predictably, it only
took 14 microseconds to get the answer.
"""
if __name__ == "__main__":
    # Note, need to convert the answer to hexadecimal, stripping the 0x prefix
    # the "L" at the end, and converting to upper case.
    print hex(solve_p162(16))[2:-1].upper()