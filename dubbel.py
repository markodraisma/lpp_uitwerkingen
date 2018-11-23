#!/usr/bin/env python3

namen = [ 'els', 'els', 'els', 'els', 'henk', 'henk',
          'jan', 'jan', 'john', 'piet', 'piet' ]

# voeg hieronder je eigen code toe

vorige = None
for i, naam in enumerate(namen):
    if naam == vorige:
        print(i, naam)
    vorige = naam
print()
for i in range(1, len(namen)):
    if namen[i] == namen[i-1]:
        print(i, namen[i])
