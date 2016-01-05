# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 00:12:45 2015

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Generates triples according to:
# http://stackoverflow.com/questions/18294496/proof-pythagorean-triple-algorithm-is-faster-by-euclids-formula
def gen_triples(pred):
    triples = [(3,4,5)]
    while len(triples) > 0:
        (a,b,c) = triples.pop()
        if pred(a,b,c):
            if a < b:
                yield (a,b,c)
            else:
                yield (b,a,c)
            triples.append((a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c))
            triples.append((a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c))
            triples.append((-a+2*b+2*c, -2*a+b+2*c, -2*a+2*b+3*c))

# Calculates the sum of all triangles with perimeters less than limit
@timefunc
def calc_triangle_sum(limit):
    result = 0
    for (a,b,c) in gen_triples(lambda a,b,c: 2*a + 2*c <= limit):
        if abs(2*a-c) == 1:
            # Combine two triangles formed from the triple
            result += 2*a+2*c
    return result

"""
Thoughts: It took me a while to solve this. My first thought was to try to
brute force all possible almost equilateral triangles using heron's formula.
This was too slow (and I later realized that it ran into precision issues).

The next solution I came up with was to generate all pythagorean triples with
perimeters under a billion. I was rusty on this topic, so I put it off but
I found a nice recursive solution, so I used that. Given a pythagorean triple,
you can construct an almost equilateral triangle by placing two right triangles
next to each other and checking if twice a within 1 of c. If so, the new
triangle has two sides of length c and one side of length 2*a. It is not
necessary to consider multiples of primative triples because we want a
difference of 1, while a multiple will also multiply this difference. This was
a lot faster due to the reduced search space but still slow (taking 90s). I
also had to simulate the recursion using a stack since I was exceeding the
stack recursion depth limit, but this is probably for the best.

The solutions other people had were a lot faster than mine, but I'm still
satisfied. The crux of the problem was reducing the search space using math
knowledge, but I am not well versed in this area. Searching the internet also
came up with mostly spoilers for this question, so I couldn't really search
either. It seemed that other people relied on another form of heron's formula
which is something I considered but didn't try out. Regardless, with this
question, I finished the first 100 problems.
"""
if __name__ == "__main__":
    limit = int(1e9)
    # Simply perform the computation and time it
    result = calc_triangle_sum(limit)
    # Print the results
    print "The answer is (limit = %d): %d" % (limit, result)