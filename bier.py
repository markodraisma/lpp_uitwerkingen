bestandsnaam = "bier.csv"

try:
    bestand = open(bestandsnaam)
except Exception:
    import sys
    sys.exit("Er ging iets mis bij het openen van %s." % bestandsnaam)

header = bestand.readline()
header = header.rstrip()
header = header.split("\t")

kopnaam = header[0]
kopbrouwerij = header[1]

for i, regel in enumerate(bestand):
    regel = regel.rstrip()
    regel = regel.split("\t")
    naam = regel[0]
    brouwerij = regel[1]
    regel = "{kopnaam:s}: {naam:s}, {kopbrouwerij:s}: {brouwerij:s}".format(
             kopnaam=kopnaam, kopbrouwerij=kopbrouwerij,naam=naam,brouwerij=brouwerij)
    print(regel)
    if i == 5:
        break

bestand.close()


