# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:05:14 2016

@author: mjcosta
"""

from collections import defaultdict
from fractions import Fraction

from proj_euler.utils.timing import timefunc

# Returns a list of tuples containing the possible outcomes from drawing at
# the current state. The first element is the number of ways an outcome can
# happen, while the second element is the new state itself.
def compute_neighbors(current):
    result = []
    # Convert from tuple to list if needed
    if type(current) == tuple:
        current = list(current)
    for (i, v) in enumerate(current):
        # Can't split an empty size.
        if v != 0:
            neighbor = current[:]
            neighbor[i] -= 1
            # Split into smaller sizes.
            for j in xrange(i+1, len(current)):
                neighbor[j] += 1
            # Exclude the empty case.
            if sum(neighbor) != 0:
                result.append((v, neighbor))
    return result

# Computes the expected number of times a single sheet is left in the bag
# for a given initial configuration, skipping the final configuration. Returns
# a fraction with the exact expected value.    
@timefunc
def solve_p151(init, verbose=False):
    # Stores the probability of a given configuration at a time step.
    states = defaultdict(int)
    states[init] = Fraction(1, 1)
    result = 0
    # Compute the number of steps needed in advance.
    steps = sum(v * 2**(len(init)-1-i) for (i, v) in enumerate(init))-2
    for i in xrange(steps):
        if verbose:
            print "Step", (i+1)
        new_states = defaultdict(int)
        for old_state in states:
            # Compute the possible transitions.
            neighbors = compute_neighbors(old_state)
            out_edges = sum(old_state)
            # Split the probability of the old state among its neighbors.                
            for (num, n) in neighbors:
                new_states[tuple(n)] += num * states[old_state] / out_edges
        # Add the probability of singleton states to the result.
        for state in new_states:
            if verbose:
                print state, new_states[state]
            if sum(state) == 1:
                result += new_states[state]        
        states = new_states
    return result

"""
Thoughts: A fine problem. I used markov chains to solve the problem. Basically,
One starts at the initial state node with probability 1, and then one can
transition between different nodes based on the probability of drawing nodes.
Then, to calculate the expected value of the number of days where only one
sheet is in the bag, simply sum the probabilities of the nodes that meet the
requirement.

The performance of the code is fairly good, taking only 5 ms to solve. This
is understandable since the number of possible states at each step is very
small. Other solutions from the solutions thread used dynamic programming,
which is very similar in idea, but I have difficulty thinking of probability
like that, so I just used markov chains.
"""
if __name__ == "__main__":
    result = solve_p151((1,1,1,1))
    # Format the result to six decimal places.
    print format(float(result), "0.6f")
    