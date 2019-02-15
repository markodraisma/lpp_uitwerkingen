#!/usr/bin/env python3

import time

def zoek100plus(d_bewoners, annonu):
    gevonden = []
    d_bewoners = d_bewoners.copy()
    for naam in d_bewoners:
        geboortejaar = d_bewoners[naam]
        leeftijd = annonu - geboortejaar
        print('DEBUG:', naam, geboortejaar)
        if leeftijd >= 100:
            # persoon is ouder dan 100!
            print('DEBUG: >= 100!', leeftijd)
            gevonden.append(naam)
    return tuple(gevonden)

bewoners = {'Thea': 1926, 'Berendien': 1919, 'Bertha': 1912,
            'Theo': 1923, 'Annegien': 1899, 'Gretha': 1926 }

jaargetal = time.localtime().tm_year

print(zoek100plus(bewoners, jaargetal))
