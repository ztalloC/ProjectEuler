# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:10:40 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

"""
Brute force:

def is_reversible(n):
    # No leading zeroes allowed in reverse(n)
    if n % 10 == 0:
        return False
    temp = n
    reverse = 0
    # Build the reverse number by taking off digits from n.
    while temp > 0:
        reverse = reverse * 10 + (temp % 10)
        temp /= 10
    s = reverse + n
    # Check that all the digits are odd.
    while s > 0:
        if s % 2 == 0:
            return False
        s /= 10
    return True

@timefunc
def solve_p145(limit):
    return sum(2 for x in xrange(1, limit, 2) if is_reversible(x))
"""

@timefunc
def solve_p145(digits):
    result = 0
    for d in xrange(1, digits+1):
        if d % 2 == 0:
            result += 20 * (30 ** (d/2 - 1))
        elif d % 4 == 3:
            result += 100 * (500 ** (d/4))  
    return result
         
"""
Thoughts: This was a relatively simple problem. It is not unreasonable to brute
force. I wrote some simple brute force code which took 10 minutes to run (just
left it running while going for dinner). It could have been faster if I wrote
it more efficiently, used parallelism, wrote it in a lower level language, etc.
In fact, one could observe that there are no 9 digit reversible numbers and
just do 1/10 the amount of work.

Then, I decided to solve it again but using logic instead. First, one can see
that 1 digit values can not be reversible since a number added with itself (
i.e. 1 digit numbers are the same when reversed) must be even. 

For two digit numbers, one can see that the two digits must add two an odd 
value and must not add to 10 or higher. Of course, the last digit must not be 
zero, else the reverse value starts with 0 (forbidden by the problem), which 
applies to higher digits. Enumerating the combos, there are 20 pairs that meet 
these conditions. 

For three digit numbers, the center digit is the problem since it adds with
itself to be even. To make it odd, the two outside digits must carry. To allow
for the outside digits to be odd, they must add to an odd value and the middle
digit can not add to a value over 10. There are 5 middle values where 2x < 10
and 20 outside values with the needed conditions, thus 100 values.

For four digit numbers, the outside digits have the same conditions as two
digit numbers, while the inner two digits must add to odd values, but one of
them is allowed to be zero. Enumerating the combos, there are 30 inner combos
and again 20 outer combos, allowing for 600 combos.

For five digit numbers, there are no combos. This is because the center digit
adds with itself to be even, but unlike in three digits, one cannot create
a carry that can make the center digit odd without making other digits even.

Six digit numbers follow the same pattern as 4, having 20*30*30 combos.

Seven digit numbers, one can make the outermost digits add to an odd value and
greater than 10, the next-most outer digits to an even value greater than 10.
The next two digits can be odd and greater than 10, and the center digit must
add to less than 10. This results in 5 choices for the center digit, 20 for
odd digits greater than 10, and 25 for even digits greater than 10, for
5 * 20 * 25 * 20.

This pattern can be generalized as follows:

if d = 2k, then 20 combos for the outer pair and 30 for each inner pair, so
20*30^(k-1) combos.
if d = 4k+1, then no combos.
if d = 4k+3, then one can use two pairs to generate a carry to the center.
25 pairs for even sum greater than 10 and 20 pairs for odd sum greater than 10.
In the middle, there are 5 choices and there is a single pair around the middle
that can have 20 combos. The formula is then, 5*20*(25*20)^k = 100*500^k.
"""
if __name__ == "__main__":
    print "Example (< 1000) (expect 120):"
    print solve_p145(3)
    print "Problem (< 1e9):"
    print solve_p145(9)