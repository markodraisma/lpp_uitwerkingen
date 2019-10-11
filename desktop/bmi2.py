#! /usr/bin/env python3
gewicht = input("Wat is je gewicht in kilo's? ")
lengte = input("Wat is je lengte in centimeters? ")
bmi = (100 * 100 * int(gewicht)) / ( int(lengte) ** 2)
print("Je BMI is: " , bmi)
if bmi < 18:
  print("Pas op, dit is te laag!")
elif bmi > 25:
  print("Pas op, dit is te zwaar!")
else:
  print("Dit is een gezond gewicht")
