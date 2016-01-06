# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:24:35 2016

@author: mjcosta
"""

import argparse

from collections import namedtuple
from collections import defaultdict

from proj_euler.utils.timing import timefunc

WeightEdge = namedtuple('WeightEdge', 'src, dest, weight')

# Given a list of strings, parses the data into a list of edges
def parse_graph(data):
    output = []
    for i, line in enumerate(data):
        entries = line.strip().split(",")
        for j, v in enumerate(entries):
            if v != '-':
                output.append(WeightEdge(src=i, dest=j, weight=int(v)))
    return output
    
# Given the list of edge data, calculates the minimum spanning tree using
# Prim's algorithm.
def prim_mst(edges):
    # Store the nodes to be added to the MST
    remaining_nodes = set()
    # Go through and store the edges for each node and get the full node set
    graph = defaultdict(list)
    for e in edges:
        graph[e.src].append(e)
        remaining_nodes.add(e.src)

    # Store the resulting MST as a list of edges
    mst = []
    # First, choose an arbitrary node from the graph as the initial vertex
    remaining_nodes.remove(edges[0].src)
    # Initialize the list of edges to choose from
    weight_key = lambda x: x.weight
    curr_edges = sorted(graph[edges[0].src], key=weight_key)
    # Add edges until all of them are in the tree or no edges to consider.
    while len(remaining_nodes) > 0 and len(curr_edges) > 0:
        # Pull edges from the current list, we maintain the invariant that
        # all source nodes in this list are part of the MST, sorted by weight.
        cheapest = curr_edges.pop(0)
        # Found a node to add to the tree
        if cheapest.dest in remaining_nodes:
            mst.append(cheapest)
            remaining_nodes.remove(cheapest.dest)
            # Add the new node's edges to the list of edges to consider
            curr_edges.extend(graph[cheapest.dest])
            # Merge the new edges in and re-sort, since Timsort makes use of
            # sorted runs in the data, this isn't bad compared to a more
            # sophisticated data structure.
            curr_edges.sort(key=weight_key)
    return mst

@timefunc    
def solve_p107(data):
    edges = parse_graph(data)
    mst = prim_mst(edges)
    print mst
    # Compute the difference in weights, for the original, remember that
    # there are two directed edges per undirected edge, so divide by two.
    weight_orig = sum(e.weight for e in edges)/2
    weight_mst = sum(e.weight for e in mst)
    return weight_orig - weight_mst

"""
Thoughts: This was a nice refresher for Minimum Spanning Tree algorithms.
Overall the problem was very simple (just implement a MST algorithm). I used
a very simple data structure which worked fine for the problem. In practice,
there are more sophisticated data structures that result in better running
times. Given that the problem size was very small (only 40 nodes), it wasn't
a huge deal.
"""
if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", dest="input", 
        default="data/p107_network.txt", help="Network")
    args = argparser.parse_args()
    data = open(args.input).readlines()
    print solve_p107(data)