#import re
f = open("verhaal.txt")

woorden = {}
woordenlijst = {}
i = 1
for regel in f:
    regel = regel.rstrip().lower()
    regel = regel.split()
    for woord in regel:
        woord = woord.strip(" ,.;:!")
        woorden[woord] = woorden.setdefault(woord,0)+1
        woordenlijst.setdefault(woord,[]).append(i)
    i+=1
        

for woord in sorted(woorden, key= lambda w:"%03d%s" % (100-woorden[w],w)):
    print(woord, woorden[woord])

for woord in sorted(woordenlijst):
    print(woord, woordenlijst[woord])
