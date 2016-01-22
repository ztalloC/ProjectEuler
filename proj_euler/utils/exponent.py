# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 07:56:53 2016

@author: mjcosta
"""

# A fast integer square root function using Newton's method. Credit to:
# http://stackoverflow.com/a/15391420
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
# Checks if x is a perfect square or not.
def perfect_square(x):
    v = isqrt(x)
    return v * v == x