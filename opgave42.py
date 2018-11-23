#!/usr/bin/env python3

import time

def zoek100plus(d_bewoners, annonu):
    centennials = []
    d_bewoners = d_bewoners.copy()
    for persoon in d_bewoners:
        naam = persoon
        jaar = d_bewoners[naam]
        leeftijd = annonu - jaar
        print('DEBUG:', persoon, d_bewoners[persoon])
        if leeftijd >= 100:
            # persoon is ouder dan 100!
            print('DEBUG: >= 100!', leeftijd)
            centennials.append(naam)
    return tuple(centennials)

bewoners = {'Thea': 1926, 'Berendien': 1919, 'Bertha': 1912,
            'Theo': 1923, 'Annegien': 1899, 'Gretha': 1926 }

jaargetal = time.localtime().tm_year

print(zoek100plus(bewoners, jaargetal))
