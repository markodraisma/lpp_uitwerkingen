#!/usr/bin/env python3

class Geld(object):
    """Een Geld klasse.  Houdt helen en centen bij
    met deze klasse kan ook gerekend worden
    """
    def __init__(self, heel, cent):
        """Initialiseer een Geld object
        heel: de helen
        cent: de centen
        """
        self.heel=heel
        self.cent=cent
        self._normalize()

    def _normalize(self):
        """zorg ervoor dat een object altijd
        hooguit 99 centen bevat"""
        self.heel += self.cent//100
        self.cent = self.cent % 100

    def __add__(self, ander):
        """tel twee Geldobjecten op.  Verandert self niet
        parameter:
        ander - het andere Geld object
        """
        g=Geld(self.heel+ander.heel, self.cent+ander.cent)
        return g

    def __rmul__(self, factor):
        """Vermenigvuldig Geld met een factor.  Verandert self niet
        parameter:
        factor - de factor
        """
        g=Geld(self.heel*factor, self.cent*factor)
        return g

    def __truediv__(self, factor):
        """Deel Geld door een factor.  Verandert self niet
        parameter:
        factor - de factor
        """
        g=Geld(0, (self.heel*100+self.cent) / factor)
        return g

    def __mul__(self, factor):
        """Vermenigvuldig Geld met een factor.  Verandert self niet
        parameter:
        factor - de factor
        """
        g=Geld(self.heel*factor, self.cent*factor)
        return g

    def __str__(self):
        """Maak string van een Geld object
        """
        return "EUR %d,%02d" % (self.heel, self.cent)

g1=Geld(2, 17)
print(g1)

g2=Geld(2, 88)
print(g2)

print(g1+g2)

print(g1*7)
print(7*g1)

g3=g1*7
print(g3/3)

g4=Geld(1, 32, "DKR")
g5=Geld(7, 99, "DKR")

print(g4+g5)
print(g4+g3)        # moet een exception geven...
