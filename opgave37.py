#!/usr/bin/env python3


mijndict = { 'een':1, 'twee':2, 'drie':3 }
sleutel = "een"
waarde = mijndict[sleutel]

waarde = mijndict.get(sleutel)

d_leeg = {}
s_leeg = set([])

s = {1,4,2,6,7,6,2}
print(s)
print(d_leeg)
print(s_leeg)

del mijndict['een']
mijndict.pop("twee")

maanden = { 1:'jan', 2: 'feb', 3:'mrt' }

for maand in maanden:
    # print(maand)
    print(maand, maanden[maand])

for nr, naam in maanden.items():
    print(nr, naam)



