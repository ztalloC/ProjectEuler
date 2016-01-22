# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:23:38 2016

@author: mjcosta
"""

# Returns an infinite generator of fibonacci numbers.
def fibo_gen():
    a = 1L
    b = 1L
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c
        