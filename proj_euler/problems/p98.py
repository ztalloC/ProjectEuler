# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 07:23:56 2015

@author: mjcosta
"""

import optparse
from proj_euler.utils.timing import timefunc
from collections import defaultdict
import itertools

# Given a comma separated string of quoted words, returns a list of words
def parse_word_input(s):
    return [x.strip('"') for x in s.split(',')]

# Given a list of words, generates a dictionary containing anagrams for
# a given set of letters
def gen_anagram_dict(words):
    result = defaultdict(set)
    for w in words:
        key = tuple(sorted(w))
        result[key].add(w)
    return result
        
# Generates a list of square values and groups them based on length, takes
# the list of words to determine the max value to generate
def gen_square_dict(words):
    result = defaultdict(set)
    maxlen = max(len(w) for w in words)
    limit = 10**maxlen
    i = 0
    while i**2 < limit:
        val = i**2
        s = str(val)
        digits = len(s)
        result[digits].add(s)
        i += 1
    return result

# Given a word, creates a mapping from the first word to the number, returns
# the mapping of the second word. Returns None if a number is used by different
# letters in the word.
def subst_words(w1, w2, n1):
    m1 = dict()
    m2 = dict()
    out = ''
    for (c, d) in zip(w1, n1):
        if d in m1 and m1[d] != c:
            return None
        m1[d] = c
        m2[c] = d
    for c in w2:
        out += m2[c]
    return out

# Given the word list, computes the maximum square number resulting from
# comparing two words
def max_anagram_squares(words):
    anagrams = gen_anagram_dict(words)
    squares = gen_square_dict(words)
    best = 0
    # Only need to consider words we know are anagrams
    for k in anagrams:
        if len(anagrams[k]) < 2:
            continue
        digits = len(k)
        for (a1, a2) in itertools.combinations(anagrams[k], 2):
            # Try substituting each number string
            for val in squares[digits]:
                subst = subst_words(a1, a2, val)
                if subst is not None and subst in squares[digits]:
                    sval = int(subst)
                    ival = int(val)
                    bval = max(sval, ival)
                    if bval > best:
                        print a1, a2, ival, sval
                        best = bval
    return best

@timefunc
def solve_p98(fname):
    s = open(fname).read()
    words = parse_word_input(s)
    best = max_anagram_squares(words)
    return best    

"""
Thoughts: I tried to solve the problem as fast as possible and it took
about 30 minutes to solve. The solution I used was to simply brute force
the problem with a few simple ideas to reduce the search space. All I did
was compare anagrams of a given set of characters with each other, performed
the substitution, tested if the result was also a square result, and stored
the best such value. 
"""
if __name__ == "__main__":
    # Read the data, accepting alternate data sources as input
    optparser = optparse.OptionParser()
    optparser.add_option("-i", "--input", dest="input", 
        default="data/p098_words.txt", help="Word list")
    (opts,_) = optparser.parse_args()
    print solve_p98(opts.input)