#!/usr/bin/env python3

while True:
    try:
        lengte = input("Geef aub. uw lengte in cm's: " )
        lengte = int(lengte)
    except Exception:
        print("Geen geldige lengte, probeer opnieuw")
    else:
        if lengte <50 or lengte>250:
            print("Geen geldige lengte, buiten range 50cm-250cm")
        else:
            break


while True:

    while True:
        try:
            gewicht = input("Geef aub. uw gewicht in kg's (0 is stop): " )
            gewicht = int(gewicht)
        except Exception:
            print("Geen geldig gewicht, probeer opnieuw")
        else:
            break
    if gewicht == 0:
       break

    bmi = (100 * 100 * gewicht ) / (lengte * lengte)

    if bmi < 18:
        bericht = "te laag"
    elif bmi <=25:
        bericht = "gezond"
    else:
        bericht = "te hoog"
    print("Uw bmi is:", bmi, "en dat is", bericht,"\n")