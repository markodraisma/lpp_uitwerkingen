#!/usr/bin/env python3

lengte_s = input("Geef aub. uw lengte in cm's: " )
lengte = int(lengte_s)

while True:
    gewicht_s = input("Geef aub. uw gewicht in kg's: " )
    try:
        gewicht = int(gewicht_s)
    except ValueError:
        print('Grag numerieke waarden, aub.')
        continue
    if gewicht == 0:
        break
        

    # gevaar! -> wat als lengte = 0?
    bmi = (100 * 100 * gewicht ) / (lengte * lengte)
    print(bmi)
