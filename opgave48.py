def priemen(max, aantal=0):
    teller = 0
    for getal in range (2, max):
        priem=True
        for deler in range(2, getal):
            if deler<getal and getal%deler == 0:
                priem=False
                break                
        if priem: 
            yield(getal)
            teller+=1
        if aantal>0 and teller==aantal:
            return


priemgetallen = list( x for x in priemen(1000, 10))

print(priemgetallen)
