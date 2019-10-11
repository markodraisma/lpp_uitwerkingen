uurwaarden = "673,1449,82,100019341,13,996308,53,7,4711,2,189320"

uurwaarden = uurwaarden.split(",")
totaal = 0
# totaal = sum(map(int,uurwaarden))
for uur in uurwaarden:
    totaal+=int(uur)
lengte = len(str(totaal))
melding = "Uur %%2d: %%%dd" % lengte  #  "Uur %2d: %7d"
print("DEBUG - melding is nu:", melding)

for nr, uur in enumerate(uurwaarden):
    uur = int(uur)
    print(melding % (nr+1, uur))
print("Totaal:", totaal)
