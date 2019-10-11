#!/usr/bin/env python3

namen = ['els', 'els', 'els', 'els', 'henk', 'henk', 'jan', 'jan', 'john',
         'piet', 'piet']

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
