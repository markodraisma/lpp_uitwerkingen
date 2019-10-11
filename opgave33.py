
try:
   f = open("bier.csv")
except Exception:
   import sys
   sys.exit("Fout bij openen bestand")

header = f.readline()
header = header.rstrip()
header = header.split("\t")

for regel in f:
    regel = regel.rstrip()
    regel = regel.split("\t")
    print("{kopnaam}: {naam:20s} | {kopbrouwerij}: {brouwerij}".format(
        kopnaam=header[0],naam=regel[0],
        kopbrouwerij=header[1],brouwerij=regel[1]), end="")
    if len(regel) >= 3:
        print(" | {kopplaats}: {plaats}".format(kopplaats=header[2],plaats=regel[2]))
    else:
        print()

f.close()

