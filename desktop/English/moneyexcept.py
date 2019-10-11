#!/usr/bin/env python3

class Money(object):
    """ a Money class.  Keeps track of entires and cents.
        This class supports calculations.
    """
    def __init__(self, entire, cent):
        """ initialize a Money object
        entire: entire euros
        cent: cents
        """
        self.entire=entire
        self.cent=cent
        self._normalize()

    def _normalize(self):
        """ take care that the value of cents
        contains a maximum of 99 """
        self.entire += self.cent //100
        self.cent  = self.cent % 100

    def __add__(self, other):
        """ add two Money objects.  It does not modify self
        argument:
        other - the other Money object
        """
        g = Money(self.entire+other.entire, self.cent+other.cent)
        return g

    def __rmul__(self, factor):
        """ multiply Money with a factor.  It does not modify self
        argument:
        factor - factor
        """
        g = Money(self.entire*factor, self.cent*factor)
        return g

    def __truediv__(self, factor):
        """ divide Money by a factor.  It does not modify self
        argument:
        factor - factor
        """
        g = Money(0, (self.entire*100+self.cent) / factor)
        return g

    def __mul__(self, factor):
        """ multiply Money with a factor.  It does not modify self
        parameter:
        factor - factor
        """
        g = Money(self.entire*factor, self.cent*factor)
        return g

    def __str__(self):
        """ Convert a Money object to a string
        """
        return "EUR %d,%02d" % (self.entire, self.cent)

g1=Money(2, 17)
print(g1)

g2=Money(2, 88)
print(g2)

print(g1+g2)

print(g1*7)
print(7*g1)

g3=g1*7
print(g3/3)

g4=Money(1, 32, "DKR")
g5=Money(7, 99, "DKR")

print(g4+g5)
print(g4+g3)        # should cause exception...
