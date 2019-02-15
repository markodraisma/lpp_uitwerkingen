
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
    print("{}: {} {}: {}".format(header[0],regel[0],
                                header[1],regel[1]), end="")
    if len(regel) == 3:
        print("{}: {}".format(header[2],regel[2]))
    else:
        print()

f.close()

