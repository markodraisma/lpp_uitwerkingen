lengte = input("Geef een lengte op in cm: ");
gewicht = input("Geef een gewicht in kg: ")

lengte = int(lengte)
gewicht = float(gewicht)

print("lengte:  ", lengte)
print("gewicht: ", gewicht)

bmi = 100 ** 2  * gewicht / lengte ** 2 

print("Uw bmi is", round(bmi,1)) 
