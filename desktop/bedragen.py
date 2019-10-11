#! /usr/bin/env python3

bedragen = (500,200,100,50,20,10,5)
getal = int(input("Geef een bedrag: "))
while getal > 5:
  for bedrag in bedragen:
    hulp = getal // bedrag
    print(hulp, " x " , bedrag)
    getal %= bedrag
print("over: ", getal);
