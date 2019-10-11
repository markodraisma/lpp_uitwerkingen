#! /usr/bin/env python3

class Dier:

  def __init__(self, aantal):
    self.aantalPoten = aantal;

  def getAantalPoten(self):
      return self.aantalPoten

  def compareTo(self, other):
    if isinstance(other, Dier):
      return self.aantalPoten - other.aantalPoten
    else:
      raise Exception(str(other) + " is geen dier")

  def __str__(self):
    return "%s met %d poten" % (self.__class__.__name__, self.aantalPoten)

class Vogel(Dier):

  def __init__(self):
    super().__init__(2)
