#!/usr/bin/env python

lijst = [1,5,2,33,5,16,7]

totaal = sum(lijst)
aantal = len(lijst)
gemiddelde = totaal/aantal
print(gemiddelde)
print(round(gemiddelde, 2))

aantal_5 = lijst.count(5)
print(aantal_5)
