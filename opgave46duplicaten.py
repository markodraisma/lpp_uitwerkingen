#!/usr/bin/env python3

import opgave46dubmod as dm

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dm.dubbelen(namen)

print(dublist)
print("documentatie bij module:", dm.__doc__)
print("documentatie bij functie:", dm.dubbelen.__doc__)
