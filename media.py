#!/usr/bin/env python3

class Medium(object):
    """Een Medium klasse
    bedoeld als superclass van alle echte media
    """
    pass

class Boek(Medium):
    """Een boek klasse
    """
    pass 


#             titel             prijs   auteur                     paginas
leapr = Boek("Learning Python", 35.50, "Mark Lutz & David Ascher", 595)

#             titel                    prijs   auteur    pags tekenaar
# astrx = Strip("Asterix en Cleopatra", 3.95, "Goscinny", 32, "Uderzo")

#             titel                    prijs   regisseur       leeftijd
# spody = Dvd("2001, a space odyssey", 17.50, "Stanley Kubrik", 12)

leapr.show()    # druk leapr af

# astrx.show()
# spody.show()
