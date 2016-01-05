# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:07:18 2015

@author: mjcosta
"""

from collections import namedtuple
from proj_euler.utils.timing import timefunc
import argparse


# Represents a point in a two dimensional plane
Point = namedtuple('Point', ['x', 'y'])

# Tests if a point is inside a triangle defined by three points
# Works by calculating the barycentric coordinates of tp in terms of the
# other points and checking if > 0
# https://stackoverflow.com/questions/2049582/how-to-determine-a-point-in-a-triangle/2049712#2049712
def in_triangle(tp, p0, p1, p2):
    A =  (-p1.y * p2.x + p0.y * (-p1.x + p2.x) + p0.x * (p1.y - p2.y) + p1.x * p2.y)/2
    sign = -1 if A < 0 else 1
    s = (p0.y * p2.x - p0.x * p2.y + (p2.y - p0.y) * tp.x + (p0.x - p2.x) * tp.y) * sign
    t = (p0.x * p1.y - p0.y * p1.x + (p0.y - p1.y) * tp.x + (p1.x - p0.x) * tp.y) * sign
    return s > 0 and t > 0 and (s + t) < (2 * A * sign)

# Given a list of points
@timefunc
def solve_p102(data):
    result = 0
    origin = Point(0, 0)
    for line in data:
        # Parse into points and check the result
        vals = [int(x) for x in line.split(",")]
        p0 = Point(vals[0],vals[1])
        p1 = Point(vals[2],vals[3])
        p2 = Point(vals[4],vals[5])
        if in_triangle(origin, p0, p1, p2):
            result += 1
    return result
    
"""
Thoughts: Really easy problem. I knew you could test if a point lies within
a triangle by looking at the signs of cross products, but I decided to look
up a faster method instead. After righting the function, it was just a matter
of counting the triangles.
"""
if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", dest="input", 
        default="data/p102_triangles.txt", help="Triangles")
    args = argparser.parse_args()
    data = open(args.input).readlines()
    print solve_p102(data)