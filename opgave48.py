def priemen(max, aantal=0):
    teller = 0
    for getal in range (2, max):
        for deler in range(2, getal):
            if getal%deler == 0:
                break                
        else: 
            yield(getal)
            teller+=1
            if aantal>0 and teller==aantal:
                return


priemgetallen = list( x for x in priemen(100))

print(priemgetallen)
