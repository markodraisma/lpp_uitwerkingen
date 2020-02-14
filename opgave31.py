try:
    f = open("bitmap", "rb")
except Exception:
    import sys
    sys.exit("Bestand bitmap niet gevonden")

found = []
index = 0
while True:
    buf = f.read(1024)                # lees een deel in
    if not buf:                       # als niks is gelezen
        break                         # stop ermee
    for b in buf:                     # voor elke byte in de buffer
        if not b:                     # alle bits in byte staan op 0?
            index+=8                  # hoog index op voor volgende byte
            continue                  # sla deze byte over
        mask = 0b10000000             # masker met significante bit gezet 
        for i in range(8):            # ga alle 8 bits van de byte af
            if b & mask:              # als de bit gezet is in de byte
                found.append(index)   # voeg toe aan gevonden blok
            index += 1                # hoog index op
            mask >>=1                 # verplaats bit in masker naar rechts

print(found)

