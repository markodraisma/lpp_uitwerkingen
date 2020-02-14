# Haal extensie af van de naam (alleen rechter deel na de punt, als die bestaat)

bestanden = ['limerick.txt', 'news.1.pdf', 'verhaal']

# manier 1: gebruik split() en join()
for bestand in bestanden:
    # splits op alle punten, indien aanwezig
    delen = bestand.split(".")    # delen = ["news", "1", "pdf"]
    if len(delen)>1:
        delen.pop()               # delen = ["news", "1"]
    print(".".join(delen))
print()



# manier 2: gebruik rsplit()
for bestand in bestanden:
    # splits alleen op rechter punt, indien aanwezig
    delen = bestand.rsplit(".", 1) # delen = ["new.1", "pdf"]
    print(delen[0])
print()



# manier 3: gebruik rfind()
for bestand in bestanden:
    # zoek positie van meest rechter punt
    index_punt = bestand.rfind(".")
    # indien gevonden
    if(index_punt>=0):
	    #toon deel na de punt
        print(bestand[:index_punt]) 
    else:
        print(bestand)

zin = 'Hoeveel e\'s zitten er in deze zin?'
print(zin, zin.lower().count("e"))









