uurwaarden = "673,1449,82,119341,13,996308,53,7,4711,2123435436,189320"

uurwaarden = uurwaarden.split(",")
totaal = 0
for uur in uurwaarden:
    totaal+=int(uur)
lengte = len(str(totaal))

melding = "Uur {{:2d}}: {{:{}d}}".format(lengte) # "Uur {:2d}: {:7d}"
print("DEBUG - melding is nu:", melding)

for nr, uur in enumerate(uurwaarden):
    uur = int(uur)
    print(melding.format(nr+1, uur))

print("Totaal:", totaal)
