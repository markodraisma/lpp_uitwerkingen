#!/usr/bin/env python3

from opgave46dubmod import dubbelen

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dubbelen(namen)

print(dubbelen(namen))
