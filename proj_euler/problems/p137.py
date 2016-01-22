# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 07:48:53 2016

@author: mjcosta
"""

from proj_euler.utils.fibo import fibo_gen
from proj_euler.utils.timing import timefunc

# Computes the num-th (1 based indexing) Fibonacci golden nugget.
# This code is a little more verbose than it needs to be (can be done with
# one liner), but this makes it easy to see the computation and print the
# intermediate values if desired.
@timefunc
def solve_p137(num, verbose = True):
    fibs = fibo_gen()
    # Skip the first value
    next(fibs)
    result = None
    for i in xrange(num):
        # Just the product of each consecutive (non-overlapping) pair of fibos.
        result = next(fibs) * next(fibs)
        if verbose:
            print (i+1), result
    return result

"""
Thoughts: This was definitely an interesting problem and was all about math
rather than coding efficiently. The first observation is that the sum of the
infinite fibonacci series can be represented as A_F(x) = x/(1 - x - x^2) from
http://math.stackexchange.com/questions/114800/infinite-series-fibonacci-2n.

Solving this equation for x, we get x = -(+/-sqrt(5y^2 + 2y + 1) + y + 1)/2y
where y = A_F(x) and we use the negative solution in the "+/-". From this
equation, the only time x is a rational number is if 5y^2 + 2y + 1 is a perfect
square. This is useful, but not good enough as the values are quite far apart,
so we can't brute force the solution. I tried brute forcing it and the first
10 values I got were:

1 2
2 15
3 104
4 714
5 4895
6 33552
7 229970
8 1576239
9 10803704
10 74049690

After that, it was too slow, so I just aborted the program. However, looking at
these numbers gave me the feeling that it was somehow related to the Fibonacci
sequence (the 2 and 15 were most suspicious). Consulting an online Fibonacci
sequence list (with the factors), I found that the sequence above is formed
from products of Fibonacci numbers. Specifically, 2 = F(2)F(3), 15 = F(4)F(5),
104 = F(6)F(7), ... up to the 10th golden nugget. Using this pattern, I was
able to very quickly come up with the 15th golden nugget in < 1 ms.
"""
if __name__ == "__main__":
    print "Example (n = 10) (expect 74049690):"
    print solve_p137(10, verbose = False)
    print "Problem (n = 15):"
    print solve_p137(15)