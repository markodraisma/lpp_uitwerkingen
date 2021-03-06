#!/usr/bin/env python3

def dubbelen(l_namen):
    l_namen = l_namen[:]
    vorige = ''
    l_dubbelen = []
    for idx,elem in enumerate(namen):
        if elem == vorige:
            # print(idx)
            l_dubbelen.append(idx)
        else:
            vorige = elem
    return l_dubbelen


def listuniq(lijst, dubbelen):
    for index in dubbelen[::-1]:
        lijst.pop(index)

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dubbelen(namen)

print(dublist)

listuniq(namen, dublist)

print("Na ontdubbelen:", namen)
