#!/usr/bin/env python

lengte = input("Geef aub. uw lengte in cm's: " )
lengte = int(lengte)
gewicht = float(input("Geef aub. uw gewicht in kg's: " ))
# gewicht = int(gewicht)


bmi = 100 * 100 * gewicht  / lengte ** 2

print("Uw BMI is:", bmi)
