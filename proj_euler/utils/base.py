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

# Converts from decimal to an arbitrary base b.
# Credit: http://stackoverflow.com/a/2267428    
def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])