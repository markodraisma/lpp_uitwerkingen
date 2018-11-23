#!/usr/bin/env python3

mylist = [1,14,7,61,38,9,13]


print("Inhoud lijst:")
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1


print("Inhoud lijst omgekeerd:")
i = len(mylist)-1
while i >= 0:
    print(mylist[i])
    i -= 1


print("Inhoud lijst omgekeerd, met negatieve index:")
i = -1
while i >= - len(mylist):
    print(mylist[i], i)
    i -= 1
