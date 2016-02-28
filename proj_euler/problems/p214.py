# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:11:40 2016

@author: mjcosta
"""

from proj_euler.utils.ntheory import generate_totient
from proj_euler.utils.timing import timefunc

def totient_length(n, totients, mem):
    if n in mem:
        return mem[n]
        
    if n == 1:
        result = 1
    else:
        t = totients[n-1]
        result = 1 + totient_length(t, totients, mem)
    mem[n] = result
    return result

@timefunc
def solve_p214(plimit, chain):
    result = 0
    totients = generate_totient(plimit)
    mem = dict()
    for i in xrange(len(totients)):
        # Test primality by checking if totient(p) == p-1 and p % 2 != 0 (or
        # p = 2)
        if i == totients[i] and (i+1 == 2 or (i+1) % 2 != 0):
            clen = totient_length(i+1, totients, mem)
            if clen == chain:
                result += (i+1)
    return result

"""
Thoughts: Very simple problem. Just sieve the totients under 40 million,
compute the prime chain lengths, and sum the results. The final running time
is 33 seconds which isn't great, but isn't terrible either. The totient
sieve function can be optimized (and is where most of the time is spent), 
so that is the main area of improvement.
"""
if __name__ == "__main__":
    print "Example (p < 20, l = 4) (expect 5 + 7 = 12):"
    print solve_p214(20, 4)
    print "Problem (p < 4*10^7, l = 25):"
    print solve_p214(4*10**7, 25)
