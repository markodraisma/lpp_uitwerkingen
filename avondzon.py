#!/usr/bin/env python3

bewoners = {'Thea' : 1926, 'Berendien' : 1919, 'Bertha' : 1912,
            'Theo' : 1923, 'Annegien'  : 1899, 'Gretha' : 1926}

import time
annonu = time.localtime().tm_year

# Voeg hieronder de code toe die de 100+ers laat zien.
for persoon in bewoners:
    leeftijd = annonu - bewoners[persoon]
    if leeftijd >= 100:
        print(persoon, ' is meer dan 100, namelijk: ',leeftijd, 'hoerra')
