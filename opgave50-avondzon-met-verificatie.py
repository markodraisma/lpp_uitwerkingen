#!/usr/bin/env python3

import time

bewoners = {'Thea': 1926, 'Berendien': 1919, 'Bertha': 1912,
            'Theo': 1923, 'Annegien': 1899, 'Gretha': 1926 }

jaargetal = time.localtime().tm_year

class ParameterError(TypeError):
    pass

def zoek100plus(d_bewoners, annonu):
    centennials = []
    if not (type(d_bewoners) == dict):
        raise ParameterError('1e parameter moet een dict zijn, ipv. %s!' % 
                        type(d_bewoners))
    if not (type(annonu) == int):
        raise ParameterError('2e parameter moet een integer zijn, ipv. %s!' %
                        type(annonu))

    d_bewoners = d_bewoners.copy()
    for persoon in d_bewoners:
        # print('DEBUG:', persoon, d_bewoners[persoon])
        if (annonu - d_bewoners[persoon]) >= 100:
            # persoon is ouder dan 100!
            # print('DEBUG: >= 100!', annonu - d_bewoners[persoon])
            centennials.append(persoon)
    return tuple(centennials)

try:
    print(zoek100plus(bewoners, jaargetal))
    # honderdplussers = zoek100plus(['piet', 'jan'], jaargetal)
    honderdplussers = zoek100plus(bewoners, '2018')
except TypeError as e:
    print('Fout in aanroepen van functie zoek100plus:', e.args[0])
