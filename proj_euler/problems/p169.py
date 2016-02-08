# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:54:35 2016

@author: mjcosta
"""

from proj_euler.utils.base import dec_to_bin
from proj_euler.utils.timing import timefunc

# Computes the number of different ways a bit string can be expressed where
# the bit string is represented as a list of differences of indices (as well as
# the end). For example, 10100 would be [2, 3]. Returns a tuple where the first
# element is the result and the second is a partial value useful for extending.
def compute_ways(diffs):
    # Special case 0, just 1.
    if len(diffs) == 0:
        return 1
    # A single element is a power of two. f(2^m) = m+1, so the result is just
    # the element (which includes the "+1"). Excluding the initial position,
    # the number of remaining shift positions is just one less.
    elif len(diffs) == 1:
        return (diffs[0], diffs[0] - 1)
    # Given the leftmost '1' bit of a bitstring, one can "expand" it by
    # replacing the 1 with a "2" in the next position and then expand that
    # "2" into a "1" and another "2". For the initial configuration and each
    # of the zeroes (i.e. the difference of indices), all configurations of
    # this section of the string are independent of the number of results in
    # the rest of the string (so we can just multiply). 
    #
    # We can also shift one last time to put the "2" into the first position
    # of the next bit string section to get a "3". This is clearly illegal,
    # so the "3" needs to shift and become a "2" (followed by a "2"). Thus
    # we can also add a fraction of the next section's results (which excludes
    # the initial configuration).
    else:
        prev_result, prev_partial = compute_ways(diffs[1:])
        curr_partial = (diffs[0] - 1) * prev_result + prev_partial
        curr_result = curr_partial + prev_result
        return curr_result, curr_partial

# Computes the number of different ways n can be expressed as a sum of powers
# of 2 using each power no more than twice.
@timefunc
def solve_p169(n):
    # Get the bit string and compute the differences between the indices of '1'
    # as well as the end.
    bits = dec_to_bin(n)
    indices = [len(bits)-x for x in xrange(len(bits)) if bits[x] == '1'] + [0]
    diffs = [indices[x]-indices[x+1] for x in xrange(len(indices)-1)]
    # Return the result, omitting the partial value.
    return compute_ways(diffs)[0]

"""
Thoughts: Interesting problem for various reasons. Looking at the solution
thread, there were a few ways of solving the problem. I modeled the problem as
coming up with the number of possible bit strings for the value where each
position can contain a 0, 1, or 2. The resulting code is very simple and the
logic is explained in the comments (longer than the code itself). 

To summarize, one can first observe that f(2^m) = m+1 because the bit string is
m+1 digits long and one can "expand" the 1 into a 2 and shift it along the
length of the string to get m+1 possibilities. Then, one can build an
incremental solution moving from left to right using the positions of each
'1' bit. Obviously, for each zero between the first '1' and the next '1' and
the initial position, the shifts in the first section are independent of all
shifts in the remaining sections. 

One can also shift the first '1' on top of the following '1' which creates a 
'3'. To get rid of the '3', split the '3' into a '2' and a '2'. Thus, one can 
also add all possible results of the remaining section excluding contributions
from the initial configuration of the next section.

From this, we have a recurrence for n that is simple to compute. My code only
took 22 microseconds to solve the problem. For reference (from the solution
thread), one could also use the recurrence A(2n) = A(n) + A(n-1), 
A(2n+1) = A(n), and A(0) = A(1) = 1, to get the solution. 

This problem actually took me a little bit more time to solve for another 
reason. Specifically, I was passing the value int(1e25) instead of 10**25.
Due to floating point precision, these two are very different values (just
check the python console) and they have very different solutions for this 
problem. Because of this, I had come up with the correct algorithm early on,
but because I was using the wrong input, it was giving me the wrong answer.
Thus, I was convinced my algorithm was wrong and spent longer on the problem
than what was necessary until I finally noticed it.
"""
if __name__ == "__main__":
    print "Example (n = 10) (expect 5):"
    print solve_p169(10)
    print "Problem (n = 10^25):"
    print solve_p169(10**25)