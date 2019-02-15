#!/usr/bin/env python

bewoners = {'Thea' : 1926, 'Berendien' : 1919, 'Bertha' : 1912,
            'Theo' : 1923, 'Annegien'  : 1899, 'Gretha' : 1926}

import time
annonu = time.localtime().tm_year
gevonden = False
# annonu = 1900
# Voeg hieronder de code toe die de 100+ers laat zien.
for persoon in bewoners:
    geboortedatum = bewoners[persoon]
    leeftijd = annonu - geboortedatum 
    if leeftijd >= 100:
        print(persoon, ' is meer dan 100, namelijk: ',leeftijd, 'hoera!')
        gevonden = True
    else:    
        print("Er is niemand meer dan 100")
