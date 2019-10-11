#! /usr/bin/env python3
import math
def isPriem(x):
    if x<=1: return False
    if x==2: return True
    if x%2==0: return False
    for deler in range(3,int(math.sqrt(x))+1,2):
       if x%deler==0: return False
    return True

for getal in range(1000):
    if isPriem(getal):
        print(getal)

del getal
del isPriem

