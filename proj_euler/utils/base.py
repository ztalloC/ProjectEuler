# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:46:48 2016

@author: mjcosta
"""

# Converts from decimal to a binary string representation.
def dec_to_bin(d):
    return "{0:b}".format(d)
    
# Converts from a binary string to a decimal representation.
def bin_to_dec(b):
    return int(b, 2)