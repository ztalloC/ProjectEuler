# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 09:15:44 2015

@author: mjcosta
"""

from functools import wraps
import time

def timefunc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()        
        result = func(*args, **kwargs)
        end = time.time()
        print "%s took %f seconds." % (func.__name__, end-start)
        return result
    return wrapper

"""
Given code to run, runs it and returns the time and the results of the code
in the form (results, time).

Deprecated, use the timefunc decorator.
"""
def time_code(f):
    start = time.time()
    results = f()
    end = time.time()
    return (results, end-start)
