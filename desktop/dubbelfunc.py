#!/usr/bin/env python3

def dubbelen(lijst):
    """
    Maak list met indexnummers van de dubbele namen in lijst.
    De lijst moet gesorteerd zijn.
    Return-waarde is de list met index-nummers.
    """
    # voeg hieronder de ontbrekende code toe
    pass


namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dubbelen(namen)

print("De indexen van de duplicaten zijn:", dublist)
