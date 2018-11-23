#!/usr/bin/env python3

while True:
    try:
        lengte_s = input("Geef aub. uw lengte in cm's: " )
        lengte = int(lengte_s)
    except Exception:
        print("Geen geldige lengte, probeer opnieuw")
    else:
        break


while True:

    while True:
        try:
            gewicht_s = input("Geef aub. uw gewicht in kg's (0 is stop): " )
            gewicht = int(gewicht_s)
        except Exception:
            print("Geen geldig gewicht, probeer opnieuw")
        else:
            break
    if gewicht == 0:
       break

    bmi = (100 * 100 * gewicht ) / (lengte * lengte)

    bericht = ""

    if bmi < 18:
        bericht = "te laag"
    elif bmi <=25:
        bericht = "gezond"
    else:
        bericht = "te hoog"
    print("Uw bmi is:", bmi, "en dat is", bericht)
