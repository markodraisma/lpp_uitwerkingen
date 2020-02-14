lengte = input("Wat is uw lengte (in cm)? ")
gewicht = input("Wat is uw gewicht (in kg)? ")
lengte = int(lengte)
gewicht = float(gewicht)

bmi = (100 * 100 * gewicht) / (lengte * lengte)

print(bmi)
