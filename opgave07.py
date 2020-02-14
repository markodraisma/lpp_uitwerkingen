#!/usr/bin/env python

lijst = [100,50,2000,33,5,16,7]
print("de inhoud van de lijst is:", lijst)

totaal = sum(lijst)
aantal = len(lijst)
gemiddelde = totaal /aantal

print("de gemiddelde waarde is:", gemiddelde)
afgerond = round( gemiddelde, -1)
print("afgerond is dat :", afgerond)
