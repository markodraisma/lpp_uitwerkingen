uurwaarden = "673,1449,82,119341,13,996308,53,7,4711,2,189320"

uurwaarden = uurwaarden.split(",")
totaal = 0
for nr, uur in enumerate(uurwaarden):
    melding = "Uur %2d: %7d" % (nr+1, int(uur))
    # print("Uur ",nr+1, ": ", uur, sep="")
    print(melding)
    totaal += int(uur)
print("Totaal:", totaal)
