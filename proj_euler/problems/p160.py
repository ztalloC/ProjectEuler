# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:14:35 2016

@author: mjcosta
"""

from proj_euler.utils.memoize import memoize
from proj_euler.utils.timing import timefunc

# Computes the difference between the powers of 2 and the powers of 5 in n!.
def remaining_two_powers(n):
    # Iterate over the powers, dividing into n.
    pow2 = 2
    exp2 = 0
    while pow2 <= n:
        exp2 += n/pow2
        pow2 *= 2
    pow5 = 5
    exp5 = 0
    while pow5 <= n:
        exp5 += n/pow5
        pow5 *= 5
    return exp2 - exp5

# Computes n! for a given modulo, omitting the multiples of 2 and 5.
@memoize
def factorial_range(n, mod):
    result = 1
    for i in xrange(3, n+1, 2):
        # Skip multiples of two or five (equivalent to 1).
        if i % 5 != 0:
            result = (result * i) % mod
    return result

# Computes n! for a given modulo with the twos and fives removed.
def factorial_digits(n, mod):
    # Base case: 0! = 1.
    if n == 0:
        return 1
    # Compute the value of the even digits. Simply compute (n/2)! recursively
    # which reduces all the powers of two.
    evens = factorial_digits(n/2, mod)
    # Compute the missing odd digits and combine them.
    odds = odd_factors(n, mod)
    return evens * odds % mod

# Computes the odd digits in n! for a given modulo, excluding 5.
def odd_factors(n, mod):
    if n == 0:
        return 1
    else:
        odd_offset = n % mod
        odd_power = n/mod
        # Factorial range excludes 5, so one can safely compute the range,
        # raise it to an exponent and include the offset.
        ftotal = factorial_range(mod, mod)
        fpartial = factorial_range(odd_offset, mod)
        # Need to include the factors in the multiples of 5, so do the same
        # trick as with the evens, dividing by 5 this time.
        return pow(ftotal, odd_power, mod) * fpartial * odd_factors(n/5, mod)

@timefunc
def solve_p160(n, mod):
    two_exps = remaining_two_powers(n)
    facts = factorial_digits(n, mod)
    return facts * pow(2, two_exps, mod) % mod
    
"""
Thoughts: This problem took me a while to wrap my head around. First, it
should be obvious that computing 10^12! is not going to happen (even if you
keep the minimum number of digits around).

The main observation for this problem is that one can get the least significant
digits by computing n! by removing all the factors of 5 and removing a factor
of 2 alongside each factor of 5. Thus, one strategy for computing the least
significant digits would be to compute the number of 2s and 5s in n!, compute
n! without the 2s and 5s, and multiply the remaining 2s back into n!. This
would all be done mod 10^5 to prevent needing to store a massive value.

The naive strategy is still too slow, but it's something to build on. The next
idea I had was to only compute up to 10^5! and extend that 10^12. The basis
for this is the fact that when one computes 10^12! mod 10^5, the values between
0 and 10^5-1 repeat 10^7 times. However, there is a problem with this idea
(which is where I got stuck for a while). The problem is that when computing
this range, we are dividing out the 5s and 2s, but this causes the values to
no longer repeat (meaning we can't just raise the produt to a power). 

To illustrate this problem, suppose we wanted to compute only the last digit
of 40!. Dividing out 2s and 5s, 10! = 1*1*3*1*1*3*7*1*9*1 = 567 = 7 mod 10.
In the range 1-10, the 5 becomes 1 as 5/5 = 1, but in the range 31-40, 35
becomes 7 as 35/5 = 7. This means that we can't just use the same range
repeatedly.

The solution I found was to separate the digits into classes and handle cases
separately. First, consider the even digits in n! such as 2, 4, 6, ..., 2i.
We want to remove the factors of 2s from these and include only the odd factors
remaining (since the plan is to multiply the twos back in at the end). So, one
can simply divide by 2 which results in the range 1, 2, 3, ..., i. This is
exactly (n/2)!. The powers of 2 like 4, 8, 16, still have factors of 2 after
dividing by two, so we can again consider the even numbers using recursion. In
this manner, we have reduced the problem of finding the even contributions to
the problem of finding the odd contributions, which is the next case.

For the odd digits of n!, we want to remove factors of 5 from the product.
For this we can simply compute n!, skipping any multiples of 5 and then
include any factors from multiples of 5 later on (e.g. 7 from 35/5=7). If it
is just odd digits of n! (excluding multiples of 5), then we can use the idea
of computing 10^5! and repeating it (by raising it to a power) to efficiently
compute this quantity. This is because the range 1-10^5 is identical to all
other ranges for the purpose of the modulo computation (since we are excluding
2s and 5s which break the regularity). 

So now it's just a matter of computing the odd factors which are part of a
multiple of 5. The multiples of 10 were converted to 5s by the even case, so
it is only necessary to handle odd multiples of 5. So, we have the sequence
5, 15, 25, 35, ... 10i+5. If we divide by 5, we get the sequence 
1, 3, 5, 7, ... 2i+1 which is effectively the odd digits of n! again. Thus,
the case for odd multiples of 5s is nearly identical to the even case, but
we use n/5 instead of n/2. As with the even case, we can eliminate higher
powers of 5 by using recursion.

With all of these findings in place, it is relatively straightforward to
write up a solution. The performance of the resulting code is fairly good,
taking only ~270 ms to solve the problem for n = 10^12. I actually had a
related question come up in an interview question, which is why I decided to
solve this problem.
"""
if __name__ == "__main__":
    print "Example (n = 9) (expect 36288):"
    print solve_p160(9, 10**5)
    print "Example (n = 10) (expect 36288):"
    print solve_p160(10, 10**5)
    print "Example (n = 20) (expect 17644):"
    print solve_p160(20, 10**5)
    print "Problem (n = 10^12):"
    print solve_p160(10**12, 10**5)