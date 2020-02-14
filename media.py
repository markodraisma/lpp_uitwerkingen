#!/usr/bin/env python3

class Medium:
    """Een Medium klasse
    bedoeld als superclass van alle echte media
    """
    def __init__(self, titel, prijs):
        self.titel = titel
        self.prijs = prijs

    def show(self):
        print(self.titel, self.prijs, sep = "\n")

class Boek(Medium):
    """Een boek klasse
    """
    def __init__(self, titel, prijs, auteur, paginas):
        super().__init__(titel, prijs)
        self.auteur = auteur
        self.paginas = paginas

    def show(self):
        super().show()
        print(self.auteur, self.paginas, sep="\n")

class Strip(Boek):
   """Een strip klasse
   """
   def __init__(self, titel, prijs, auteur, paginas, tekenaar):
       super().__init__(titel, prijs, auteur, paginas)
       self.tekenaar=tekenaar

   def show(self):
       super().show()
       print(self.tekenaar)

#             titel             prijs   auteur                     paginas
leapr = Boek("Learning Python", 35.50, "Mark Lutz & David Ascher", 595)

#             titel                    prijs   auteur    pags tekenaar
astrx = Strip("Asterix en Cleopatra", 3.95, "Goscinny", 32, "Uderzo")

#             titel                    prijs   regisseur       leeftijd
# spody = Dvd("2001, a space odyssey", 17.50, "Stanley Kubrik", 12)

leapr.show()    # druk leapr af
print()
astrx.show()
# spody.show()
