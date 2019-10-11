#!/usr/bin/env python
geld = 1788 
# geld = int(geld)

briefjes = (500,200,100,50,20,10,5)
for briefje in briefjes:
    aantal = geld//briefje
    print(aantal, "briefjes van", briefje)
    geld%=briefje
print("rest in euro's", geld)

