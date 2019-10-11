#!/usr/bin/env python

getallen = {'een':1}
print(getallen['een']) # verwachte uitkomst: 1

getallen['twee']=2
print(getallen['twee']) # verwachte uitkomst: 2


getallen['een']='EEN'
print(getallen)

a = [1,2,3]
b = a
c = a[:]
d = [a, c]

print(d[0][1])
