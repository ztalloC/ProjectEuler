# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:51:30 2015

@author: mjcosta
"""

import optparse

# Expands subtractions to facilitate further transformations, the result is
# not necessarily valid.
def expand_subtractions(s):
    # I can only appear before V and X
    # X can only appear before L and C
    # C can only appear before D and M
    return s.replace("IV", "IIII") \
        .replace("IX", "VIIII") \
        .replace("XL", "XXXX")  \
        .replace("XC", "LXXXX") \
        .replace("CD", "CCCC") \
        .replace("CM", "DCCCC") 

# Given a string of roman numerals, sorts the numerals into descending order
# Should not be used on strings containing subtractions
def sort_numerals(s):
    value = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    return "".join(sorted(s, key = lambda x: value[x], reverse = True))

# Given a string of roman numerals, performs substitutions to reduce length
def perform_substitutions(s):
    return s.replace("IIIII", "V") \
        .replace("VV", "X") \
        .replace("XXXXX", "L") \
        .replace("LL", "C") \
        .replace("CCCCC", "D") \
        .replace("DD", "M")

# Given a string of roman numerals, inserts subtractions where possible
# to reduce the length
def insert_subtractions(s):
    # Perform in reverse order as in previous function
    return s.replace("DCCCC", "CM") \
        .replace("CCCC", "CD") \
        .replace("LXXXX", "XC") \
        .replace("XXXX", "XL") \
        .replace("VIIII", "IX") \
        .replace("IIII", "IV")

# Computes the optimal roman numeral
def compute_optimal(s):
    t = expand_subtractions(s)
    t = sort_numerals(t)
    t = perform_substitutions(t)
    return insert_subtractions(t)

"""
Thoughts: Overall fairly straightforward, just string manipulation. My solution
is a little verbose but it's clear why it works. Probably could have removed
sort_numerals and combined the others into a single function.
"""
if __name__ == "__main__":
    # Read the data, accepting alternate data sources as input
    optparser = optparse.OptionParser()
    optparser.add_option("-i", "--input", dest="input", 
        default="data/p089_roman.txt", help="Roman numerals")
    (opts,_) = optparser.parse_args()

    lines = [line.strip() for line in open(opts.input)]
    red_lines = [compute_optimal(x) for x in lines]
    red_length = [len(x)-len(y) for (x,y) in zip(lines, red_lines)]
    print sum(red_length)