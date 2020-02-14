lengte = input("Geef aub. uw lengte in cm's: " )
lengte = int(lengte)
gewicht = input("Geef aub. uw gewicht in kg's: " )
gewicht = int(gewicht)

while gewicht != 0:
    bmi = (100 * 100 * gewicht ) / (lengte * lengte)
    print("Uw bmi is ", bmi)
    if bmi<18:
        print("Dat is te laag")
    elif bmi<=25:
        print("Dat is een gezonde bmi")
    else:
        print("Dat is te hoog")
    gewicht = input("Geef aub. uw (streef-)gewicht in kg's: " )
    gewicht = int(gewicht)

print("Einde oefening")
