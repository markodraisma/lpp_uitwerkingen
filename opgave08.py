#!/usr/bin/env python

getallen = {'een':1}
print(getallen['een'])

getallen['twee']=2
print(getallen['twee'])


getallen['een']='EEN'
print(getallen)

a = [1,2,3]
b = a
c = a[:]
d = [a, c]

print(d[0][1])
