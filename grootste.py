v1 = input("Geef eerste getal: ")
v2 = input("Geef tweede getal: ")
v3 = input("Geef derde getal: ")

print(v1, v2, v3)

if v1 > v2:
    grootste = v1
else:
    grootste = v2

if v3 > grootste:
    grootste = v3

print("De hoogste waarde was: ", grootste)
