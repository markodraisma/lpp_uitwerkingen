while True:
    try:
        lengte = input("Geef aub. uw lengte in cm's: " )
        lengte = int(lengte)
        gewicht = input("Geef aub. uw gewicht in kg's: " )
        gewicht = int(gewicht)
    except Exception:
        print("Gebruik alleen gehele getallen")
    else:  
        break

while True:
    if gewicht == 0:
        break
    bmi = (100 * 100 * gewicht ) / (lengte * lengte)
    print("Uw bmi is ", bmi)
    if bmi<18:
        print("Dat is te laag")
    elif bmi<=25:
        print("Dat is een gezonde bmi")
    else:
        print("Dat is te hoog")
    while True:
        try:
            gewicht = input("Geef aub. uw (streef-)gewicht in kg's: " )
            gewicht = int(gewicht)
        except Exception:
            print("gebruik alleen gehele getallen")
        else:
            break

print("Einde oefening")








