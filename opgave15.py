tekst = """ Dit is een voorbeeld, met nog wat # andere tekens.
Het is de bedoeling om klinkers EN medeklinkers te tellen"""

klinkers = 0
medeklinkers = 0

for teken in tekst:

    if teken in "AEIOUYaeiouy":
        klinkers +=1
    elif teken in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        medeklinkers+=1


print("Klinkers:", klinkers, "Medeklinkers:", medeklinkers)

