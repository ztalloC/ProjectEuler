# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:26:43 2016

@author: mjcosta
"""

import argparse

from proj_euler.utils.timing import timefunc
from proj_euler.problems.p103 import check_special_sumset

# Given a list of strings representing the data, computes the sum of the
# special sum sets.
@timefunc
def solve_p105(data):
    result = 0
    for line in data:
        # Parse the string into a list of numbers.
        vals = [int(x) for x in line.split(',')]
        # Simply add the sum if the set passes the test.
        if check_special_sumset(vals):
            result += sum(vals)
    return result

"""
Thoughts: Problems 103, 105, and 106 are related to one another. When I first
saw 103, I decided to check 105 and 106 to see if I could get hints/structure
my work to be re-usable. As it turned out, a component from 103 could be used
for 105, making it trivial. I actually solved 105 before 103 since it allowed
me to test my code.
"""  
if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", dest="input", 
        default="data/p105_sets.txt", help="Sets")
    args = argparser.parse_args()
    data = open(args.input).readlines()
    print solve_p105(data)