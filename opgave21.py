bestanden = ['limerick.txt', 'news.1.pdf', 'verhaal']
for bestand in bestanden:
    delen = bestand.split(".")
    if len(delen)>1:
        delen.pop()
    print(".".join(delen));
print()

for bestand in bestanden:
    delen = bestand.rsplit(".",1)
    print(delen[0]);

print()
for bestand in bestanden:
    pos = bestand.rfind(".")
    if(pos>=0):
        print(bestand[:pos])
    else:
        print(bestand)

zin = 'Hoeveel e\'s zitten er in deze zin?'
print(zin, zin.lower().count("e"))
