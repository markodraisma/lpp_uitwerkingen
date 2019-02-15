#!/usr/bin/env python

lengte_s = input("Geef aub. uw lengte in cm's: " )
lengte = int(lengte_s)
gewicht_s = input("Geef aub. uw gewicht in kg's: " )
gewicht = int(gewicht_s)


bmi = (100 * 100 * gewicht ) / (lengte * lengte)

print(bmi)
