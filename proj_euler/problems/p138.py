# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:24:24 2016

@author: mjcosta
"""

from itertools import islice

from proj_euler.utils.timing import timefunc

# Returns an infinite generator of solutions for the equation y^2 = 5L^2 - 1 
# where solutions are returned in the format (L, y).
def diophantine_solutions():
    # Initial solution, 5*1^2 -1 = 2^2.
    x, y = (1, 2)
    yield (x, y)
    while True:
        # We can generate infinite solutions with a recurrence relation.
        # Coefficients generated from: https://www.alpertron.com.ar/QUAD.HTM
        x, y = (9*x + 4*y, 20*x + 9*y)
        yield (x, y)

# Returns an infinite generator of special isoceles triangles in the form
# (b, h, L). 
def generate_special_isoceles():
    diop_sols = diophantine_solutions()
    # Skip the solution (0, 1, 1)
    next(diop_sols)
    for L, y in diop_sols:
        # Based on how solutions are generated, y can only be 2 or 3 mod 5,
        # which determines whether it is h = b + 1 or h = b - 1.
        sign = 1 if y % 5 == 2 else -1
        b = (sign * -4 + 2 * y)/5
        yield (b, b + sign, L)


# Computes the sum of the first num smallest special isoceles triangles.
@timefunc
def solve_p138(num):
    return sum(x[2] for x in islice(generate_special_isoceles(), num))

"""
Thoughts: This problem took a while for me to solve since it was mostly math
based (the code was very short). The problem was finding special isoceles
triangles where the height was within +/- 1 of the base. From this requirement,
one can use the Pythagorean formula to have L^2 = b^2 + h^2 and then substitute
h = b +/- 1 into the formula and solve. Solving the equation results in
b = (-/+ 4 +/- sqrt(5L^2-1)), but since sqrt(5L^2-1) >= 4 (if L > 0), we can
just consider b = (-/+ 4 + sqrt(5L^2-1)).

Now we need to find values of 5L^2-1 that are equal to a perfect square. If
you let y^2 = 5L^2 - 1, then y^2 - 5L^2 = -1, which is the negative Pell's
equation. I did not feel like writing a solver, so after much searching online,
I found "https://www.alpertron.com.ar/QUAD.HTM", which is a tool for solving
quadratic Diophantine solutions (Pell's is a specific case) of the form
ax^2 + bxy + cy^2 + dx + ey + f  = 0 (where you plug in the constants a-f).
The tool gave me some simple recurrences that I could use to generate infinite
solutions from an initial solution (also given). 

I then just had to plug in the solutions to y^2 = 5L^2 - 1, and use some simple
math to generate b and h. It was then just a matter of summing up the lengths
of the triangles. The code is very short and efficient, taking only a few
microseconds to run (my timing method is probably not accurate enough). After
solving the problem, I looked at how other people solved it and it seems that
the side length of the triangles are half of every 6th Fibonacci number
starting from 9 (i.e. 9, 15, 21, ...). This is quite interesting, though it
is not something I would have thought of unless I was very familiar with
Fibonacci numbers.
"""
if __name__ == "__main__":
    # 307 + 15 = 322
    print "Example (2 lowest) (expect 322):"
    print solve_p138(2)
    print "Problem (12 lowest):"
    print solve_p138(12)
                