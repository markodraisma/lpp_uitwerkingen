#!/usr/bin/env python3

#### Origineel:
# l = [ 1, 5, 2, 33, 5, 16, 7 ]
# 
# som = sum(l)
# 
# print("het gemiddelde van de", len(l), \
#       "items in", l, "is:", float(som)/len(l))

l = [ 1, 5, 2, 33, 5, 16, 7 ]

def gemiddelde(l):
    l = l[:]
    som = sum(l)
    return float(som) / len(l)

print("het gemiddelde van de", len(l), \
      "items in", l, "is:", gemiddelde(l))

def gemiddelde2(l):
    l = l[:]
    som = sum(l)
    aantal = len(l)
    return ( (float(som) / aantal), aantal)

gem, aantal = gemiddelde2(l)
print("het gemiddelde van de %d items in %s is: %.2f" % (
       aantal, l , gem ))

