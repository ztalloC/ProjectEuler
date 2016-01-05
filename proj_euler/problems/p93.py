# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:10:32 2015

@author: mjcosta
"""

import operator
import itertools
from proj_euler.utils.timing import timefunc

# Calculates the set with the longest subsequence of arithmetic expressions
@timefunc
def find_longest_set():
    digits = range(10)
    max_set = None
    max_len = 0
    for combo in itertools.combinations(digits, 4):
        exp_set = compute_operations(list(combo))
        exp_len = compute_run(exp_set)
        if exp_len > max_len:
            max_len = exp_len
            max_set = combo
    return max_set
        

# Given a set of numbers, computes the number of consecutive values from 1 to n
def compute_run(vals):
    vals = sorted(vals)
    for i in range(len(vals)):
        if vals[i] != (i+1):
            return i

# Given a set of digits, computes all the possible operation combos
def compute_operations(vals):
    if len(vals) == 1:
        if vals[0] > 0 and int(vals[0]) == vals[0]:
            return set(vals)
        else:
            return set()

    ops = [operator.add, operator.sub, operator.mul, operator.div]
    results = set()
    for combo in itertools.permutations(vals, 2):
        for op in ops:
            # Don't divide by 0
            if combo[1] == 0 and op == operator.div:
                break            
            # Remove the two values and add the result
            new_vals = vals[:]
            new_vals.remove(combo[0])
            new_vals.remove(combo[1])
            if op == operator.div:
                v = op(float(combo[0]), combo[1])
            else:
                v = op(combo[0], combo[1])
            new_vals.append(v)
            results = results.union(compute_operations(new_vals))
    return results

"""
Thoughts: The problem was not particularly difficult, though I did make a few
mistakes. First, I forgot to exclude negative numbers and second I excluded
intermediate fractional results e.g. (3/2) * 2. As for the algorithm, it was
just brute force. It could be faster by memorizing the results for subsets
of values or being clever. 
"""
if __name__ == "__main__":
    # Simply perform the computation and time it
    result = find_longest_set()
    # Print the results
    print "The answer is:", result