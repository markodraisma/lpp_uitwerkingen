mylist = [1,14,7,61,38,9,13]

for getal in mylist:
    print(getal)
    

for nummer, getal in enumerate(mylist):
    print("nr", nummer+1, "=", getal)

print()

tafel = 5
for getal in range(1, 11):
    print(getal, 'x', tafel, '=', getal*tafel)


print()
for getal, uitkomst in enumerate(range(tafel, tafel*11, tafel)):
    print(getal+1, 'x', tafel, '=', uitkomst)

