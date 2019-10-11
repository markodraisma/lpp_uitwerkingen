#! /usr/bin/env python3

from dieren import Dier, Vogel

a = Dier(4)
if isinstance(a, Dier):
  print(a)


b = Vogel()
if isinstance(b, Dier):
  print(b)

print(b.compareTo(a))

print(a.compareTo(3))
