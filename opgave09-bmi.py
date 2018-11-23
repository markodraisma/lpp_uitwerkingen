#!/usr/bin/env python3

lengte_s = input("Geef aub. uw lengte in cm's: " )
lengte = int(lengte_s)
gewicht_s = input("Geef aub. uw gewicht in kg's: " )
gewicht = int(gewicht_s)


bmi = (100 * 100 * gewicht ) / (lengte * lengte)

bericht = ""

if bmi < 18:
    bericht = "te laag"
elif bmi <=25:
    bericht = "gezond"
else:
    bericht = "te hoog"

print("Uw bmi is:", bmi, "en dat is", bericht)

