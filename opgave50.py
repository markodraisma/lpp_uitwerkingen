bewoners = {'Thea' : 1926, 'Berendien' : 1919, 'Bertha' : 1912,
            'Theo' : 1923, 'Annegien'  : 1899, 'Gretha' : 1926}
import time
annonu = time.localtime().tm_year
# annonu = 1900
# Voeg hieronder de code toe die de 100+ers laat zien.

def zoek100plus(d_bewoners, jaar):
    fouten = []
    if type(d_bewoners) != dict:
        fouten.append("TypeError: Type van eerste argument moet een dict zijn")
    if type(jaar) != int:
        fouten.append("TypeError: Type van tweede argument moet een int zijn")
    if len(fouten)>0:
        raise TypeError(*fouten)
    for naam in d_bewoners:
        geboortedatum = d_bewoners[naam]
        leeftijd = jaar - geboortedatum
        if leeftijd >=100 :
            print(naam, "is 100 of ouder, namelijk", leeftijd, "Hoera!")

try:
    zoek100plus(['jan', 'piet'], '2019')
except TypeError as te:
    for fout in te.args:
        print(fout)
    print()

try:
    zoek100plus(bewoners, 2020)
except TypeError as te:
    print(te.args)
