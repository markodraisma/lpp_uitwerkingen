vraag = input("Stel een vraag: ") 
vraag = vraag.rstrip()
vraag = vraag.rstrip("?")
vraag = vraag.rstrip()
woord = vraag.split().pop()
woord = woord[1:]
medeklinkers = 'bcdfghjklmnpqrstvwxz'
medeklinkers += medeklinkers.upper()
while woord[0] in medeklinkers:
    woord = woord[1:]
# of:
# woord = woord.lstrip(medeklinkers)
woord = woord.capitalize()
print(woord)
