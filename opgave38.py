try:
    f = open("weer.txt")
except Exception:
    import sys
    sys.exit("Foutje")

#temp_tot = 0;
#aantal = 0
steden = {}
for regel in f:
    if regel[0] == '#':
        continue
    regel = regel.split()
    try:
        temp = float(regel[-1])
    except Exception:
        continue
    stad = " ".join(regel[:-1])
    steden[stad]=temp
  #  aantal +=1
  #  temp_tot += temp

gemiddeld = sum(steden.values()) / len(steden)
print("gemiddelde temperatuur:", gemiddeld)
laag = []
hoog = []
for stad in sorted(steden):
    temp = steden[stad]
    if temp<gemiddeld:
        laag.append(tuple([stad, temp]))
    else:
        hoog.append(tuple([stad, temp]))

#print(laag)
#print()
#print(hoog)

print("\nsteden onder het gemiddelde:")
for s, t in laag:
    print("{}: {}".format(s, t))
print("\nsteden boven of op het gemiddelde:")
for s, t in hoog:
    print("{}: {}".format(s, t))

f.close()

