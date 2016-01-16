# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 09:02:34 2016

@author: mjcosta
"""

from collections import defaultdict

from proj_euler.utils.timing import timefunc

# Computes the number of cubes needed for the n-th layer for an a x b x c base.
def cuboid_layer(a, b, c, n):
    # The formula consists of the base layer
    base = 2 * (a * b + b * c + a * c)
    # The ridges on the sides created by extending the base layer
    ridges = 4 * (n - 1) * (a + b + c)
    # And the corners formed between the ridges.
    corners = 8 * triangle_number(n - 2)
    return base + ridges + corners

# Computes the n-th triangle number, 0 and below is defined as 0.
def triangle_number(n):
    return n * (n + 1)/2

# Computes the least value of n with a given number of solutions. Also takes
# a parameter that upper bounds the solution set.   
@timefunc
def solve_p126(target, limit):
    # Not really elegant, but it is effective.
    a = 1
    counts = defaultdict(int)
    # Note: Do not repeat identical shapes.
    while cuboid_layer(a, a, a, 1) < limit:
        b = a
        while cuboid_layer(a, b, b, 1) < limit:
            c = b
            while cuboid_layer(a, b, c, 1) < limit:
                n = 1
                while cuboid_layer(a, b, c, n) < limit:
                    num = cuboid_layer(a, b, c, n)
                    counts[num] += 1
                    n += 1
                c += 1
            b += 1
        a += 1
    # Return the minimum key equal to the target
    return min(filter(lambda k: counts[k] == target, counts))
    
"""
Thoughts: I pushed this problem back for a while, but it wasn't that bad. When
I first saw the problem, I had difficulty visualizing how the cubes were
arranged on the third and fourth layer (which were not shown). Later, I used
a 3d drawing website that let me arrange cubes, so that I could see what the
final shapes looked like. Once I could see the shapes of the cubes, coming
up with the formula for the number of cuboids needed for a layer was quite
simple. 

Intuitively, we start as a "cube" whoses faces are extruded
to become like a fat "+" symbol. The faces extrude further out, but edges
appear between them, causing the shape to become a rough octagon. Then corners
appear between the edges, causing the shape to gain 8 triangle faces forming
a 24-sided shape.

For each layer, the cuboids could be divided into three cases. The first was
simply the original cube faces, extruded outwards; this was a constant value
for each layer. The second was the edges formed between the extruded faces
of the original cube. For each dimension, there are a multiple of 4 edges
that need to be handled (which grows proportianately with the number of 
layers). Lastly, there are the corners (starting at layer 3) which form 
between the "edges" and grow quadratically (actually proportionate to the 
triangle numbers).

After coming up with the formula, it was just a matter of brute forcing the
solutions. This was just iterating over the possible values of the three
dimensions and the number of layers, constraining them by some upper bound
(which I adjusted once or twice until I found a solution). One important
thing is that I did not consider identical shapes such as (1, 1, 2) vs 
(2, 1, 1) vs (1, 2, 1). The performance was not bad, it took 3.6s to run. The
brute force code is not particularly elegant, but it works and I could easily
generalize it if I wanted to.
"""
if __name__ == "__main__":
    print "Example (10) (expect 154):"
    print solve_p126(10, 200)
    print "Problem (1000):"
    print solve_p126(1000, 20000)