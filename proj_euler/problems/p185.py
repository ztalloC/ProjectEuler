# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:04:23 2016

@author: mjcosta
"""

import re
from collections import defaultdict

from proj_euler.utils.timing import timefunc

def parse_data(s):
    lines = s.strip().split("\n")
    # Parse with regular expressions.
    pat = re.compile("(\d+) ;(\d+) correct")
    groups = [pat.match(l).groups() for l in lines]
    groups = [(a, int(b)) for (a, b) in groups]
    output = zip(*groups)
    return list(output[0]), list(output[1])

def solve_puzzle(grid, counts, col, threshold=0.5, verbose=None):
    # One letter in the grid to consider.
    if col == len(grid[0])-1:
        # There should only be one digit left with a count of 1.
        one_count, zero_count = set(), set()
        for i in xrange(len(grid)):
            if counts[i] > 1:
                return None
            elif counts[i] == 1:
                one_count.add(grid[i][col])
            else:
                zero_count.add(grid[i][col])
        # There should only be one value left to fill.
        if len(one_count) != 1:
            return None
        else:
            result = next(iter(one_count))
            # This value should not have any zeroes.
            if result in zero_count:
                return None
            else:
                return [result]
    else:
        # Figure out the viable possibilities (i.e. no zero counts). Also
        # create an index of value positions.
        val_counts = defaultdict(set)
        val_pos = defaultdict(list)
        for i in xrange(len(grid)):
            val_counts[grid[i][col]].add(counts[i])
            val_pos[grid[i][col]].append(i)
        # Compute a fitness value for each choice.
        choices = defaultdict(int)
        for i in xrange(len(grid)):
            val = grid[i][col]
            if val not in choices or choices[val] != 0:
                if counts[i] != 0:
                    choices[val] += counts[i]/float(len(grid[0])-col)
                else:
                    choices[val] = 0
        # If 9 possibilities, then it's possible for the left out value since
        # it would not break the uniqueness constraint.
        if len(choices) == 9:
            digits = set(str(x) for x in range(10))
            left_out = next(iter(digits.difference(choices.keys())))
            choices[left_out] = 1.0/(len(grid[0])-col)
        max_prob = max(choices.values())
        # Filter for probabilities greater than the max * threshold (and not 0).
        choice_probs = filter(lambda x: x[1] >= max_prob * threshold and x[1] > 0, choices.items())
        # Sort in descending order of expected value.
        choice_probs.sort(key=lambda x: x[1], reverse=True)
        # Now, test each viable value and solve recursively.
        for (v, vprob) in choice_probs:
            # Create a copy of the counts and decrease by 1 at each position
            # where the digit occurs in this column.
            hypo_counts = counts[:]
            for i in val_pos[v]:
                hypo_counts[i] -= 1
            if verbose is not None and col < verbose:
                print "Checking %s at column %d w/ exp %.3f" % (v, col, vprob)
            sol_digits = solve_puzzle(grid, hypo_counts, col+1, threshold, verbose)
            # Found a solution!
            if sol_digits != None:
                sol_digits.insert(0, v)
                return sol_digits
        return None

@timefunc
def solve_p185(data, threshold=0.5, verbose=None):
    grid, counts = parse_data(data)
    sol = solve_puzzle(grid, counts, 0, threshold, verbose=verbose)
    if sol != None:
        return "".join(sol)
    else:
        return None

example = """
90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct"""

problem = """
5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct"""

"""
Thoughts: This was a very interesting problem. From initial inspection, the
brute force method of trying is obviously infeasible with 10^16 possibilities.
A more realistic solution is to guess one of the digits, decrement the number
correct based on it, and return the result if it meets all the requirements.

The reason this strategy is better is because one can restrict the possible
digits based on the number correct and the digits present in a given column.
Obviously if a row has zero correct, one can eliminate the possibility of a
digit in a given column. One can also restrict the possible allowed digits
to the set of unique digits in a column (not belonging to a zero row). If there
are 9 unique digits, one must allow all 10 digits to be chosen. This is because
if there are 9 unique digits, it's possible that the left out digit is correct.
But if there are 8 or fewer, then if the correct digit is not among the digits
present, then the solution string is no longer unique as it could have multiple
outcomes (and there are no constraints).

So, this strategy works (though it was a little finicky to get the code working
), but it is slow. Although many possibilities have been eliminated, the
search space is still massive. The problem is actually NP-hard, so there is
no guaranteed solution for all inputs. However, if we assume the input digits
are essentially random, we can use some heuristics to speed it up.

First, the order that we guess digits is very important, especially for the
first digit. If we can guess the right digit in a small number of guesses, then
the search will finish faster. One heuristic I used was to compute the expected
value that a given guess was correct for a column. Suppose that there are X
digits in a row and Y of them are correct, then a given digit is correct with
expectation Y/X. For digits with non-zero rows, one can sum the expected values
up to get a fitness score. Thinking back, a geometric mean might be more
appropriate, but it doesn't matter that much. Once we have a fitness score for
each digit, one can simply sort in descending order and consider digits in that
order.

With score ranking, the search is slightly faster, but it still takes ages.
Obviously, if we guess wrong on the first digit, we have to wait a long time
for the recursion to finish before trying another first digit. The natural
solution to this problem is to prune the search space. The solution I came up
with was a simple threshold based pruning method (not particularly great, but
easy to do). Given the fitness score for a digit, I would only consider scores
that were higher than a certain percent of the highest score. In this way, I
would not consider unlikely paths and save a lot of time. This approach is
something that I learned in a machine translation course that I once took
(where one wants to find the best translation in a large search space).

The downside to this threshold pruning approach is that there is the
possibility that we might skip over the actual solution. Fortunately, the
solution we are looking for is unique, so if we skip over it, then we can
easily tell at the end. The threshold itself is a configurable parameter of
the algorithm. The lower the threshold, the closer it is to exhaustive search,
while a higher threshold is faster but could potentially skip the solution.

Playing with the parameter, the program can find the answer in ~160 ms.
Raising the threshold can cause the program to fail to find it, but fail very
quickly. I did not try very hard to optimize the threshold. Looking at the
solution thread, ~160 ms is very respectable as other people took hours to
solve this problem (which is what I would estimate without pruning). The code
itself could be a lot cleaner (decomposed into smaller functions or written
simpler), but the performance is very good.
"""
if __name__ == "__main__":
    print "Example (expect 39542):"
    print solve_p185(example)
    print "Problem:"
    print solve_p185(problem, 0.65, None)