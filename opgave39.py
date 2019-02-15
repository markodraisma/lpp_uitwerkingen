import re
f = open("verhaal.txt")

tekens=re.compile("[ .,;:!]")
woorden = {}

for regel in f:
    regel = regel.rstrip().lower()
    regel = tekens.split(regel)
    for woord in regel:
        woorden[woord] = woorden.setdefault(woord,0)+1

for woord in sorted(woorden):
    print(woord, woorden[woord])
