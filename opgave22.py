vraag = input("Stel een vraag: ") 
woord = vraag.split().pop()
woord = woord.rstrip("?")
woord = woord[1:]
medeklinkers = 'bcdfghjklmnpqrstvwxz'
medeklinkers += medeklinkers.upper()
while woord[0] in medeklinkers:
    woord = woord[1:]
woord = woord.capitalize()
print(woord)
