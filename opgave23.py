uurwaarden = "673,1449,82,119341,13,996308,53,7,4711,2,189320"
uurwaarden = uurwaarden.split(",")
print(uurwaarden)
totaal = 0

for index, getal in enumerate(uurwaarden):
    totaal += int(getal)
 #  print( "Uur %2d: %7s" % (index + 1, getal))
    print( "Uur {:>2d}: {:>7s} ".format(index + 1, getal))

#  print("Totaal: %7d" % totaal)
print("Totaal: {:>7d}".format(totaal))
