#!/usr/bin/env python

geld = input("Geef het terug te geven bedrag op: ")
geld = int(geld)
# tuple is hier geschikt: de waarden van de briefjes kunnen niet gewijzigd worden
briefjes = (500,200,100,50,20,10,5)

for briefje in briefjes:
    aantal = geld // briefje
    print(aantal, "briefjes van", briefje)
    geld %= briefje
	
print("rest in euro's", geld)

