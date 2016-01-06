# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 07:23:56 2015

@author: mjcosta
"""

import numpy as np
import itertools
import optparse

from proj_euler.utils.timing import timefunc

class Sudoku:
    """
    Constructor for Sudoku instance, represents a sudoku grid.
    """
    def __init__(self, data, elim=None, unsolved=None):
        if elim is None:
            # Initialise the solution grid.
            self.grid = np.zeros((9,9), dtype=int)
            # Count the unsolved squares
            self.unsolved_squares = 9*9
            # Initially assume that it is solvable
            self.solvable = True
            # Initialise the elimination grid.
            self.elimination = np.zeros(self.grid.shape+(9,), dtype=int)
            # For all non-zero values, just place them
            nz = np.where(data != 0)
            nz = zip(nz[0], nz[1])
            for c in nz:
                self.place_location(c[0], c[1], data[c])
        else:
            self.grid = np.array(data)
            self.elimination = np.array(elim)
            self.solvable = True
            self.unsolved_squares = unsolved
            
    """
    Creates a Sudoku instance from a string representing a grid.
    """
    @classmethod
    def from_grid_str(cls, grid_str):
        lines = grid_str.split('\n')
        lines = [map(lambda x: int(x), line.strip()) for line in lines]
        data = np.array(lines)
        return cls(data)

    """
    Creates a Sudoku instance from another Sudoku grid.
    """
    @classmethod
    def from_sudoku(cls, sudoku):
        return cls(sudoku.grid, sudoku.elimination, sudoku.unsolved_squares)
        
    """
    Given a coordinate, returns the coordinates of all items in the same
    3x3 grid.
    """
    @staticmethod
    def _get_box_coords(i, j):
        box_i = i // 3
        box_j = j // 3
        return itertools.product(range(box_i*3, box_i*3+3),
                                 range(box_j*3, box_j*3+3))
    
    """
    Places an item in a given coordinate.
    """
    def place_location(self, i, j, v):
        # If solved, don't try to do anything
        if self.is_solved():
            return
        
        # If already eliminated, then don't try
        if self.elimination[i,j,v-1] and self.grid[i,j] == 0:
            self.solvable = False
        
        # If still solvable, then place it and eliminate it
        if self.solvable:
            self.grid[i,j] = v
            self._eliminate(i, j, v)
            self.unsolved_squares -= 1
    
    """
    Checks whether the sudoku grid is solved.
    """
    def is_solved(self):
        return self.unsolved_squares == 0
    
    """
    Performs an elimination given a grid coordinate and a value.
    """
    def _eliminate(self, i, j, v):
        # The row and column can't have v anymore
        self.elimination[i,:,v-1] = 1
        self.elimination[:,j,v-1] = 1
        # The grid square can't have v in it
        grid_cs = self._get_box_coords(i, j)
        for (b_i,b_j) in grid_cs:
            self.elimination[b_i,b_j,v-1] = 1
        # Also this position can't have anything in it
        self.elimination[i,j,:] = 1
        # At the end, check if it is still solvable
        self._check_solvability()        
        
    """
    Updates the solvability status of the grid.
    """
    def _check_solvability(self):
        # We only consider locations that are unsolved but can't be solved
        # It is possible that there is an invalid location, but we don't
        # check for that here.
        if self.solvable:
            impossible = (self.grid == 0) & (self.elimination.sum(axis=2) == 9)
            if np.sum(impossible) != 0:
                self.solvable = False

    """
    Checks if any numbers are forced to be placed by nature of being the
    only spot for that number (even if others could potentially go there).
    Returns a list of such coordinate values.
    """
    def _check_forced_square(self):
        result = []
        for i in range(3):
            for j in range(3):
                for value in range(9):
                    grid = self.elimination[i*3:i*3+3, j*3:j*3+3,value]
                    remaining = 9 - grid.sum()
                    if remaining == 1:
                        # Get the coordinate
                        local = np.where(grid == 0)
                        local = (local[0][0],local[1][0])
                        coord = (local[0]+i*3, local[1]+j*3, value+1)
                        result.append(coord)
        return result
                        
    """
    Solves the Sudoku grid.
    """
    def solve_grid(self):
        # Continue until the grid is solved or unsolvable
        while not self.is_solved() and self.solvable:
            # Get the number of possibilities for each coordinate
            remaining = 9 - self.elimination.sum(axis=2)
            # We want to get the minimum value that is not 0, so just
            # temporarily set those to 10 so we ignore them
            remaining[remaining == 0] = 10
            min_val = remaining.min()
            # Get all the coordinates of entries with min values
            min_coords = np.where(remaining == min_val)
            min_coords = zip(min_coords[0], min_coords[1])
            # If min_val is 1 then just place the values, getting the possible
            # value and setting it
            if min_val == 1:
                # Get all the locations and then place all at once
                new_locs = []
                for mc in min_coords:
                    new_entry = np.where(self.elimination[mc] == 0)[0][0]+1
                    new_locs.append((mc[0],mc[1],new_entry))
                # Do it in two steps since an invalid configuration can
                # prevent one from being placed                  
                for (i,j,v) in new_locs:
                    self.place_location(i,j,v)
                    # Stop if unsolvable
                    if not self.solvable:
                        break

            else:
                # Check if we can force any values
                forced = self._check_forced_square()
                if len(forced) > 0:
                    for (i,j,v) in forced:
                        self.place_location(i, j, v)
                else:
                    # Otherwise we need to guess and check...
                    # So we'll only guess one location
                    guess_loc = min_coords[0]
                    pos_vals = np.where(self.elimination[guess_loc] == 0)[0]
                    pos_vals = [x+1 for x in pos_vals]
                    for guess in pos_vals:
                        # Create a new Sudoku instance and try solving it.
                        sudoku = Sudoku.from_sudoku(self)
                        sudoku.place_location(guess_loc[0], 
                                              guess_loc[1], guess)
                        sudoku.solve_grid()
                        # If solved, replace ourself with this answer
                        if sudoku.is_solved():
                            self.grid = sudoku.grid
                            self.elimination = sudoku.elimination
                            self.unsolved_squares = 0
                            return
                        # Guess was wrong, couldn't solve, so just continue on
                    # If we reach this point, then assume it was unsolvable
                    self.solvable = False
 
"""
Solves project euler 96 given the name of the file to read sudoku puzzles
from as input.
"""
@timefunc
def solve_p96(input_name):
    result = 0

    with open(input_name) as f:
        lines = [line.strip() for line in f]
        for i in range(len(lines)/10):
            s = ""
            for j in range(9):
                s += lines[i*10+1+j] + "\n"
            s = s.strip()
            sudoku = Sudoku.from_grid_str(s)
            sudoku.solve_grid()
            # For project euler, sum the 3 digit numbers in the top left corner
            result += int(''.join([str(x) for x in sudoku.grid[0,0:3]]))
        return result

"""
Thoughts: Overall the problem was not that difficult but took a reasonable
amount of code. The main difficulty was finding a good representation of
the sudoku puzzle and then I made various mistakes which made it take longer
(such as accidentally making shallow copies when making guesses). I did
learn more about how numpy.where works, so that was useful overall.

It seems that other people who solved this problem just brute forced it
which is probably reasonable given an efficient implementation.
"""
if __name__ == "__main__":
    # Read the data, accepting alternate data sources as input
    optparser = optparse.OptionParser()
    optparser.add_option("-i", "--input", dest="input", 
        default="data/p096_sudoku.txt", help="Sudoku puzzles")
    (opts,_) = optparser.parse_args()

    # Get the result and time it took
    result = solve_p96(opts.input)
    print "The answer is: %d" % (result)