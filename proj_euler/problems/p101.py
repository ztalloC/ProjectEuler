# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:41:20 2015

@author: mjcosta
"""

from proj_euler.utils.timing import timefunc

class NewtonPolynomial:
    def __init__(self):
        self.table = []
        self.coefs = []
        self.xs = []
    
    def add_point(self, x, y):
        if x in self.xs:
            raise ValueError("No duplicate xs are allowed.")
            
        # No points, just use a constant expression
        if len(self.coefs) == 0:
            self.coefs.append(y)
            self.table.append(y)
            self.xs.append(x)
        # Calculate the divided difference and update the table
        else:
            new_table = [y]
            i = 0
            while i < len(self.table):
                diff = (new_table[i]-self.table[i])/(x-self.xs[-i-1])
                new_table.append(diff)
                i += 1
            self.table = new_table
            self.coefs.append(new_table[-1])
            self.xs.append(x)
        
    def evaluate(self, x):
        if len(self.coefs) == 0:
            raise ValueError("Polynomial needs at least one point.")
            
        xacc = 1
        result = 0
        i = 0
        while i < len(self.coefs):
            result += self.coefs[i]*xacc
            xacc *= (x-self.xs[i])
            i += 1
        return result
        
        
# Given a polynomial in the form of a dictionary, evaluates that polynomial
# for a given x.
def evaluate_poly(coefs, x):        
    return sum(coefs[k]*(x**k) for k in coefs)    
    
"""
Given coeficients of a polynomial for a_k*x^k+a_(k-1)*x^(k-1)+...+a_1*x
in a dictionary of the form {k:a_k}, calculates the sum of the BOPs for
the polynomial.
"""
@timefunc
def solve_101(coefs):
    max_k = max(coefs)
    # Generate one extra value for comparing against last value.
    xs = range(1,max_k+2)
    ys = [evaluate_poly(coefs, x) for x in xs]
    polyfit = NewtonPolynomial()
    result = 0
    i = 0
    while i < max_k:
        polyfit.add_point(xs[i], ys[i])
        yhat = polyfit.evaluate(xs[i+1])
        result += yhat
        # Problem doesn't define what happens if its actually correct
        # so just print it out and we'll see if it happens
        if ys[i+1] == yhat:
            print "correct: ", i, xs[i+1], yhat
        i += 1
    return result

"""
Thoughts: After having difficulty finishing up the 90s, the first problem
in 100+ was refreshingly easy. This was just fitting some polynomials to
a set of points and summing the first value outside the interpolated range.
Given that I am familiar with polynomial interpolation, this was very easy
and a nice refresher on what I learned in class years ago. The result took
less than 1ms to run, but the input size was very small. I ended up writing
a reasonable amount of code, but I figured that I might need it in the future
(and in that case I might move it to another file).
"""
if __name__ == "__main__":
    example = {3:1}
    print "Example fit"
    r_example = solve_101(example)
    print r_example
    actual = {0:1,1:-1,2:1,3:-1,4:1,5:-1,6:1,7:-1,8:1,9:-1,10:1}
    print "Actual fit"
    r_actual = solve_101(actual)
    print r_actual