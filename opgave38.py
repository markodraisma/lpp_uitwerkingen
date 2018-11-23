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

print("steden onder het gemiddelde:")
for stad in sorted(steden):
    if steden[stad]<gemiddeld:
        print(stad, steden[stad])
print("steden boven of op het gemiddelde:")
for stad in sorted(steden):
    if steden[stad]>=gemiddeld:
        print(stad, steden[stad])

f.close()

