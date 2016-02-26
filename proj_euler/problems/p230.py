# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:32:31 2016

@author: mjcosta
"""

from proj_euler.utils.fibo import fibo_gen
from proj_euler.utils.timing import timefunc

def backtrace(n, a, b):
    fgen = fibo_gen(a, b)
    fibs = []
    curr = 0
    while curr < n:
        curr = next(fgen)
        fibs.append(curr)
    cpos = len(fibs) - 1
    index = n
    # Map the indices to the previous two values.
    while cpos > 1:
        # Belongs to the second region.
        if index >= fibs[cpos-2]:
            index -= fibs[cpos-2]
            cpos -= 1
        # First region, no need to update index.
        else:
            cpos -= 2
    # Adjust the index relative to cpos 1
    if cpos == 1:
        index -= a
    return (cpos, index)

def digit_ab(a, b, n):
    pos, index = backtrace(n-1, len(a), len(b))
    return int(a[index] if pos == 0 else b[index])

@timefunc
def solve_p230():
    A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    return sum(10**n * digit_ab(A, B, (127+19*n)*7**n) for n in xrange(18))

"""
Thoughts: Relatively straightforward problem. First of all, if one computes the
digits for n = 17, there are clearly way too many digits to fit into memory
if one were to actually compute the strings. The main intuition in this problem
is that all the digits in the final string originate from the strings A and B.
So, one can convert the desired index into an index in either A or B.

To illustrate this process, consider the example for N=35. The lengths of the
strings are: 10, 10, 20, 30, 50 (or just the fibonacci numbers where the first 
two values are 10). The 35th position in the last string is the 15th position
in the string of length 30 because the first half of the length 50 string
comes from the length 20 string, and the second half from the length 30 string.
Next, the 15th position in the length 30 string is the 5th position in the
length 20 string. Then, the 5th position in the length 20 string is the 5th
position in the first of the two length 10 strings. The iteration stops when
we reach one of the two original strings, so we can just take the 5th digit
in string A.

Generalizing this process results in an efficient solution to this problem.
The program computes the correct answer in <1 ms which is quite reasonable.
"""
if __name__ == "__main__":
    print solve_p230()