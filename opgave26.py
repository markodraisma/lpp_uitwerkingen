#!/usr/bin/env python3

namen = ['els', 'els', 'els', 'els', 'henk', 'henk', 'jan', 'jan', 'john',
         'piet', 'piet']

for i in range(1,len(namen)):
    if namen[i] == namen[i-1]:
        print(i, namen[i])


gezien = None
for (i, naam) in enumerate(namen):
    if naam == gezien:
        print(i, naam)
    gezien = naam

namen[1]='piet'
namen.append('john')
namen.insert(5,'jan')

print(namen)

gezien = []

for(i, naam) in enumerate(namen):
    if naam in gezien:
        print(i, naam)
    else:
        gezien.append(naam)

