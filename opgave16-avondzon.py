#!/usr/bin/env python

bewoners = {'Thea' : 1926, 'Berendien' : 1919, 'Bertha' : 1912,
            'Theo' : 1923, 'Annegien'  : 1899, 'Gretha' : 1926}

import time
annonu = time.localtime().tm_year
# annonu = 2020
# Voeg hieronder de code toe die de 100+ers laat zien.

for naam in bewoners:
    geboortedatum = bewoners[naam]
    leeftijd = annonu - geboortedatum
    if leeftijd <100:
        continue
    print(naam, "is 100+, namelijk:", leeftijd, "Hoera!")
