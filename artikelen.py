class Artikel:
    def __init__(self, naam, prijs):
        self.naam=naam
        self.prijs=prijs

    def totaal(self, aantal):
        return self.getprijs() * aantal

    def setprijs(self, prijs):
        if prijs>=0:
            self.prijs = prijs

    def getprijs(self):
        return self.prijs

    def __str__(self):
        return "Artikel met naam %s en prijs %s" % (self.naam, 
                self.getprijs())

class ArtikelMetKorting(Artikel):
    def __init__(self, naam, prijs, korting):
        super().__init__(naam, prijs)
        self.korting=korting

    def getprijs(self):
        return self.prijs - self.prijs * self.korting / 100

    def __str__(self):
        return super().__str__() + " (korting: %s %%)" % self.korting 

    
class Kassa:
    def __init__(self):
        self.totaal = 0
        self.bon = ""

    def scan(self, a, aantal):
        if isinstance(a, Artikel):
            totaal_artikelen = a.totaal(aantal)
            self.totaal+=totaal_artikelen
            self.bon+="%7s: %5d x %7.2f = %9.2f\n" % (a.naam, aantal
                    , a.getprijs()
                    , totaal_artikelen)

    def afrekenen(self):
        self.bon+="Totaal:                 %12.2f" % self.totaal
        print(self.bon)
        self.totaal=0
        self.bon=""

if __name__ == '__main__':
    pen = Artikel("pen", 1.5)
    potlood = Artikel("potlood", 0.8)
    gum = ArtikelMetKorting("gum", .75, 33)
    kassa = Kassa()
    kassa.scan(pen, 3)
    kassa.scan(potlood, 2)
    kassa.scan(gum, 2)
    kassa.afrekenen()


