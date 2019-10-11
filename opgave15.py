tekst = """ Dit is een voorbeeld, met nog wat # andere tekens.
Het is de bedoeling om klinkers EN medeklinkers te tellen"""

aantal_klinkers = 0
aantal_medeklinkers = 0
letters = "".join(chr(a) for a in range(ord('a'),ord('z')+1))
letters += letters.upper()
klinkers = 'aeiouy'
klinkers += klinkers.upper()

print(letters)

for teken in tekst:
    if teken in klinkers:
        aantal_klinkers +=1
    elif teken in letters: 
        # "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        aantal_medeklinkers+=1

print("Klinkers:", aantal_klinkers, "Medeklinkers:", aantal_medeklinkers)

