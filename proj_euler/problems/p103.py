# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:26:10 2016

@author: mjcosta
"""

from collections import namedtuple

from proj_euler.utils.timing import timefunc

# Represents the sum of a set of numbers, storing the count of values as well.
SubsetSum = namedtuple('SubsetSum', 'sum, count')
# An empty subset sum.
emptySet = SubsetSum(0, 0)

# Given a list of numbers, returns a generator of lists where each element
# in an output list is within +/-dist of the original element, e.g. [1] and 1
# can output [0], [1], and, [2].
def generate_range(l, dist):
    # If empty, output a empty list
    if len(l) == 0:
        yield []
        return
    curr = l[0]
    remain = l[1:]
    # Generate all possibilities for the remaining list
    for new_range in generate_range(remain, dist):
        for new_value in xrange(curr-dist, curr+dist+1):
            new_copy = new_range[:]
            new_copy.insert(0, new_value)
            yield new_copy
            
# Checks if a list of elements is a special sum set. Returns True if so,
# and false otherwise.
def check_special_sumset(l):
    # First, the elements must be unique (for both set and subset condition).
    # This condition filters many values.
    s = set(l)
    if len(s) != len(l):
        return False
    # Next, generate the distinct disjoint subset sum pairs.
    sum_pairs = generate_distinct_empty(l)
    # Check if all pairs satisfy the properties.
    return all(check_valid(p) for p in sum_pairs)

# Checks if a subset sum pair is valid.
def check_valid(pair):
    x, y = pair
    # Do not consider comparisons against the empty set (which are valid).
    if x.count == 0 or y.count == 0:
        return True
    # One can violate if the sums are equal
    if x.sum == y.sum:
        return False
    # If same count, then no violation
    if x.count == y.count:
        return True
    # Get the larger and smaller count
    big = max(pair, key=lambda a: a.count)
    small = min(pair, key=lambda a: a.count)
    # Big should have a bigger sum than small
    return big.sum > small.sum

# Generates distinct disjoint subsets given a list of values. Includes empty
# fields which need to be filtered.
def generate_distinct_empty(vs):
    if len(vs) == 0:
        yield (emptySet, emptySet)
    elif len(vs) == 1:
        yield (emptySet, emptySet)
        # Only do one side to prevent symmetric records
        yield (SubsetSum(sum=vs[0], count=1), emptySet)
    else:
        head = vs[0]
        tail = vs[1:]
        for d in generate_distinct_empty(tail):
            yield d
            dleft = (SubsetSum(sum=d[0].sum+head, count=d[0].count+1), d[1])
            yield dleft
            # In the case of two empty records, we do not want to output 
            # two entrie since the two are actually the same
            if d[0].count != 0 or d[1].count != 0:
                dright = (d[0], SubsetSum(sum=d[1].sum+head, count=d[1].count+1))
                yield dright
            
            
# Computes a near optimum set using a heuristic given the previous optimum.
def heuristic_optimum(prev):
    # Find the middle element (taking the upper value if even length)
    middle = prev[len(prev)/2]
    result = map(lambda x: x + middle, prev)
    result.insert(0, middle)
    return result
            
# Given the optimum set of size n, performs a search for the optimum set of 
# size n + 1 (given a distance parameter to use).
@timefunc
def find_optimum(prev, dist):
    # Use the heuristic as the initial estimate.
    output = heuristic_optimum(prev)
    min_sum = sum(output)
    # Check all possible lists within a certain distance of the heuristic.
    for cand in generate_range(output, dist):
        # If the sum is higher, just skip it to save time
        cand_sum = sum(cand)
        if cand_sum >= min_sum:
            continue
        if check_special_sumset(cand):
            output = cand
            min_sum = cand_sum
    return sorted(output)

"""
Thoughts: I worked on this while considering 105 and 106. I put in a little
thought on how to check the special sum set property in a reasonably efficient
manner. I checked my solution against 105 before attempting 103. 

The method is to simply check the neighborhood of sets around the heuristic 
(since it is "close" to optimum) by adding or subtracting from each value. For 
each candidate, just check if the properties hold. The challenging part is to 
come up with all the disjoint subsets efficiently. I used a recursive method
that builds pairs. For a given number, one can either not consider it, add it
to the left set, or add it to the right set. There are some edge cases with
removing duplicates such as ({1},{2}) vs ({2},{1}). It is obviously infeasible
to generate all the subsets, compute all pairs, and then filter for disjoint
pairs only.

After finishing the code, I tried a search space of 3 which took 116 seconds 
to run. I computed the heuristic and got the same answer, so I thought my 
distance wasn't enough. I tried a distance of 4 and got the same answer. So, 
I tried entering the heuristic value and sure enough it was correct. 
Therefore, one can just use a search distance of 0 which completes in < 1 ms.
I find it very strange that the problem would tell you a heuristic, tell you
that the heuristic is not always right (requiring a deeper solution) and then
have the heuristic be the right answer. It isn't a huge deal since you need to
do it the right way for 105, but it is still strange.
"""
if __name__ == "__main__":
    # n = 6: Expected solution is [11, 18, 19, 20, 22, 25]
    example = [6, 9, 11, 12, 13]
    print "Example (n = 6):"
    print find_optimum(example, 2)
    print "Problem (n = 7):"
    problem = [11, 18, 19, 20, 22, 25]
    # Adjusted distance manually, this is very strange.
    print find_optimum(problem, 0)