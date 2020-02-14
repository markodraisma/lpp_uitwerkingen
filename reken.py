#! /urr/bin/env python3

import sys

if len(sys.argv) != 3:
    sys.exit("Geef twee getallen mee")

a, b = tuple(map(float, sys.argv[1:3]))
print(a, "+", b, "=", a+b)
 
