# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:09:12 2016

@author: mjcosta
"""

# A decorator that provides memoization for a general function.
class memoize:
    def __init__(self, f):
        self.f = f
        self.mem = dict()
    def __call__(self, *args):
        if args not in self.mem:
            self.mem[args] = self.f(*args)
        return self.mem[args]