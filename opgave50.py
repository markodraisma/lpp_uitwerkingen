#!/usr/bin/env python3

import time

class ParameterError(TypeError):
    pass

def zoek100plus(d_bewoners, annonu):
    fout = False
    fouten = []
    if not type(d_bewoners) == dict:
        fouten.append("Eerste parameter zou een dict moeten zijn, maar was %s" % type(d_bewoners))
        fout = True
    if not type(annonu) == int:
        fouten.append("Tweede parameter zou een int moeten zijn, maar was %s" % type(annonu))
        fout = True
    if fout:
        raise ParameterError(tuple(fouten))
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

try:
    print(zoek100plus(['jan', 'piet'],'2019'))
except TypeError as e:
    print("Er ging iets mis: ", e.args)
finally:
    print("Eindelijk klaar")
