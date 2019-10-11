import math
for getal in range (2, 1001):
    priem=True
    for deler in range(2, int(math.sqrt(getal)+1)):
        if getal%deler == 0:
            priem=False
            continue
    if priem: print(getal)
