#!/usr/bin/env python3

from bonkmod import Bank, Bankrekening


# Maak een bank object
#
bonkbank   = Bank("Bonk Bank - Bonafide in Geldzaken")

# Maak drie bankrekening objecten
#
pietpuk    = Bankrekening("Pieter Puk")
diktrom    = Bankrekening("Dik Trom")
filantroop = Bankrekening("Filan Troop", 50000.00)

# Voeg de bankrekeningen toe aan de bank
#
bonkbank.openrekening(12345, pietpuk)
bonkbank.openrekening(54321, diktrom)
bonkbank.openrekening(67890, filantroop)

# Voer transacties uit
#
bonkbank.transactie(67890, 12345, 3000.00)
bonkbank.transactie(67890, 54321,   50.00)
bonkbank.transactie(54321, 12345,   35.99)
bonkbank.transactie(54321, 12345,   25.00)

# Toon alle bankrekeningen van de Bonk Bank
#
print(bonkbank)

for rekening, rekinfo in bonkbank:
    print("%9d\t%s" % (rekening, rekinfo))
