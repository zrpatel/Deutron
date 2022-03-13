# Class representing a polynomial of a single variable
# It has a list of coefficients coefs
class Polynomial:
    def __init__(self, coefs):
        this.coefs = coefs

    # Evaluates the polynomial at x.
    # So e.g. for the polynomial representing x^3 + 3x + 1
    # evaluate(0) returns 1
    # evaluate(1) returns 5
    # evaluate(2) returns 15
    def evaluate(self, x):
        # To implement

    # Adds two polynomials (self and other) 
    def add(self, other):
        # To implement

    # Multiplies the polynomial by a constant factor
    # You can use this and add to implement subtract
    def scale(self, scalar):
        # To implement

    # Subtracts other from self.
    def subtract(self, other):
        return self.add(other.scale(-1))

    # Multiplies self by other
    def multiply(self, other):
        # To implement

    # Take the derivative of self
    def derivative(self):
        # To implement