# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:11:00 2016

@author: mjcosta
"""

from __future__ import division

from proj_euler.utils.timing import timefunc

# Generates the sequence defined in project euler 186.
def sequence():
    values = []
    for k in xrange(1, 56):
        val = (100003 - 200003*k + 300007*(k**3)) % 1000000
        yield val
        values.append(val)
    while True:
        val = (values[-24] + values[-55]) % 1000000
        yield val
        values.pop(0)
        values.append(val)

# A Union-Find data structure with path compression.
class Node:
    def __init__(self, val):
        self.val = val
        self._rank = 0
        self._count = 1
        self._parent = self
    
    def find(self):
        if self._parent == self:
            return self
        else:
            self._parent = self._parent.find()
            return self._parent
        
    @staticmethod
    def union(x, y):
        xRoot = x.find()
        yRoot = y.find()
        if xRoot._rank < yRoot._rank:
            xRoot._parent = yRoot
            yRoot._count += xRoot._count
        elif xRoot._rank > yRoot._rank:
            yRoot._parent = xRoot
            xRoot._count += yRoot._count
        elif xRoot != yRoot:
            xRoot._parent = yRoot
            yRoot._count += xRoot._count
            yRoot._rank += 1
            
    def count(self):
        return self.find()._count

@timefunc
def solve_p186(pm_num=524287, ratio=0.99):
    rgen = sequence()
    total = 10**6
    success = 0
    friends = dict()
    while pm_num not in friends or friends[pm_num].count()/total < ratio:
        caller, called = next(rgen), next(rgen)
        # Invalid call.
        if caller == called:
            continue
        success += 1
        # Create the nodes if not already present.
        if caller not in friends:
            friends[caller] = Node(caller)
        if called not in friends:
            friends[called] = Node(called)
        Node.union(friends[caller], friends[called])
    return success

"""
Thoughts: Fairly straightforward problem, we want to generate random numbers
until the prime minister is in a connected sub-graph containing 99% of users.
The key is coming up with an efficient data structure for joining sets, which
is well-known in Kruskal's MST algorithm. The data structure I used is the
standard union-find structure with path compression and balanced trees. Once
the data structure is done, the rest of the problem is trivial.

The runtime of the code is about 24 seconds, which is reasonable. It is
possible to speed up the code by encoding everything as a list, but it comes at
the price of readability. If one really wanted to speed up the code, one should
simply write in a lower level language like C/C++ or Java.
"""
if __name__ == "__main__":
    print solve_p186()