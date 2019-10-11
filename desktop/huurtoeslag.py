#! /usr/bin/env python3

leeftijd = int(input("wat is uw leeftijd? "))
aantal = int(input("hoeveel bewoners? "))
huur = int(input("wat is uw huurbedrag? "))
inkomen = int(input("wat is uw inkomen? "))
vermogen = int(input("wat is uw vermogen? "))
huurtoeslag=False;
aantalinkomenvermogen = (aantal == 1 and inkomen <= 22000 and vermogen <=21000) or (aantal>1 and inkomen <300000 and vermogen <= 42000)
if leeftijd < 23:
    if huur >= 231 and huur <= 409 and aantalinkomenvermogen:
            huurtoeslag = True
elif huur >=231 and huur <= 710 and aantalinkomenvermogen:
    huurtoeslag = True
if huurtoeslag:
    print("U heeft wel recht op huurtoeslag")
else:
    print("U heeft geen recht op huurtoeslag")
