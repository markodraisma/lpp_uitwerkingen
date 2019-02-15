try:
    f = open("weer.txt")
except Exception:
    import sys
    sys.exit("Foutje")

temp_tot = 0;
aantal = 0
steden = {}
for regel in f:
    if regel[0] == '#':
        continue
    regel = regel.split()
    temp = float(regel[-1])
    stad = " ".join(regel[:-1])
    steden[stad]=temp
    aantal +=1
    temp_tot += temp

gemiddeld = temp_tot / aantal
print("gemiddelde temperatuur:", gemiddeld)
laag = []
hoog = []
# keys = tuple(stad for stad in sorted(steden))
for stad in sorted(steden):
    if steden[stad]<gemiddeld:
        laag.append(tuple([stad, steden[stad]]))
    else:
        hoog.append(tuple([stad, steden[stad]]))
print("\nsteden onder het gemiddelde:")
for k, v in laag:
    print("{}: {}".format(k, v))
print("\nsteden boven of op het gemiddelde:")
for k, v in hoog:
    print("{}: {}".format(k, v))

f.close()

