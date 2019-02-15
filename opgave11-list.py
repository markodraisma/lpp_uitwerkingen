#!/usr/bin/env python3

mylist = [1,14,7,61,38,9,13]

aantal = len(mylist)

print("Inhoud lijst:")
i = 0
while i < aantal:
    print(mylist[i])
    i += 1


print("\nInhoud lijst omgekeerd:")
i = aantal-1
while i >= 0:
    print(mylist[i])
    i -= 1


print("\nInhoud lijst omgekeerd, met negatieve index:")
i = -1
while i >= -aantal:
    print(mylist[i], i)
    i -= 1
