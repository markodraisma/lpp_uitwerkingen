lengte =  input("Wat is uw lengte: ")
gewicht = input("Wat is uw gewicht: ")
lengte = int(lengte)
gewicht = int(gewicht)
bmi = (100*100*gewicht) / (lengte * lengte)

print("Uw BMI is", bmi)
