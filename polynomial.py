from itertools import zip_longest
import math


class Polynomial:
    def __init__(self, *coefficients):
        if len(coefficients) == 1:
            coefficients = coefficients[0]
        if isinstance(coefficients, Polynomial):
            self.coefficients = coefficients.coefficients
        elif isinstance(coefficients, int):
            self.coefficients = [coefficients]
        elif isinstance(coefficients, dict):
            mydict = coefficients
            deg = max(map(int, mydict.keys()))
            self.coefficients = [
                mydict[i] if i in mydict else 0 for i in range(deg + 1)]
        else:
            self.coefficients = list(coefficients)
        while self.coefficients[-1] == 0 and len(self.coefficients) > 1:
            self.coefficients.pop()
        if not self.coefficients:
            self.coefficients = [0]

    def __repr__(self):
        return "Polynomial " + str(self.coefficients)

    def __str__(self):
        res = ''
        for i in reversed(range(len(self.coefficients))):
            coeff = self.coefficients[i]
            if coeff:
                if coeff > 0:
                    res += '+'
                else:
                    res += '-'
                if abs(int(coeff)) != 1 or i == 0:
                    res += str(abs(int(coeff)))
                a = self.coefficients.index(coeff)
                if i != 0:
                    res += 'x'
                if i > 1:
                    res += '^' + str(i)
        return '0' if not res else res.lstrip('+')

    def __eq__(self, other):
        c1 = self.coefficients[:]
        c2 = other.coefficients[:]
        if len(c1) != len(c2):
            return False
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                return False
        return True

    def __add__(self, other):
        c1 = self.coefficients
        c2 = Polynomial(other).coefficients
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(res)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        res = [-t for t in self.coefficients]
        return Polynomial(res)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __call__(self, x):
        return sum([self.coefficients[i] * x ** i for i in range(len(self.coefficients))])

    def degree(self):
        return len(self.coefficients) - 1
    
    #def der(self, d=1):

    #def __mul__(self, other):

    #def __rmul__(self, other):

    #def __mod__(self, other):

    #def __rmod__(self, other):

    #def gcd(self, other):

    #def __iter__(self):

    #def __next__(self):

