# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 08:37:18 2015

@author: mjcosta
"""

from proj_euler.utils import primes
from proj_euler.utils.timing import timefunc
from collections import namedtuple

MinPSumRecord = namedtuple('MinPSumRecord', 'factors, product, sum')

"""
Takes a sorted list of primes, a limit, a history dictionary, 
and the current MinPSumRecord record. Generates a list of all products
less than the limit using the given primes (through the history dict).
"""
def generate_prods(ps, limit, history, curr):
    # Add a prime from the set of considered primes
    for p in ps:
        # If the prime times the current number is bigger than the limit
        # then we have reached our stopping point for this point
        new_num = curr.product * p

        if new_num > limit:
            return
        # Add the prime to the current working set
        current_p = curr.factors[:]
        current_p.append(p)
        current_p.sort()
        key = tuple(current_p)
        new_ps = []
        # If the set has already been used, don't repeat it
        if key not in history:
            new_ps.append(MinPSumRecord(current_p, new_num, curr.sum + p))
        
        # We also consider multiplying the new prime by any existing factor
        for i in range(len(curr.factors)):
            new_f = curr.factors[:]
            new_f[i] *= p
            new_f.sort()
            key = tuple(new_f)
            # As before check if we've done it before
            if key in history:
                continue
            # Otherwise, add to the set to consider
            new_ps.append(MinPSumRecord(new_f, new_num, sum(new_f)))
        # At the end, generate a recursive call for each branch
        for new_p in new_ps:            
            # Add each entry to the history
            key = tuple(new_p.factors)
            history[key] = new_p
            generate_prods(ps, limit, history, new_p)

"""
Given a max_k for the set of min product sum numbers, generates a dictionary
where the key is the value of k and the value is the number for that k.
"""
def generate_min_ps(max_k):
    # First, we only need to consider values twice that of k
    limit = 2 * max_k
    # We also only need to use primes that are <= limit
    prime_set = primes.generate_primes(limit)
    # Now generate the set of all products using those values.
    start_psr = MinPSumRecord([], 1, 0)
    prods = dict()
    # The results are returned through the history dictionary "prods"
    generate_prods(prime_set, limit, prods, start_psr)
    # So now go through the values and generate the min prod sums
    min_psn = dict()
    for psr in prods.values():
        # The value is just the product
        val = psr.product
        # For the size of the set, we need to add 1s to make up the difference
        # based on the difference between the product and sum
        set_size = len(psr.factors) + (psr.product - psr.sum)
        # Must be composed of at least two numbers
        if set_size < 2 or set_size > max_k:
            continue
        # If we haven't seen this set size or the value is smaller, update
        if set_size not in min_psn or val < min_psn[set_size]:
            # print set_size, val, psr
            min_psn[set_size] = val
    # We have the result
    return min_psn
    
"""
Given a max k, finds the sum of the complete set of minimal product sum
numbers.
"""
@timefunc
def calc_sum_mpsn(max_k):
    # Compute the min product sum numbers
    min_psn = generate_min_ps(max_k)
    # Get the set of values and sum them up
    min_psn_set = set(min_psn.values())
    return sum(min_psn_set)

"""
Thoughts: The first major observation I had was that you could construct
a product sum number given a factorization by adding 1s until the sum
equaled the product. 

This means that it is only necessary to consider values
up to 2*k. Specifically, if you have a number "x = 2*k", the most you can
do to create a difference between the product and sum is to divide by 2. This
leaves you with the numbers 2 and k with a difference of k-2 between the
product and the sum. So if you have k-2 1's, that leaves you with k values
in total. Thus, 2k is the maximum bound of numbers to consider.

So how to generate the solution? Well, my initial thought was to get the
prime factorizations, somehow combine them to get all factorizations for all
numbers between 2 and 2k. However, this is rather complicated and left me
thinking for a while. Eventually, I decided to just take the primes that
could possibly be used and generate all combinations of products <= 2k.
Using recursion and limiting the amount of branching, this was relatively
straightforward and gave me the answer.
""" 
if __name__ == "__main__":
    # The values of k to evaluate
    k_values = [6,12,12000]
    for k in k_values:
        result = calc_sum_mpsn(k)
        # Print the results
        print "The answer for (k = %d) is: %d" % (k, result)