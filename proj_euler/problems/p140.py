# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:18:16 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Generates modified fibonacci nuggets given an initial solution and a limit.
def generate_nuggets(x, y, limit):
    i = 0
    while i < limit:
        ysol = abs(y)
        if ysol % 5 == 2 and ysol >= 7:
            yield (ysol - 7)/5
        x, y = 9*x + 4*y, 20*x + 9*y
        i += 1
        
@timefunc
def solve_p140(limit, num):
    gen_signs = lambda x, y: [(x, y), (-x, y), (x, -y), (-x, -y)]
    initial_sols = gen_signs(5, 13) + gen_signs(7, 17) + gen_signs(1, 7) \
        + gen_signs(2, 8) + gen_signs(14, 32)
    nuggets = []
    for (x, y) in initial_sols:
        for nug in generate_nuggets(x, y, limit):
            nuggets.append(nug)
    nuggets = sorted(set(nuggets))
    nuggets.remove(0)
    return sum(nuggets[:num])

"""
Thoughts: There is not much to figure out in this problem that wasn't already
done in 137 (Fibonacci golden nuggets). Solving the infinite series results
in the equation A(x) = (3x^2 + x)/(1 - x - x^2) which has a rational value
when 5y^2 + 14y + 1 is a perfect square. Then, we can reduce solving y
to: y = +/- sqrt(5a^2 + 44)/5 - 7/5. So, if 5a^2 + 44 is a perfect square, then
we can generate a solution for y. We can use Dario Alpern's two variable
equation solver to come up with a recurrence relation to generate infinite
solutions from a set of initial solutions. There were quite a few duplicate
solutions, so I just take a bunch from each initial solution and then
combine and sort later on.
"""
if __name__ == "__main__":
    print solve_p140(200, 30)