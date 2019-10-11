while True:
    try:
        lengte = input("Geef aub. uw lengte in cm's: " )
        lengte = int(lengte)
        gewicht = input("Geef aub. uw gewicht in kg's: " )
        gewicht = int(gewicht)
    except Exception:
        print("Geen geldig getal opgegeven")
    else:
        break

while True:
    bmi = (100 * 100 * gewicht ) / (lengte * lengte)
    print("Uw bmi is ", bmi)
    if bmi<18:
        print("Dat is te laag")
    elif bmi<=25:
        print("Dat is een gezonde bmi")
    else:
        print("Dat is te hoog")
    gewicht = input("Geef aub. uw (streef-)gewicht in kg's: " )
    if gewicht == '0' or len(gewicht)==0:
      break
    gewicht = int(gewicht)

print("Einde oefening")
