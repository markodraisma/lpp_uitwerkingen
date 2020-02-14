#!/usr/bin/env python3

namen = ['els', 'els', "jan", 'els', 'henk', 'henk', 'jan',"john", 'jan', 'john',
         'piet', 'Piet', 'els']

# namen.sort()

namen = list(map(lambda s: s.upper(), namen))

# gezien = []
for index, naam in enumerate(namen):
    if index >  namen.index(naam):                 # naam = jan, gezien =['els'], dus False
        print(index, naam)

















"""
for i in range(0,len(namen)):
    if i == 0: 
        continue
    if namen[i] == namen[i-1]:
        print(i, namen[i])

print()
gezien = None
for (i, naam) in enumerate(namen):
    if naam == gezien:
        print(i, naam)
    gezien = naam

print()


namen[1]='piet'
namen.append('john')
namen.insert(5,'jan')

print(namen)
print()
for (i, naam) in enumerate(namen):
    if naam in namen and i > namen.index(naam):
        print(i, naam)


print()

gezien = []

for(i, naam) in enumerate(namen):
    if naam in gezien:
        print(i, naam)
    else:
        gezien.append(naam)

print(gezien)
"""
