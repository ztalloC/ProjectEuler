# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 07:44:51 2016

@author: mjcosta
"""

from math import sqrt

from proj_euler.utils.timing import timefunc

# Given two points on an ellipse, computes the next point on the ellipse
# where the ellipse is given as x^2/a^2 + y^2/b^2 = 1.
def compute_next_point(a, b, x0, y0, x1, y1):
    m_orig = (y1 - y0)/(x1 - x0)
    # The slope of the tangent of the ellipse is given as (-x/y)b^2/a^2
    # so the normal line is just -1/m.
    m_normal = y1 / x1 * (a * a)/(b * b)
    # http://stackoverflow.com/questions/17395860/how-to-reflect-a-line-over-another-line
    # where m1 is the line to reflect over and m2 is the line being reflected.
    # m3 = (m1^2*m2 + 2*m1 - m2) / (1 + 2*m1*m2 - m1^2)
    m_refl = (m_normal * m_normal * m_orig + 2 * m_normal - m_orig) \
        / (1 + 2 * m_normal * m_orig - m_normal * m_normal)
    # Compute slope intercept form of the reflected line.
    c = - m_refl * x1 + y1
    # Compute the intersection points
    # http://www.ambrsoft.com/TrigoCalc/Circles2/Ellipse/EllipseLine.htm
    # x = (-a^2*m*c +/- ab*sqrt(a^2m^2+b^2-c^2))/(a^2m^2+b^2)
    # y = (b^2*c +/- abm*sqrt(a^2m^2+b^2-c^2))/(a^2m^2+b^2)
    x_minus = (-a*a*m_refl*c - a*b*sqrt(a*a*m_refl*m_refl + b*b - c*c)) \
        / (a*a*m_refl*m_refl + b*b)
    x_plus = (-a*a*m_refl*c + a*b*sqrt(a*a*m_refl*m_refl + b*b - c*c)) \
        / (a*a*m_refl*m_refl + b*b)
    # We could just use the equation of the ellipes instead, but that
    # propagates floating point error twice rather than once.
    y_minus = (b*b*c - a*b*m_refl*sqrt(a*a*m_refl*m_refl + b*b - c*c)) \
        / (a*a*m_refl*m_refl + b*b)
    y_plus = (b*b*c + a*b*m_refl*sqrt(a*a*m_refl*m_refl + b*b - c*c)) \
        / (a*a*m_refl*m_refl + b*b)
    # We have two points but we don't know which one to use apriori, so just
    # use the one with the biggest difference.
    if ((x_minus - x1)**2 + (y_minus - y1)**2) \
        < ((x_plus - x1)**2 + (y_plus - y1)**2):
        return (x_plus, y_plus)
    else:
        return (x_minus, y_minus)

# Takes as input (a, b) for an ellipse of the form x^2/a^2 + y^2/b^2 = 1, the 
# entry point of the light beam (x0, y0), the initial target of the beam 
# (x1, y1), the width of the opening, and optionally the number of points 
# to print out.
@timefunc
def solve_p144(a, b, x0, y0, x1, y1, width, verbose = 10):
    # Note: (x1, y1) is an interior point, but we count the exit point as well
    # so use count = 0 instead of count = 1.
    count = 0
    prev_x = x0
    prev_y = y0
    curr_x = x1
    curr_y = y1
    while not (curr_y > 0 and curr_x <= width and curr_x >= -width):
        new_x, new_y = compute_next_point(a, b, prev_x, prev_y, curr_x, curr_y)
        prev_x, prev_y = (curr_x, curr_y)
        curr_x, curr_y = (new_x, new_y)
        count += 1
        if verbose is not None and count <= verbose:
            print count, (curr_x, curr_y)
    return count

"""
Thoughts: I haven't worked with ellipses in a long time, so this was a nice
refresher. The problem was mostly getting the equations correct rather than
any computational challenge. I had to look up a bunch of equations such as
how to reflect a line across another and the intersection of a line with
an ellipse. I did not want to use trigonometry since trig operations are slow
and I tried to minimize floating point error. This was one of the reasons why
I looked up equations rather than trying it myself (I could have done it with
trig). I have the feeling that I might have to re-use this code in the future,
so I wrote it fast now, rather than having to rewrite it later. 
"""
if __name__ == "__main__":
    # Note: 4x^2 + y^2 = 100 <=> x^2/5^2 + y^2/10^2 = 1       
    print solve_p144(5, 10, 0, 10.1, 1.4, -9.6, 0.01, verbose = 10)