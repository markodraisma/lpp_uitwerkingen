#!/usr/bin/env python3

def dubbelen(l_namen):
    l_namen = l_namen[:]
    gevonden = []
    l_dubbelen = []
    for idx,elem in enumerate(namen):
        if elem in gevonden:
            # print(idx)
            l_dubbelen.append(idx)
        else:
            gevonden.append(elem)
            vorige = elem
    return l_dubbelen

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

# namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dubbelen(namen)

print(dubbelen(namen))
