import time

def zoek100plus(annonu, **d_bewoners):
    gevonden = []
    d_bewoners = d_bewoners.copy()
    for naam in d_bewoners:
        geboortejaar = d_bewoners[naam]
        leeftijd = annonu - geboortejaar
  #     print('DEBUG:', naam, geboortejaar)
        if leeftijd >= 100:
            # persoon is ouder dan 100!
  #         print('DEBUG: >= 100!', leeftijd)
            gevonden.append(naam)
    return tuple(gevonden)

bewoners = {'Thea': 1926, 'Berendien': 1919, 'Bertha': 1912,
            'Theo': 1923, 'Annegien': 1899, 'Gretha': 1926 }

jaargetal = time.localtime().tm_year

#print(zoek100plus(jaargetal, Jan = 1800))
print(zoek100plus(jaargetal, **bewoners))
