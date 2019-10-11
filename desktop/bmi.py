#! /usr/bin/env python3
gewicht = input("Wat is je gewicht in kilo's? ")
lengte = input("Wat is je lengte in centimeters? ")
bmi = (100 * 100 * int(gewicht)) / ( int(lengte) ** 2)
print("Je BMI is: " , bmi)

