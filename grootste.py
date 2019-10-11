#! /usr/bin/env python3
# bepaal de grootste van drie getallen

getal1 = input("Geef het eerste getal: ")
getal2 = input("Geef het tweede getal: ")
getal3 = input("Geef het derde getal: ")
hoogste = 0

if getal1 > getal2:
    hoogste = getal1
else:
    hoogste = getal2

if getal3 > hoogste:
    hoogste = getal3

print("De hoogste waarde was:", hoogste)
