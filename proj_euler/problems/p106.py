# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 23:13:18 2016

@author: mjcosta
"""

from copy import deepcopy

from proj_euler.utils.timing import timefunc

# Given a list, generates the power set of that iterable
def power_set(l):
    if len(l) == 0:
        yield []
    else:
        head = l[0]
        tail = l[1:]
        for pset in power_set(tail):
            # Current element can either be in the set or not.
            yield pset
            pnew = deepcopy(pset)
            pnew.insert(0, head)
            yield pnew

# For a given list, counts the number of non strictly-dominated subsets.
@timefunc
def count_non_dominant(elements):
    pset = [set(x) for x in power_set(elements)]
    count = 0
    for i, s1 in enumerate(pset):
        # Don't consider mirrored pairs
        for s2 in pset[i:]:
            # Sets need to be disjoint, of equal size, and larger than 1.
            if len(s1) == len(s2) and len(s1) > 1 and \
                len(s1) + len(s2) == len(s1.union(s2)):
                # Sets are not necessarily in sorted order
                l1 = sorted(s1)
                l2 = sorted(s2)
                # Count the number of inequalities between the two.
                ineq = len(filter(lambda s: s[0] < s[1], zip(l1, l2)))
                # If the set is not dominated (or dominant), then increment.
                if ineq != 0 and ineq != len(s1):
                    count += 1
    return count

"""
Thoughts: This was a tricky problem even after solving 103 and 105. The
essence of the problem is figuring out which subset pairs to consider. First,
the two entries must be of equal size since we assume property 2 is true so
they can't be equal. We also assume that the items are strictly increasing,
so there can't be duplicate 1-sets (and they are a set to begin with). 

Looking at n = 4, there are three pairs (12)(34), (13)(24), and (14)(23).
The first two pairs can be skipped since each element in the first set can
be matched with another element in the second set which is bigger than the
first element. This leaves 1 pair which is what we expected. The rule is to
just check if there is at least 1 inequality that breaks the trend, that is
the set is not strictly dominated or dominating.

Generating all these pairs to compute was the second issue. I didn't want to
do something troublesome like adapt 103's algorithm for this problem, so I just
generated all subsets and filtered, while skipping mirrored pairs. Unlike in
103 and 105, I would only be considering one set of elements at a time (rather
than testing many candidate sets), so this was actually feasible.

The initial code worked as expected for n = 4 and n = 7, but gave me the wrong 
answer for n = 12. This was because I had forgotten to sort the sets (in order
to pair the elements for comparison). Fixing this gave me the correct answer
in 1.2 seconds.
"""
if __name__ == "__main__":
    print "Example (n = 4):"
    print count_non_dominant(range(4))
    print "Example (n = 7):"
    print count_non_dominant(range(7))
    print "Problem (n = 12):"
    print count_non_dominant(range(12))