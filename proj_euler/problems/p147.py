# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:27:45 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Given (m, n), computes the number of additional rectangles possible in the
# diagonal grid compared to (m-1, n). Assumes m >= n. 
def additional_rects(m, n):
    count = 0
    # There are (n - 1) 1x1 rectangles added to the bottom (between new 
    # squares) these can form larger rectangles based on their position.
    for j in xrange(1, n):
        # The size of the rectangles depend on the distance from the left and
        # right sides. Because of the assumption l + r = n <= m, this gets rid
        # of a lot of special cases where height restricts the rectangle length
        # The number of rectangles possible is simply the area of the bounding 
        # rectangle because we fix one point and can select width * height 
        # possible other points.
        count += 4 * j * (n - j)
    # There are n 1x1 rectangles added between the bottom edge of the old
    # rectangle and the new squares.
    for j in xrange(n):
        # These squares have their bottom vertex in the middle of squares
        pos = 1 + 2*j
        # Area of the bounding rectangle is same as before.
        rects = pos * (2*n - pos)
        # But, if m == n, then the top point is out of bounds, so just omit it.
        if m == n:
            rects -= 1
        count += rects
    return count

# Computes the number of all possible rectangles in cross-hatched grids less
# than or equal to rows x column size.
@timefunc
def solve_p147(rows, columns, verbose=True):
    result = 0
    diag_counts = dict()
    # The diagonal code assumes m >= n, so swap if m < n.
    if rows < columns:
        rows, columns = columns, rows
    for m in xrange(1, rows+1):
        for n in xrange(1, min(m+1, columns+1)):
            # The number of horizontal and vertical rectangles is simply
            # (m choose 2)*(n choose 2) or m*(m+1)*n*(n+1)/4
            rects = m*(m+1)*n*(n+1)/4
            if m == 1:
                # One row implies n - 1 diagonal rects (which is 0 if n <= m).
                diags = n - 1
            else:
                # Otherwise, we can compute the number of new diagonals added
                # by adding a new row.
                new_diags = additional_rects(m, n)
                # Get the old diags, we store tuples (m, n) s.t. m >= n.
                if m > n:
                    old_diags = diag_counts[(m-1, n)]
                # If m == n, then (m - 1) < n, so reverse the tuple.
                else:
                    old_diags = diag_counts[(n, m-1)]
                diags = old_diags + new_diags
            diag_counts[(m, n)] = diags
            total = rects + diags
            if verbose:
                print (m, n, total)
            # Double counts if the reversed tuple is also valid (but not equal)
            if m != n and n <= rows and m <= columns:
                result += total * 2
            else:
                result += total
    return result

"""
Thoughts: This was an annoying problem that took me a while to solve. There
actually is not that much code, it's just hard to understand without comments.
The time is quite fast as well (4 ms), but there really is not much to compute
rather than just getting it right.

The basic idea is to count the horizontal and vertically aligned rectangles
and then count the diagonally aligned rectangles. The horizontal and vertical
rectangles are quite easy, as one can form a rectangle by selecting any two
horizontal lines and any two vertical lines for (m choose 2)*(n choose 2) =
m*(m+1)*n*(n+1)/4 possible rectangles.

The diagonally aligned rectangles are much harder to wrap your mind around.
Intuitively, one can just rotate the picture by 45 degrees and then compute
the possible rectangles for that shape. But, that isn't obvious either. 

The method I used was to consider the rectangles where m >= n and consider how
many new sub-rectangles are possible when compared to the rectangle of size
(m - 1, n). There are (n - 1) 1x1 squares formed horizontally between each of 
the columns in the new row and n 1x1 squares formed vertically between the new
row and the old bottom row. 

For each of the (n - 1) rectangles, one can follow the lines from the bottom 
point to the left and right sides. Then, one can form a rectangle with these
two lines. This bounding rectangle represents all possible rectangles that can
be formed using a given new "bottom" rectangle. Because we assumed m >= n,
we never have to worry about the case where this bounding rectangle exits the
grid through the top. So for each of (n - 1) rectangle, we simply add the
product of the distances from the left and right side. We also multiply by 4
since each grid square contributes to 2 diagonal squares, so 2*2 = 4.

Each of the n rectangles have a bottom point in the middle of each of the new 
grid squares. We do not want to double count with the (n - 1) rectangles, so
we want to count all possible rectangles formed above the bottom point. The
idea is the same as the (n - 1) rectangles where we form rectangles by
considering the bounding rectangle. Since the bottom point is in the middle
of a grid square, we include the 2x multiplier and add 1 to get a position.
Then, as before, we simply use the area of the bounding rectangle. However,
because the bottom vertex is in the middle of a grid square, it is also
slightly higher and it is possible for the top vertex of the bounding rectangle
to exit the grid. This happens if m == n, so in that case we simply subtract 1.

Now we can compute the change in the number of diagonal squares, so it is easy
to compute the number of diagonally aligned squares. For grids where m = 1, the
number of diagonal squares is simply n - 1, which we use as a starting point.
The requirement that m >= n does not matter since the computation is symmetric,
so we can just double count as needed. Thus, we are done.

As an aside, there is in fact a closed form formula for computing the number
of diagonally aligned rectangles. It came up in the solutions thread for the
problem, but it is unlikely that someone would come up with it without working
out the problem in some other method and then deriving it. For reference, this
formula is: n*((2m-n)*(4n^2-1)-3)/6. Other methods used included brute force
and recursive formulas.
"""
if __name__ == "__main__":
    print "Example (3 x 2) (expect 72):"
    print solve_p147(3, 2, False)
    print "Problem (47 x 43):"
    print solve_p147(47, 43, False)