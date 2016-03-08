# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:46:31 2016

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

# Computes the y value of the Blancmange curve at a given 0 <= x <= 1 for
# a given number of steps (the curve is a fractal).
def blancmange(x, steps):
    pow2 = 1
    s = lambda v: abs(round(v) - v)
    result = 0
    for i in xrange(steps):
        result += s(pow2 * x)/pow2
        pow2 *= 2
    return result
    
# Computes the lower y value of a point on a circle with a given center 
# coordinate and radius.    
def lower_circle(x, center_x, center_y, radius):
    return center_y - (radius**2 - (x - center_x)**2)**0.5
    
# Calculates the area under the blancmange curve enclosed by a circle with
# center at (0.25, 0.5) and radius 0.25. Uses numerical integration with the
# trapezoid method with dx being the width of the trapezoids and steps the
# number of steps for the blancmange curve.
@timefunc
def solve_p226(dx, steps):
    # Circle constants.
    cx = 0.25
    cy = 0.5
    rad = 0.25
    # Store the second point for the trapezoid method.
    x = 0.5 - dx
    prev_yb = 0.5
    prev_yc = 0.5
    result = 0
    # Iterate backwards until the blancmange drops below the circle.
    while prev_yb >= prev_yc:
        yb = blancmange(x, steps)
        yc = lower_circle(x, cx, cy, rad)
        # Compute area under each trapezoid slice and sum the differences.
        syb = dx * (prev_yb + yb)/2
        syc = dx * (prev_yc + yc)/2
        result += syb - syc
        x -= dx
        prev_yb = yb
        prev_yc = yc
    return result
    
"""
Thoughts: Not a difficult problem, though it was a nice review of numerical
integration. By definition of the blancmange curve, it would be hard to
analytically compute the integral, so one can just numerically compute it
instead. I just used the basic trapezoid method, starting at (0.5, 0.5) which
we know is one point of intersection, and moving backwards until we reach
the unknown second point of intersection. 

Then, it is just a matter of tuning the parameters (the width of the 
integration intervals and the number of iterations to compute the blancmange 
curve) until the sum stabilizes. I just did this by hand and eventually got the 
final solution. The performance is quite reasonable, taking only 3.7 seconds
to finish. The solution thread mostly had similar solutions with some
optimizations.
"""
if __name__ == "__main__":
    print "%.8f" % solve_p226(1e-6, 26)