# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:37:59 2016

@author: mjcosta
"""

from proj_euler.utils.pythag import primitive_pythag_perim
from proj_euler.utils.timing import timefunc

@timefunc
def solve_p139(plimit):
    # One-liner version.
    return sum(int(plimit/(a + b + c)) for (a, b, c) in \
        primitive_pythag_perim(plimit) if c % (b - a) == 0)
    """
    # Standard version.
    result = 0
    # Simply generate the primitive pythagorean triples, test the property,
    # and add all the multiples.
    for (a, b, c) in primitive_pythag_perim(plimit):
        if c % (b - a) == 0:
            result += int(plimit/(a + b + c))
    return result
    """

"""
Thoughts: The problem was not particularly difficult, but it was useful. It was
just a matter of writing code that efficiently generates Pythagorean triples.

I used Euclid's method to generate primitive pythagorean triples where given 
m > n > 0, one can generate a triple: (m^2 - n^2, 2 * m * n, m^2 + n^2). By
itself, this method does not generate all pythagorean triples, but it does
generate all primitive pythagorean triples. If you add the restrictions that
one of m and n must be even and the other odd, as well as gcd(m, n) == 1, then
you can generate only primitive triples. Generating all triples can be done by
simply taking multiples of the primitive triples. The code I wrote could be
slightly more efficient since when I compute n, I simply increment by 2 (for
the given parity) and test the gcd. Instead, there are methods for generating
coprime pairs of numbers, that I could have used, but this is sufficient for
now.

After writing the Pythagorean triple code, it was just a matter of testing
whether the difference between the two side lengths divides the hypotenuse.
Note that in this case it is sufficient to test the primitives and just add
the number of multiples under the perimiter limit. This is because if the
primitive does not satisfy the property, then neither will any multiple of it
(and vice versa). It takes around 10 seconds to run (probably because of the
number of primitives to test), which isn't bad but could be better. I was able
to write a one-liner for it (given the primitive generation code).
"""
if __name__ == "__main__":
    print solve_p139(1e8)