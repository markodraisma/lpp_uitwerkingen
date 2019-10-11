#import re
f = open("verhaal.txt")

#tekens=re.compile("[ .,;:!]")
woorden = {}
woordenlijst = {}
i = 1
for regel in f:
    regel = regel.rstrip().lower()
    #regel = tekens.split(regel)
    regel = regel.split()
    for woord in regel:
        woord = woord.strip(" ,.;:!")
        woorden[woord] = woorden.setdefault(woord,0)+1
        woordenlijst.setdefault(woord,[])
    #    if not i in woordenlijst[woord]:
        woordenlijst[woord].append(i)
    i+=1
        

for woord in sorted(woorden):
    print(woord, woorden[woord])

for woord in sorted(woordenlijst):
    print(woord, woordenlijst[woord])
