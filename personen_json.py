import json

personen = (
{
    "naam": {"voornaam": "Dagobert", "achternaam": "Duck"},
   "adres": {"straatnaam": "Krulplein", "huisnummer": 1, "postcode": "1111 AA", "plaatsnaam":"Duckstad"}
},
{
    "naam": {"voornaam": "Mickey", "achternaam": "Mouse"},
   "adres": {"straatnaam": "Onder de bomen", "huisnummer": 2, "postcode": "1110 AA", "plaatsnaam": "Duckstad"}
}
)

with open("personen.json", "wt") as f:
    json.dump(personen, f, indent=2)

with open("personen.json", "rt") as f2:
    personen2 = json.load(f2)

print("\nZijn personen en personen2 gelijk aan elkaar?")
print(personen == personen2, type(personen), type(personen2))

print("\nIs de inhoud van personen en personen2 gelijk aan elkaar?")
for i in range(len(personen)):
    print(personen[i]==personen2[i])


# vind snel het adres van Mickey Mouse
print("\nWat is het adres van Mickey Mouse?")
mickey = next(filter(lambda d:d["naam"]["voornaam"]=="Mickey", personen2))
for key in mickey["adres"]:
    print(key, mickey["adres"][key])

