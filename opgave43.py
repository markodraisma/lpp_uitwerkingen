#!/usr/bin/env python3

def dubbelen(l_namen):
    l_namen = l_namen[:]
#    l_dubbelen = []
#    for idx in range(1,len(l_namen)):
#        if l_namen[idx]==l_namen[idx-1]:
#            l_dubbelen.append(idx)
#    return tuple(l_dubbelen)
    return tuple([idx for idx in 
        range(1,len(l_namen)) if l_namen[idx]==l_namen[idx-1]])

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dubbelen(namen)

print(dublist)
