# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 13:44:04 2016

@author: mjcosta
"""

from proj_euler.utils.base import baseN
from proj_euler.utils.timing import timefunc

# Computes the number of non divisible entries up to a given row where the
# row is written as a string "n" in base "base". Starts counting from 0.
def compute_non_div(n, base):
    # Empty string, just 0.
    if len(n) == 0:
        return 0
    # Length 1, just sum under that value.
    elif len(n) == 1:
        return sum(xrange(1, int(n)+2))
    base_sum = sum(xrange(1, base+1))
    digit = int(n[0])
    digit_sum = sum(xrange(1, digit+1))
    # Get the next significant value in the string, if all 0s, just return 0.
    # Do this by stripping away zeroes.
    remain_sig = n[1:].lstrip('0')
    if len(remain_sig) == 0:
        remain_sig = '0'
    base_value = digit_sum * (base_sum ** (len(n)-1))
    return base_value + ((digit + 1) * compute_non_div(remain_sig, base))


@timefunc
def solve_p148(nrows, base):
    # Our algorithm starts from 0, while the number is given starting from 1,
    # so subtract 1.
    return compute_non_div(baseN(int(nrows-1), base), base)
    
"""
Thoughts: Very interesting problem, though not particularly difficult. 

First, I considered the idea that (a choose b) is equal to a!/b!(a-b)!. 
If an entry is to be divisible, then the number of 7s in the top factorial
must be greater than sum of the 7s in the denominator. Thinking about the
pattern the results, you get a bunch of recursive triangle figures which prints
some nice patterns (the Sierpinski triangle). However, this was not used to
solve the problem (but is worth mentioning).

During my search for ideas, I found: http://stackoverflow.com/a/22526217
which gives a formula for the number of non-divisible items in a given row,
which is equal to the product of the digits + 1 in a given base (base 7 here)
e.g. 123 has (2 + 1) * (3 + 1) * (4 + 1) non-divisible entries. This is very
useful and one could probably brute force the sum of 1 billion entries.

After coming up with a formula for each row, I tried to come up with a formula
for the sum of the entries. In the base string representation, the sum of all
possible values in the least significant entry is for base 7, 1+2+3+4+5+6+7=28.
The sum of all possible values in the next digit is simply 28^2 = 784. So, for
a given digit in base 7, one can add the triangle number of the digit times
28^n (where n is the number of zeroes afterwards). So, for 2000 we would add
(1+2)*28^3 to the sum.

However, after consider a certain digit, we need to consider the rows after
the value represented by the digit alone. For example, in 201, we have 3*28^2
from 2, but still need to account for the remaining digits. To account for
the remaining digits, we just compute the number of non divisible entries for
the remaining digits but multiply by the (digit + 1). This is because the
remaining digits are occurring in the context of the digit we just considered.
So, S(201) = 2*28^2 + (1+2)*S(1) = 2*28^2 + 3*(1+2) = 2*28^2 + 9 = 2361. In the
case that there are no significant digits, we still need to consider "0" or all
the zeroes following the digit. Note that 201 in base 7 is 99 in base 10, which
corresponds to the 100th row in the problem description (thus 2361 entries).

The answer works quite well, running under 1/10 of a millisecond (my timing may
not be accurate at this point). I could have brute forced the solution, but
this was very satisfying to do. In fact, the problem can reasonably be done
by hand if desired.
"""
if __name__ == "__main__":
    print "Example (100) (expect 2361):"
    print solve_p148(100, 7)
    print "Problem (1e9):"
    print solve_p148(1e9, 7)