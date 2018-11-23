#!/usr/bin/env python3

import opgave46dubmod

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De invoerlijst wordt:", namen)

dublist = opgave46dubmod.dubbelen(namen)

print("De indexen van de duplicaten zijn:", dublist)
